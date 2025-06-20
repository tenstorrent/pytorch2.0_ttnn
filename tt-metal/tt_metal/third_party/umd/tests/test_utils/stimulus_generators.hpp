/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once
#include <cassert>
#include <functional>
#include <iostream>
#include <map>
#include <random>
#include <variant>
#include <vector>

#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_xy_pair.h"

/* Sizes:
 * Distribution (including min/max)
 * Rules/Constraints:
 * - Divisible by 4
 */

/* Addresses:
 * Distribution (including min/max)
 * Rules/Constraints:
 * - Divisible by 16
 */

/* Destinations:
 * - Tuple of (int, int, int):
 *   - first entry is chip ID and must be one of a provided list of values
 *   - second and third entries are y and x, respectively, and must be chosen
 *     as a pair from a provided list of pairs
 */

namespace tt::umd::test::utils {

static const std::string SOC_DESC_PATH = "tests/soc_descs/wormhole_b0_8x10.yaml";

enum RemoteTransferType : uint8_t { WRITE = 0, READ };

template <
    typename SAMPLE_T,
    typename UNCONSTRAINED_SAMPLE_T,
    template <typename>
    class DISTRIBUTION_T,
    typename GENERATOR_T = std::mt19937>
class ConstrainedTemplateTemplateGenerator {
public:
    ConstrainedTemplateTemplateGenerator(
        int seed,
        DISTRIBUTION_T<UNCONSTRAINED_SAMPLE_T> const& distribution,
        std::function<SAMPLE_T(UNCONSTRAINED_SAMPLE_T)> constrain) :
        generator(seed), distribution(distribution), constrain(constrain) {}

    SAMPLE_T generate() {
        auto sample = distribution(generator);
        return constrain(sample);
    }

private:
    GENERATOR_T generator;
    DISTRIBUTION_T<UNCONSTRAINED_SAMPLE_T> distribution;
    std::function<SAMPLE_T(UNCONSTRAINED_SAMPLE_T)> constrain;
};

template <typename SAMPLE_T, typename UNCONSTRAINED_SAMPLE_T, class DISTRIBUTION_T, typename GENERATOR_T = std::mt19937>
class ConstrainedTemplateGenerator {
public:
    ConstrainedTemplateGenerator(
        int seed, DISTRIBUTION_T const& distribution, std::function<SAMPLE_T(UNCONSTRAINED_SAMPLE_T)> constrain) :
        generator(seed), distribution(distribution), constrain(constrain) {}

    SAMPLE_T generate() {
        auto sample = distribution(generator);
        return constrain(sample);
    }

private:
    GENERATOR_T generator;
    DISTRIBUTION_T distribution;
    std::function<SAMPLE_T(UNCONSTRAINED_SAMPLE_T)> constrain;
};

using DefaultTransferTypeGenerator =
    ConstrainedTemplateTemplateGenerator<RemoteTransferType, int, std::discrete_distribution>;

using address_t = uint32_t;
using destination_t = std::pair<chip_id_t, CoreCoord>;
using transfer_size_t = uint32_t;

struct write_transfer_sample_t {
    destination_t destination;
    address_t address;
    transfer_size_t size_in_bytes;
    // (payload.data(), size, destination, address, false, false);
};

struct read_transfer_sample_t {
    destination_t destination;
    address_t address;
    transfer_size_t size_in_bytes;
    // (payload.data(), destination, address, size);
};

using remote_transfer_sample_t =
    std::tuple<RemoteTransferType, std::variant<write_transfer_sample_t, read_transfer_sample_t>>;

template <
    template <typename>
    class DEST_DISTR_T,
    template <typename>
    class ADDR_DISTR_T,
    class DISTR_OUT_T,
    template <typename>
    class SIZE_DISTR_T,

    typename GENERATOR_T = std::mt19937>
struct WriteCommandGenerator {
    using destination_generator_t = ConstrainedTemplateTemplateGenerator<destination_t, int, DEST_DISTR_T, GENERATOR_T>;
    using address_generator_t = ConstrainedTemplateTemplateGenerator<address_t, address_t, ADDR_DISTR_T, GENERATOR_T>;
    using size_generator_t =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, DISTR_OUT_T, SIZE_DISTR_T, GENERATOR_T>;

