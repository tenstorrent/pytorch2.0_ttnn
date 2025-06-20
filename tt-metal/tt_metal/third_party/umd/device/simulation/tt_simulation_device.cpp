/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include "umd/device/tt_simulation_device.h"

#include <nng/nng.h>
#include <uv.h>

#include <iostream>
#include <string>
#include <tt-logger/tt-logger.hpp>
#include <vector>

#include "assert.hpp"
#include "tt_simulation_device_generated.h"
#include "umd/device/driver_atomics.h"

flatbuffers::FlatBufferBuilder create_flatbuffer(
    DEVICE_COMMAND rw, std::vector<uint32_t> vec, tt_xy_pair core_, uint64_t addr, uint64_t size_ = 0) {
    flatbuffers::FlatBufferBuilder builder;
    auto data = builder.CreateVector(vec);
    auto core = tt_vcs_core(core_.x, core_.y);
    uint64_t size = (size_ == 0 ? vec.size() * sizeof(uint32_t) : size_);
    auto device_cmd = CreateDeviceRequestResponse(builder, rw, data, &core, addr, size);
    builder.Finish(device_cmd);
    return builder;
}

void print_flatbuffer(const DeviceRequestResponse* buf) {
    std::vector<uint32_t> data_vec(buf->data()->begin(), buf->data()->end());
    uint64_t addr = buf->address();
    uint32_t size = buf->size();
    tt_xy_pair core = {buf->core()->x(), buf->core()->y()};

    std::stringstream ss;
    ss << std::hex << reinterpret_cast<uintptr_t>(addr);
    std::string addr_hex = ss.str();

    std::stringstream data_ss;
    for (int i = 0; i < data_vec.size(); i++) {
        data_ss << "0x" << std::hex << std::setw(8) << std::setfill('0') << data_vec[i] << " ";
    }
    std::string data_hex = data_ss.str();

    log_debug(tt::LogEmulationDriver, "{} bytes @ address {} in core ({}, {})", size, addr_hex, core.x, core.y);
    log_debug(tt::LogEmulationDriver, "Data: {}", data_hex);
}

tt_SimulationDeviceInit::tt_SimulationDeviceInit(const std::filesystem::path& simulator_directory) :
    simulator_directory(simulator_directory), soc_descriptor(simulator_directory / "soc_descriptor.yaml", false) {}

tt_SimulationDevice::tt_SimulationDevice(const tt_SimulationDeviceInit& init) : Chip(init.get_soc_descriptor()) {
    log_info(tt::LogEmulationDriver, "Instantiating simulation device");
    soc_descriptor_per_chip.emplace(0, init.get_soc_descriptor());
    arch_name = init.get_arch_name();
    target_devices_in_cluster = {0};

    // Start VCS simulator in a separate process
    std::filesystem::path simulator_path = init.get_simulator_path();
    if (!std::filesystem::exists(simulator_path)) {
        TT_THROW("Simulator binary not found at: ", simulator_path);
    }
    uv_loop_t* loop = uv_default_loop();
    uv_process_t child_p;
    uv_process_options_t child_options = {0};
    std::string simulator_path_string = simulator_path;

    child_options.file = simulator_path_string.c_str();
    child_options.flags = UV_PROCESS_DETACHED;

    int rv = uv_spawn(loop, &child_p, &child_options);
    if (rv) {
        TT_THROW("Failed to spawn simulator process: ", uv_strerror(rv));
    } else {
        log_info(tt::LogEmulationDriver, "Simulator process spawned with PID: {}", child_p.pid);
    }

    uv_unref((uv_handle_t*)&child_p);
    uv_run(loop, UV_RUN_DEFAULT);
    uv_loop_close(loop);
}

tt_SimulationDevice::~tt_SimulationDevice() { close_device(); }

void tt_SimulationDevice::start_device() {
    void* buf_ptr = nullptr;

    host.start_host();

    log_info(tt::LogEmulationDriver, "Waiting for ack msg from remote...");
    size_t buf_size = host.recv_from_device(&buf_ptr);
    auto buf = GetDeviceRequestResponse(buf_ptr);
    auto cmd = buf->command();
    TT_ASSERT(cmd == DEVICE_COMMAND_EXIT, "Did not receive expected command from remote.");
    nng_free(buf_ptr, buf_size);
}

