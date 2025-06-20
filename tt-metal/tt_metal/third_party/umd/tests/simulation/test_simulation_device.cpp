// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include <random>

#include "device_fixture.hpp"
#include "tests/test_utils/device_test_utils.hpp"

std::vector<uint32_t> generate_data(uint32_t size_in_bytes) {
    size_t size = size_in_bytes / sizeof(uint32_t);
    std::vector<uint32_t> data(size);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<uint32_t> dis(0, 100);

    for (uint32_t i = 0; i < size; i++) {
        data[i] = dis(gen);
    }
    return data;
}

class LoopbackAllCoresParam : public SimulationDeviceFixture, public ::testing::WithParamInterface<tt_xy_pair> {};

INSTANTIATE_TEST_SUITE_P(
    LoopbackAllCores, LoopbackAllCoresParam, ::testing::Values(tt_xy_pair{0, 1}, tt_xy_pair{1, 1}, tt_xy_pair{1, 0}));

TEST_P(LoopbackAllCoresParam, LoopbackSingleTensix) {
    std::vector<uint32_t> wdata = {1, 2, 3, 4, 5};
    std::vector<uint32_t> rdata(wdata.size(), 0);
    auto &soc_desc = device->get_soc_descriptor();
    tt::umd::CoreCoord core = soc_desc.get_coord_at(GetParam(), CoordSystem::VIRTUAL);

    device->write_to_device(core, wdata.data(), 0x100, wdata.size() * sizeof(uint32_t));
    device->read_from_device(core, rdata.data(), 0x100, rdata.size() * sizeof(uint32_t));

    ASSERT_EQ(wdata, rdata);
}

bool loopback_stress_size(std::unique_ptr<tt_SimulationDevice> &device, tt::umd::CoreCoord core, uint32_t byte_shift) {
    uint64_t addr = 0x0;

    std::vector<uint32_t> wdata = generate_data(1 << byte_shift);
    std::vector<uint32_t> rdata(wdata.size(), 0);

    device->write_to_device(core, wdata.data(), addr, wdata.size() * sizeof(uint32_t));
    device->read_from_device(core, rdata.data(), addr, rdata.size() * sizeof(uint32_t));

    return wdata == rdata;
}

TEST_P(LoopbackAllCoresParam, LoopbackStressSize) {
    auto &soc_desc = device->get_soc_descriptor();
    tt::umd::CoreCoord core = soc_desc.get_coord_at(GetParam(), CoordSystem::VIRTUAL);
    tt::umd::CoreCoord dram = soc_desc.get_coord_at({1, 0}, CoordSystem::VIRTUAL);
    if (core == dram) {
        for (uint32_t i = 2; i <= 30; ++i) {  // 2^30 = 1 GB
            ASSERT_TRUE(loopback_stress_size(device, core, i));
        }
    } else {
        for (uint32_t i = 2; i <= 20; ++i) {  // 2^20 = 1 MB
            ASSERT_TRUE(loopback_stress_size(device, core, i));
        }
    }
}

TEST_F(SimulationDeviceFixture, LoopbackTwoTensix) {
    auto &soc_desc = device->get_soc_descriptor();
    std::vector<uint32_t> wdata1 = {1, 2, 3, 4, 5};
    std::vector<uint32_t> wdata2 = {6, 7, 8, 9, 10};
    std::vector<uint32_t> rdata1(wdata1.size());
    std::vector<uint32_t> rdata2(wdata2.size());
    tt::umd::CoreCoord core1 = soc_desc.get_coord_at({0, 1}, CoordSystem::VIRTUAL);
    tt::umd::CoreCoord core2 = soc_desc.get_coord_at({1, 1}, CoordSystem::VIRTUAL);

    device->write_to_device(core1, wdata1.data(), 0x100, wdata1.size() * sizeof(uint32_t));
    device->write_to_device(core2, wdata2.data(), 0x100, wdata2.size() * sizeof(uint32_t));

    device->read_from_device(core1, rdata1.data(), 0x100, rdata1.size() * sizeof(uint32_t));
    device->read_from_device(core2, rdata2.data(), 0x100, rdata2.size() * sizeof(uint32_t));

    ASSERT_EQ(wdata1, rdata1);
    ASSERT_EQ(wdata2, rdata2);
}