    WriteCommandGenerator(
        destination_generator_t const& destination_generator,
        address_generator_t const& address_generator,
        size_generator_t const& size_generator) :
        destination_generator(destination_generator),
        address_generator(address_generator),
        size_generator(size_generator) {}

    destination_generator_t destination_generator;
    address_generator_t address_generator;
    size_generator_t size_generator;
};

template <
    template <typename>
    class DEST_DISTR_T,
    template <typename>
    class ADDR_DISTR_T,
    template <typename>
    class SIZE_DISTR_T,
    class LAST_CMD_DISTR_T,
    class ORDERED_DISTR_T,

    typename GENERATOR_T = std::mt19937>
struct WriteEpochCmdCommandGenerator {
    using destination_generator_t = ConstrainedTemplateTemplateGenerator<destination_t, int, DEST_DISTR_T, GENERATOR_T>;
    using address_generator_t = ConstrainedTemplateTemplateGenerator<address_t, address_t, ADDR_DISTR_T, GENERATOR_T>;
    using size_generator_t =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, SIZE_DISTR_T, GENERATOR_T>;
    using last_cmd_generator_t = ConstrainedTemplateGenerator<bool, bool, LAST_CMD_DISTR_T, GENERATOR_T>;
    using ordered_generator_t = ConstrainedTemplateGenerator<bool, bool, ORDERED_DISTR_T, GENERATOR_T>;

    WriteEpochCmdCommandGenerator(
        destination_generator_t const& destination_generator,
        address_generator_t const& address_generator,
        size_generator_t const& size_generator,
        last_cmd_generator_t const& last_cmd_generator,
        ordered_generator_t const& ordered_generator) :
        destination_generator(destination_generator),
        address_generator(address_generator),
        size_generator(size_generator),
        last_cmd_generator(last_cmd_generator),
        ordered_generator(ordered_generator) {}

    destination_generator_t destination_generator;
    address_generator_t address_generator;
    size_generator_t size_generator;
    last_cmd_generator_t last_cmd_generator;
    ordered_generator_t ordered_generator;
};

template <
    template <typename>
    class DEST_DISTR_T,
    template <typename>
    class SIZE_DISTR_OUT_T,
    class DISTR_SIZE_OUT_T,
    template <typename>
    class SIZE_DISTR_T,
    template <typename>
    class UNROLL_COUNT_DISTR_T,

    typename GENERATOR_T = std::mt19937>
struct RolledWriteCommandGenerator {
    using destination_generator_t = ConstrainedTemplateTemplateGenerator<destination_t, int, DEST_DISTR_T, GENERATOR_T>;
    using address_generator_t =
        ConstrainedTemplateTemplateGenerator<address_t, address_t, SIZE_DISTR_OUT_T, GENERATOR_T>;
    using size_generator_t =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, DISTR_SIZE_OUT_T, SIZE_DISTR_T, GENERATOR_T>;
    using unroll_count_generator_t = ConstrainedTemplateTemplateGenerator<int, int, UNROLL_COUNT_DISTR_T, GENERATOR_T>;

    RolledWriteCommandGenerator(
        destination_generator_t const& destination_generator,
        address_generator_t const& address_generator,
        size_generator_t const& size_generator,
        unroll_count_generator_t const& unroll_generator) :
        destination_generator(destination_generator),
        address_generator(address_generator),
        size_generator(size_generator),
        unroll_generator(unroll_generator) {}

    destination_generator_t destination_generator;
    address_generator_t address_generator;
    size_generator_t size_generator;
    unroll_count_generator_t unroll_generator;
};

template <
    template <typename>
    class DEST_DISTR_T,
    template <typename>
    class ADDR_DISTR_T,
    class DISTR_OUT_T,
    template <typename>
    class SIZE_DISTR_T,

