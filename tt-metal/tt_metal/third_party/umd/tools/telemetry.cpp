// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include <chrono>
#include <cxxopts.hpp>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <ostream>
#include <sstream>
#include <string>
#include <thread>
#include <tt-logger/tt-logger.hpp>
#include <vector>

#include "common.h"
#include "fmt/core.h"
#include "umd/device/arc_telemetry_reader.h"
#include "umd/device/types/wormhole_telemetry.h"

using namespace tt::umd;

std::string run_default_telemetry(int pci_device, ArcTelemetryReader* telemetry_reader) {
    // Holds information about the max AICLK value and the current one.
    uint32_t aiclk_info = telemetry_reader->read_entry(wormhole::TAG_AICLK);
    uint32_t aiclk_current = aiclk_info & 0xFFFF;
    uint32_t vcore = telemetry_reader->read_entry(wormhole::TAG_VCORE);
    uint32_t tdp = telemetry_reader->read_entry(wormhole::TAG_TDP) & 0xFFFF;
    uint32_t asic_temperature = telemetry_reader->read_entry(wormhole::TAG_ASIC_TEMPERATURE);
    uint32_t current_temperature = (asic_temperature & 0xFFFF) / 16.0;
    return fmt::format(
        "Device id {} - AICLK: {} VCore: {} Power: {} Temp: {}",
        pci_device,
        aiclk_current,
        vcore,
        tdp,
        current_temperature);
}

int main(int argc, char* argv[]) {
    cxxopts::Options options("telemetry", "Poll telemetry values from devices.");

    options.add_options()(
        "d,devices",
        "List of device pci ids to read telemetry for. If empty, will poll on all available devices",
        cxxopts::value<std::vector<std::string>>())(
        "t,tag",
        "Telemetry tag to read. If set to -1, will run default telemetry mode which works only for WH and reads aiclk, "
        "power, temperature and vcore. See device/api/umd/device/types/wormhole_telemetry.h (or blackhole_telemetry.h) "
        "for all available tags.",
        cxxopts::value<int>()->default_value("-1"))(
        "f,freq", "Frequency of polling in microseconds.", cxxopts::value<int>()->default_value("1000"))(
        "o,outfile",
        "Output file to dump telemetry to. If omitted, will print out to stdout.",
        cxxopts::value<std::string>())("h,help", "Print usage");

    auto result = options.parse(argc, argv);

    if (result.count("help")) {
        std::cout << options.help() << std::endl;
        return 0;
    }

    int frequency_us = result["freq"].as<int>();
    int telemetry_tag = result["tag"].as<int>();

    std::vector<int> discovered_pci_device_ids = PCIDevice::enumerate_devices();
    std::vector<int> pci_device_ids;

    if (result.count("devices")) {
        for (int device_id : extract_int_vector(result["devices"])) {
            if (std::find(discovered_pci_device_ids.begin(), discovered_pci_device_ids.end(), device_id) ==
                discovered_pci_device_ids.end()) {
                std::cerr << "Device ID with pci id " << device_id << " not found in the system." << std::endl;
                // Ignore this device id and continue.
            } else {
                pci_device_ids.push_back(device_id);
            }
        }
    } else {
        pci_device_ids = discovered_pci_device_ids;
    }

    std::ofstream output_file;
    if (result.count("outfile")) {
        output_file.open(result["outfile"].as<std::string>());
        if (!output_file.is_open()) {
            std::cerr << "Failed to open output file: " << result["outfile"].as<std::string>() << std::endl;
        }
    }

    std::vector<std::pair<int, std::unique_ptr<ArcTelemetryReader>>> telemetry_readers;
    std::vector<std::unique_ptr<TTDevice>> tt_devices;
    for (int pci_device_id : pci_device_ids) {
        std::unique_ptr<TTDevice> tt_device = TTDevice::create(pci_device_id);
        std::unique_ptr<ArcTelemetryReader> arc_telemetry_reader =
            ArcTelemetryReader::create_arc_telemetry_reader(tt_device.get());
        tt_devices.push_back(std::move(tt_device));
        telemetry_readers.push_back(std::make_pair(pci_device_id, std::move(arc_telemetry_reader)));
    }

    while (true) {
        auto start_time = std::chrono::steady_clock::now();
        for (int i = 0; i < telemetry_readers.size(); i++) {
            int device_id = telemetry_readers.at(i).first;
            auto& telemetry_reader = telemetry_readers.at(i).second;

            std::string telemetry_message;
            if (telemetry_tag == -1) {
                telemetry_message = run_default_telemetry(device_id, telemetry_reader.get());
            } else {
                uint32_t telemetry_value = telemetry_reader->read_entry(telemetry_tag);
                telemetry_message = fmt::format("Device id {} - Telemetry value: 0x{:x}", device_id, telemetry_value);
            }
            if (output_file.is_open()) {
                auto timestamp = std::chrono::system_clock::now();
                auto time = std::chrono::system_clock::to_time_t(timestamp);
                auto fractional_seconds =
                    std::chrono::duration_cast<std::chrono::microseconds>(timestamp.time_since_epoch()) % 1000000;

                std::stringstream ss;
                ss << std::put_time(std::localtime(&time), "%F %T") << "." << std::setfill('0') << std::setw(6)
                   << fractional_seconds.count() << " - " << telemetry_message;
                output_file << ss.str() << std::endl;
            } else {
                log_info(tt::LogSiliconDriver, "{}", telemetry_message);
            }
        }

        auto end_time = std::chrono::steady_clock::now();
        auto time_passed = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
        uint64_t time_to_wait = frequency_us - time_passed;
        if (time_to_wait > 0) {
            std::this_thread::sleep_for(std::chrono::microseconds(time_to_wait));
        }
    }

    return 0;
}
