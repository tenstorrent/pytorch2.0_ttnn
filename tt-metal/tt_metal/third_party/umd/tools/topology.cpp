// SPDX-FileCopyrightText: (c) 2025 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0
#include <cxxopts.hpp>
#include <tt-logger/tt-logger.hpp>

#include "common.h"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"

using namespace tt::umd;

int main(int argc, char *argv[]) {
    cxxopts::Options options("topology", "Extract system topology and save it to a yaml file.");

    options.add_options()("f,path", "File path to save cluster descriptor to.", cxxopts::value<std::string>())(
        "l,logical_devices",
        "List of logical device ids to filter cluster descriptor for.",
        cxxopts::value<std::vector<std::string>>())(
        "p,pci_devices",
        "List of pci device ids to perform topology discovery on.",
        cxxopts::value<std::vector<std::string>>())("h,help", "Print usage");

    auto result = options.parse(argc, argv);

    if (result.count("help")) {
        std::cout << options.help() << std::endl;
        return 0;
    }

    if (result.count("logical_devices") && result.count("pci_devices")) {
        std::cerr << "Error: Using both 'pci_devices' and 'logical_devices' options is not allowed." << std::endl;
        return 1;
    }

    std::string cluster_descriptor_path = "";
    if (result.count("path")) {
        cluster_descriptor_path = result["path"].as<std::string>();
    }

    std::unordered_set<int> pci_ids = {};
    if (result.count("pci_devices")) {
        pci_ids = extract_int_set(result["pci_devices"]);
    }

    std::unique_ptr<tt_ClusterDescriptor> cluster_descriptor = tt::umd::Cluster::create_cluster_descriptor("", pci_ids);

    if (result.count("logical_devices")) {
        std::unordered_set<int> logical_device_ids = extract_int_set(result["logical_devices"]);

        cluster_descriptor =
            tt_ClusterDescriptor::create_constrained_cluster_descriptor(cluster_descriptor.get(), logical_device_ids);
    }

    std::string output_path = cluster_descriptor->serialize_to_file(cluster_descriptor_path);
    log_info(tt::LogSiliconDriver, "Cluster descriptor serialized to {}", output_path);
    return 0;
}