    typename GENERATOR_T = std::mt19937>
struct ReadCommandGenerator {
    using destination_generator_t = ConstrainedTemplateTemplateGenerator<destination_t, int, DEST_DISTR_T, GENERATOR_T>;
    using address_generator_t = ConstrainedTemplateTemplateGenerator<address_t, address_t, ADDR_DISTR_T, GENERATOR_T>;
    using size_generator_t =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, DISTR_OUT_T, SIZE_DISTR_T, GENERATOR_T>;

    ReadCommandGenerator(
        destination_generator_t const& destination_generator,
        address_generator_t const& address_generator,
        size_generator_t const& size_generator) :
        destination_generator(destination_generator),
        address_generator(address_generator),
        size_generator(size_generator) {}

    destination_generator_t destination_generator;
    address_generator_t address_generator;
    size_generator_t size_generator;
};

template <
    template <typename>
    class WRITE_DEST_DISTR_T,
    template <typename>
    class WRITE_ADDR_DISTR_T,
    class WRITE_SIZE_DISTR_OUT_T,
    template <typename>
    class WRITE_SIZE_DISTR_T,

    template <typename>
    class READ_DEST_DISTR_T,
    template <typename>
    class READ_ADDR_DISTR_T,
    class READ_SIZE_DISTR_OUT_T,
    template <typename>
    class READ_SIZE_DISTR_T,

    typename GENERATOR_T = std::mt19937>
class TestGenerator {
    // ConstrainedTemplateTemplateGenerator<RemoteTransferType, int, TRANS_TYPE_DISTRIBUTION_T, GENERATOR_T>;
    using transfer_type_generator_t = DefaultTransferTypeGenerator;
    using write_command_generator_t =
        WriteCommandGenerator<WRITE_DEST_DISTR_T, WRITE_ADDR_DISTR_T, WRITE_SIZE_DISTR_OUT_T, WRITE_SIZE_DISTR_T>;
    using read_command_generator_t =
        ReadCommandGenerator<READ_DEST_DISTR_T, READ_ADDR_DISTR_T, READ_SIZE_DISTR_OUT_T, READ_SIZE_DISTR_T>;

public:
    TestGenerator(
        int seed,
        transfer_type_generator_t const& transfer_type_distribution,
        write_command_generator_t const& write_command_generator,
        read_command_generator_t const& read_command_generator) :
        generator(seed),
        transfer_type_distribution(transfer_type_distribution),
        write_command_generator(write_command_generator),
        read_command_generator(read_command_generator) {}

    // Generate a sample (transfer type, size, chip, destination, address) based on custom distributions
    remote_transfer_sample_t generate_sample() {
        // Randomly select a transfer type
        RemoteTransferType transfer_type = transfer_type_distribution.generate();
        assert(transfer_type < 4 && transfer_type >= 0);
        switch (transfer_type) {
            case RemoteTransferType::WRITE: {
                destination_t const& destination = write_command_generator.destination_generator.generate();
                address_t const& address = write_command_generator.address_generator.generate();
                transfer_size_t const& size_in_bytes = write_command_generator.size_generator.generate();
                return {
                    transfer_type,
                    write_transfer_sample_t{
                        .destination = destination, .address = address, .size_in_bytes = size_in_bytes}};
            } break;

            case RemoteTransferType::READ: {
                destination_t const& destination = read_command_generator.destination_generator.generate();
                address_t const& address = read_command_generator.address_generator.generate();
                transfer_size_t const& size_in_bytes = read_command_generator.size_generator.generate();
                return {
                    transfer_type,
                    read_transfer_sample_t{
                        .destination = destination, .address = address, .size_in_bytes = size_in_bytes}};
            } break;

            default:
                throw std::runtime_error("Invalid transfer type");
        };
    }

private:
    std::mt19937 generator;

    transfer_type_generator_t transfer_type_distribution;