void tt_SimulationDevice::send_tensix_risc_reset(tt_xy_pair core, const TensixSoftResetOptions& soft_resets) {
    if (soft_resets == TENSIX_ASSERT_SOFT_RESET) {
        log_info(tt::LogEmulationDriver, "Sending assert_risc_reset signal..");
        auto wr_buffer =
            create_flatbuffer(DEVICE_COMMAND_ALL_TENSIX_RESET_ASSERT, std::vector<uint32_t>(1, 0), core, 0);
        uint8_t* wr_buffer_ptr = wr_buffer.GetBufferPointer();
        size_t wr_buffer_size = wr_buffer.GetSize();

        print_flatbuffer(GetDeviceRequestResponse(wr_buffer_ptr));
        host.send_to_device(wr_buffer_ptr, wr_buffer_size);
    } else if (soft_resets == TENSIX_DEASSERT_SOFT_RESET) {
        log_info(tt::LogEmulationDriver, "Sending 'deassert_risc_reset' signal..");
        auto wr_buffer =
            create_flatbuffer(DEVICE_COMMAND_ALL_TENSIX_RESET_DEASSERT, std::vector<uint32_t>(1, 0), core, 0);
        uint8_t* wr_buffer_ptr = wr_buffer.GetBufferPointer();
        size_t wr_buffer_size = wr_buffer.GetSize();

        host.send_to_device(wr_buffer_ptr, wr_buffer_size);
    } else {
        TT_THROW("Invalid soft reset option.");
    }
}

void tt_SimulationDevice::send_tensix_risc_reset(const TensixSoftResetOptions& soft_resets) {
    send_tensix_risc_reset({0, 0}, soft_resets);
}

void tt_SimulationDevice::close_device() {
    // disconnect from remote connection
    log_info(tt::LogEmulationDriver, "Sending exit signal to remote...");
    auto builder = create_flatbuffer(DEVICE_COMMAND_EXIT, std::vector<uint32_t>(1, 0), {0, 0}, 0);
    host.send_to_device(builder.GetBufferPointer(), builder.GetSize());
}

void tt_SimulationDevice::set_remote_transfer_ethernet_cores(const std::unordered_set<tt::umd::CoreCoord>& cores) {}

// Runtime Functions
void tt_SimulationDevice::write_to_device(tt_xy_pair core, const void* src, uint64_t l1_dest, uint32_t size) {
    log_info(
        tt::LogEmulationDriver,
        "Device writing {} bytes to l1_dest {} in core ({}, {})",
        size,
        l1_dest,
        core.x,
        core.y);
    std::vector<std::uint32_t> data((uint32_t*)src, (uint32_t*)src + size / sizeof(uint32_t));
    auto wr_buffer = create_flatbuffer(DEVICE_COMMAND_WRITE, data, core, l1_dest);
    uint8_t* wr_buffer_ptr = wr_buffer.GetBufferPointer();
    size_t wr_buffer_size = wr_buffer.GetSize();

    print_flatbuffer(GetDeviceRequestResponse(wr_buffer_ptr));  // sanity print
    host.send_to_device(wr_buffer_ptr, wr_buffer_size);
}

void tt_SimulationDevice::read_from_device(tt_xy_pair core, void* dest, uint64_t l1_src, uint32_t size) {
    void* rd_resp;

    // Send read request
    auto rd_req_buf = create_flatbuffer(DEVICE_COMMAND_READ, {0}, core, l1_src, size);
    host.send_to_device(rd_req_buf.GetBufferPointer(), rd_req_buf.GetSize());

    // Get read response
    size_t rd_rsp_sz = host.recv_from_device(&rd_resp);

    auto rd_resp_buf = GetDeviceRequestResponse(rd_resp);

    // Debug level polling as Metal will constantly poll the device, spamming the logs
    log_debug(tt::LogEmulationDriver, "Device reading vec");
    print_flatbuffer(rd_resp_buf);

    std::memcpy(dest, rd_resp_buf->data()->data(), rd_resp_buf->data()->size() * sizeof(uint32_t));
    nng_free(rd_resp, rd_rsp_sz);
}

void tt_SimulationDevice::dma_write_to_device(const void* src, size_t size, tt_xy_pair core, uint64_t addr) {
    write_to_device(core, src, addr, size);
}

void tt_SimulationDevice::dma_read_from_device(void* dst, size_t size, tt_xy_pair core, uint64_t addr) {
    read_from_device(core, dst, addr, size);
}

void tt_SimulationDevice::wait_for_non_mmio_flush() {}

void tt_SimulationDevice::l1_membar(const std::unordered_set<tt::umd::CoreCoord>& cores) {}

void tt_SimulationDevice::dram_membar(const std::unordered_set<uint32_t>& channels) {}

void tt_SimulationDevice::dram_membar(const std::unordered_set<tt::umd::CoreCoord>& cores) {}

void tt_SimulationDevice::deassert_risc_resets() {}

void tt_SimulationDevice::set_power_state(tt_DevicePowerState state) {}

int tt_SimulationDevice::get_clock() { return 0; }

int tt_SimulationDevice::arc_msg(
    uint32_t msg_code,
    bool wait_for_done,
    uint32_t arg0,
    uint32_t arg1,
    uint32_t timeout_ms,
    uint32_t* return_3,
    uint32_t* return_4) {
    *return_3 = 1;
    return 0;
}