    write_command_generator_t write_command_generator;
    read_command_generator_t read_command_generator;
};

struct transfer_type_weights_t {
    double write;
    double read;
};

static auto address_aligner = [](address_t addr) -> address_t {
    addr = (((addr - 1) / 32) + 1) * 32;
    assert(addr % 32 == 0);
    return addr;
};
static auto transfer_size_aligner = [](transfer_size_t size) -> transfer_size_t {
    size = (((size - 1) / 4) + 1) * 4;
    assert(size > 0);
    assert(size % 4 == 0);
    return size;
};
static auto address_aligner_32B = [](transfer_size_t size) -> transfer_size_t {
    size = (((size - 1) / 32) + 1) * 32;
    assert(size > 0);
    return size;
};
static auto size_aligner_32B = [](transfer_size_t size) -> transfer_size_t {
    size = (((size - 1) / 32) + 1) * 32;
    assert(size > 0);
    return size;
};
template <typename T>
static auto passthrough_constrainer = [](T const& t) -> T { return t; };

static inline std::vector<destination_t> generate_core_index_locations(
    tt_ClusterDescriptor const& cluster_desc, tt_SocDescriptor const& soc_desc) {
    std::vector<destination_t> core_index_to_location = {};

    for (chip_id_t chip : cluster_desc.get_all_chips()) {
        for (const CoreCoord dram_core : soc_desc.get_cores(CoreType::DRAM)) {
            core_index_to_location.push_back({chip, dram_core});
        }
    }

    return core_index_to_location;
}

// Add a default test harness that can be invoked with custom distributions only.
static void print_command(remote_transfer_sample_t const& command) {
    RemoteTransferType transfer_type = std::get<0>(command);
    switch (transfer_type) {
        case RemoteTransferType::WRITE: {
            write_transfer_sample_t const& command_args = std::get<write_transfer_sample_t>(std::get<1>(command));
            std::cout << "Transfer type: WRITE, chip: (c=" << command_args.destination.first
                      << ", core: " << command_args.destination.second.str() << ", address: " << command_args.address
                      << ", size_in_bytes: " << command_args.size_in_bytes << std::endl;
        } break;
        case RemoteTransferType::READ: {
            read_transfer_sample_t const& command_args = std::get<read_transfer_sample_t>(std::get<1>(command));
            std::cout << "Transfer type: READ, chip: (c=" << command_args.destination.first
                      << ", core: " << command_args.destination.second.str() << ", address: " << command_args.address
                      << ", size_in_bytes: " << command_args.size_in_bytes << std::endl;
        } break;
        default:
            throw std::runtime_error("Invalid transfer type");
    };
}

template <typename T>
int bytes_to_words(int num_bytes) {
    return ((num_bytes - 1) / sizeof(T)) + 1;
}

static inline void dispatch_remote_transfer_command(
    Cluster& driver, remote_transfer_sample_t const& command, std::vector<uint32_t>& payload) {
    RemoteTransferType transfer_type = std::get<0>(command);
    auto resize_payload = [](std::vector<uint32_t>& payload, int size_in_bytes) {
        payload.resize(bytes_to_words<uint32_t>(size_in_bytes));
    };

    switch (std::get<0>(command)) {
        case RemoteTransferType::WRITE: {
            write_transfer_sample_t const& command_args = std::get<write_transfer_sample_t>(std::get<1>(command));
            assert(command_args.size_in_bytes >= sizeof(uint32_t));
            resize_payload(payload, command_args.size_in_bytes);
            driver.write_to_device(
                payload.data(),
                bytes_to_words<uint32_t>(command_args.size_in_bytes),
                command_args.destination.first,
                command_args.destination.second,
                command_args.address);
        } break;
        case RemoteTransferType::READ: {
            read_transfer_sample_t const& command_args = std::get<read_transfer_sample_t>(std::get<1>(command));
            assert(command_args.size_in_bytes >= sizeof(uint32_t));
            resize_payload(payload, command_args.size_in_bytes);
            driver.read_from_device(
                payload.data(),
                command_args.destination.first,
                command_args.destination.second,
                command_args.address,
                command_args.size_in_bytes);
        } break;
        default:
            throw std::runtime_error("Invalid transfer type");
    };
}

static void print_command_executable_code(remote_transfer_sample_t const& command) {
    auto emit_payload_resize_string = [](int size_bytes, int size_word) {
        std::cout << "payload.resize(((" << size_bytes << " - 1) / " << size_word << ") + 1);" << std::endl;
    };
    auto emit_bytes_to_words_len_string = [](std::string const& var_name, int size_in_bytes, int size_word) {
        std::cout << "int " << var_name << " = (((" << size_in_bytes << " - 1) / " << size_word << ") + 1);"
                  << std::endl;
    };

    std::cout << "{" << std::endl;
    switch (std::get<0>(command)) {
        case RemoteTransferType::WRITE: {
            write_transfer_sample_t const& command_args = std::get<write_transfer_sample_t>(std::get<1>(command));
            assert(command_args.size_in_bytes >= sizeof(uint32_t));
            std::cout << "chip = " << command_args.destination.first
                      << ", core = " << command_args.destination.second.str() << std::endl;
            std::cout << "assert(" << command_args.size_in_bytes << " >= sizeof(uint32_t));" << std::endl;
            emit_bytes_to_words_len_string("len", command_args.size_in_bytes, sizeof(uint32_t));
            emit_payload_resize_string(command_args.size_in_bytes, sizeof(uint32_t));
            std::cout << "cluster->write_to_device(payload.data(), len, destination, " << command_args.address << "\");"
                      << std::endl;
            // driver.write_to_device(payload.data(), command_args.size, command_args.destination, command_args.address,
            // false, false);
        } break;
        case RemoteTransferType::READ: {
            read_transfer_sample_t const& command_args = std::get<read_transfer_sample_t>(std::get<1>(command));
            std::cout << "chip = " << command_args.destination.first
                      << ", core = " << command_args.destination.second.str() << std::endl;
            emit_payload_resize_string(command_args.size_in_bytes, sizeof(uint32_t));
            std::cout << "cluster->read_from_device(payload.data(), destination, " << command_args.address << ", "
                      << command_args.size_in_bytes << "\");" << std::endl;
            // driver.read_from_device(payload.data(), command_args.destination, command_args.address,
            // command_args.size);
        } break;
        default:
            throw std::runtime_error("Invalid transfer type");
    };

    std::cout << "}" << std::endl;
    std::cout << std::endl;
}

static void print_command_history_executable_code(std::vector<remote_transfer_sample_t> const& command_history) {
    std::cout << "std::vector<uint32_t> payload;" << std::endl;
    for (remote_transfer_sample_t const& command : command_history) {
        print_command_executable_code(command);
    }
}

template <
    template <typename>
    class WRITE_DEST_DISTR_T,
    template <typename>
    class WRITE_ADDR_DISTR_T,
    class WRITE_SIZE_DISTR_OUT_T,
    template <typename>
    class WRITE_SIZE_DISTR_T,

    template <typename>
    class READ_DEST_DISTR_T,
    template <typename>
    class READ_ADDR_DISTR_T,
    class READ_SIZE_DISTR_OUT_T,
    template <typename>
    class READ_SIZE_DISTR_T>
void RunMixedTransfers(
    Cluster& cluster,
    int num_samples,
    int seed,

    transfer_type_weights_t const& transfer_type_weights,

    WriteCommandGenerator<WRITE_DEST_DISTR_T, WRITE_ADDR_DISTR_T, WRITE_SIZE_DISTR_OUT_T, WRITE_SIZE_DISTR_T> const&
        write_command_generator,
    ReadCommandGenerator<READ_DEST_DISTR_T, READ_ADDR_DISTR_T, READ_SIZE_DISTR_OUT_T, READ_SIZE_DISTR_T> const&
        read_command_generator,

    bool record_command_history = false,
    std::vector<remote_transfer_sample_t>* command_history = nullptr) {
    SCOPED_TRACE("RunMixedTransfers");
    auto test_generator = TestGenerator(
        seed,
        {seed,
         {transfer_type_weights.write, transfer_type_weights.read},
         [](int transfer_type) -> RemoteTransferType {
             assert(transfer_type < 4);
             return static_cast<RemoteTransferType>(transfer_type);
         }},
        write_command_generator,
        read_command_generator);

    if (record_command_history) {
        assert(command_history != nullptr);
        assert(command_history->size() == 0);  // only support passing in empty command histories
        command_history->reserve(num_samples);
    }
    std::vector<uint32_t> payload = {};
    for (int i = 0; i < num_samples; i++) {
        auto const& sample = test_generator.generate_sample();
        if (record_command_history) {
            command_history->push_back(sample);
        }

        RemoteTransferType transfer_type = std::get<0>(sample);
        if (record_command_history) {
            print_command_executable_code(sample);
        } else {
            // print_command(sample);
        }
        if (i != 0 && num_samples > 100 && i % (num_samples / 100) == 0) {
            // std::cout << "Completed " << i / (num_samples / 100) << "% of samples" << std::endl;
        }
        dispatch_remote_transfer_command(cluster, sample, payload);
    }
}

static ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>
get_default_address_generator(int seed, address_t start, address_t end) {
    auto const& address_distribution = std::uniform_int_distribution<address_t>(start, end);
    return ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>(
        seed + 1, address_distribution, address_aligner);
}

static ConstrainedTemplateTemplateGenerator<destination_t, int, std::uniform_int_distribution>
get_default_full_dram_dest_generator(int seed, Cluster* cluster) {
    assert(cluster != nullptr);
    tt_ClusterDescriptor* cluster_desc = cluster->get_cluster_description();
    tt_SocDescriptor const& soc_desc = cluster->get_soc_descriptor(0);
    std::vector<destination_t> core_index_to_location = generate_core_index_locations(*cluster_desc, soc_desc);

    return ConstrainedTemplateTemplateGenerator<destination_t, int, std::uniform_int_distribution>(
        seed,
        std::uniform_int_distribution<int>(0, core_index_to_location.size() - 1),
        [core_index_to_location](int dest) -> destination_t { return core_index_to_location.at(dest); });
}

static WriteCommandGenerator<
    std::uniform_int_distribution,
    std::uniform_int_distribution,
    transfer_size_t,
    std::uniform_int_distribution>
build_dummy_write_command_generator(Cluster& cluster) {
    tt_ClusterDescriptor* cluster_desc = cluster.get_cluster_description();
    tt_SocDescriptor const& soc_desc = cluster.get_soc_descriptor(0);
    std::vector<destination_t> core_index_to_location = generate_core_index_locations(*cluster_desc, soc_desc);
    auto dest_generator = ConstrainedTemplateTemplateGenerator<destination_t, int, std::uniform_int_distribution>(
        0,
        std::uniform_int_distribution<int>(0, core_index_to_location.size() - 1),
        [core_index_to_location](int dest) -> destination_t { return core_index_to_location.at(dest); });
    auto addr_generator = ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>(
        0, std::uniform_int_distribution<address_t>(0, 0), address_aligner);
    auto addr_generator_32B_aligned =
        ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>(
            0, std::uniform_int_distribution<address_t>(0, 0), address_aligner_32B);
    auto write_size_generator =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, std::uniform_int_distribution>(
            0, std::uniform_int_distribution<address_t>(0, 0), transfer_size_aligner);

    return WriteCommandGenerator(dest_generator, addr_generator, write_size_generator);
}

static ReadCommandGenerator<
    std::uniform_int_distribution,
    std::uniform_int_distribution,
    transfer_size_t,
    std::uniform_int_distribution>
build_dummy_read_command_generator(Cluster& cluster) {
    tt_ClusterDescriptor* cluster_desc = cluster.get_cluster_description();
    tt_SocDescriptor const& soc_desc = cluster.get_soc_descriptor(0);
    std::vector<destination_t> core_index_to_location = generate_core_index_locations(*cluster_desc, soc_desc);
    auto dest_generator = ConstrainedTemplateTemplateGenerator<destination_t, int, std::uniform_int_distribution>(
        0,
        std::uniform_int_distribution<int>(0, core_index_to_location.size() - 1),
        [core_index_to_location](int dest) -> destination_t { return core_index_to_location.at(dest); });
    auto addr_generator = ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>(
        0, std::uniform_int_distribution<address_t>(0, 0), address_aligner);
    auto read_size_generator =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, std::uniform_int_distribution>(
            0, std::uniform_int_distribution<transfer_size_t>(0, 0), transfer_size_aligner);

    return ReadCommandGenerator(dest_generator, addr_generator, read_size_generator);
}

template <
    template <typename>
    class ADDR_GENERATOR_T,
    typename ADDR_DISTR_T,
    template <typename>
    class WRITE_SIZE_GENERATOR_T,
    template <typename>
    class READ_SIZE_GENERATOR_T,
    template <typename>
    class UNROLL_COUNT_GENERATOR_T>
void RunMixedTransfersUniformDistributions(
    Cluster& cluster,
    int num_samples,
    int seed,

    transfer_type_weights_t const& transfer_type_weights,
    ADDR_GENERATOR_T<ADDR_DISTR_T> const& address_distribution,
    WRITE_SIZE_GENERATOR_T<transfer_size_t> const& write_size_distribution,
    UNROLL_COUNT_GENERATOR_T<int> const& unroll_count_distribution,
    float percent_not_last_epoch_cmd,
    float percent_not_remote_ordered,
    READ_SIZE_GENERATOR_T<transfer_size_t> const& read_size_distribution,

    bool record_command_history = false,
    std::vector<remote_transfer_sample_t>* command_history = nullptr) {
    tt_ClusterDescriptor* cluster_desc = cluster.get_cluster_description();
    tt_SocDescriptor const& soc_desc = cluster.get_soc_descriptor(0);
    std::vector<destination_t> core_index_to_location = generate_core_index_locations(*cluster_desc, soc_desc);

    auto dest_generator = ConstrainedTemplateTemplateGenerator<destination_t, int, std::uniform_int_distribution>(
        seed,
        std::uniform_int_distribution<int>(0, core_index_to_location.size() - 1),
        [&core_index_to_location](int dest) -> destination_t { return core_index_to_location.at(dest); });
    auto addr_generator = ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>(
        seed + 1, address_distribution, address_aligner);
    auto addr_generator_32B_aligned =
        ConstrainedTemplateTemplateGenerator<address_t, address_t, std::uniform_int_distribution>(
            seed + 1, address_distribution, address_aligner_32B);
    auto write_size_generator =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, std::uniform_int_distribution>(
            seed + 2, write_size_distribution, transfer_size_aligner);
    auto read_size_generator =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, std::uniform_int_distribution>(
            seed + 2, read_size_distribution, transfer_size_aligner);
    auto last_epoch_cmd_generator = ConstrainedTemplateGenerator<bool, bool, std::bernoulli_distribution>(
        seed + 3, std::bernoulli_distribution(percent_not_last_epoch_cmd), [](bool last_epoch_cmd) -> bool {
            return last_epoch_cmd;
        });
    auto ordered_generator = ConstrainedTemplateGenerator<bool, bool, std::bernoulli_distribution>(
        seed + 3,
        std::bernoulli_distribution(percent_not_remote_ordered),
        [](bool ordered_with_prev_remote_write) -> bool { return ordered_with_prev_remote_write; });
    auto unroll_count_generator = ConstrainedTemplateTemplateGenerator<int, int, std::uniform_int_distribution>(
        seed + 4, unroll_count_distribution, [](int unroll_count) -> int { return unroll_count; });

    RunMixedTransfers(
        cluster,
        num_samples,
        seed,

        transfer_type_weights,

        WriteCommandGenerator(dest_generator, addr_generator, write_size_generator),
        ReadCommandGenerator(dest_generator, addr_generator, read_size_generator),

        record_command_history,
        command_history);
}

}  // namespace tt::umd::test::utils
