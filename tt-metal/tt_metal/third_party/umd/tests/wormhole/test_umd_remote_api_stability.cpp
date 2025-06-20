// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include <chrono>
#include <cstdint>
#include <ctime>
#include <numeric>
#include <random>
#include <thread>
#include <tt-logger/tt-logger.hpp>

#include "filesystem"
#include "gtest/gtest.h"
#include "test_wh_common.h"
#include "tests/test_utils/generate_cluster_desc.hpp"
#include "tests/test_utils/stimulus_generators.hpp"
#include "umd/device/cluster.h"
#include "umd/device/tt_cluster_descriptor.h"
#include "umd/device/tt_soc_descriptor.h"
#include "wormhole/eth_interface.h"
#include "wormhole/host_mem_address_map.h"
#include "wormhole/l1_address_map.h"

namespace tt::umd::test::utils {
class WormholeNebulaX2TestFixture : public WormholeTestFixture {
private:
    static int detected_num_chips;
    static bool skip_tests;

protected:
    static constexpr int EXPECTED_NUM_CHIPS = 2;
    static uint32_t scale_number_of_tests;

    static void SetUpTestSuite() {
        std::unique_ptr<tt_ClusterDescriptor> cluster_desc = Cluster::create_cluster_descriptor();
        detected_num_chips = cluster_desc->get_number_of_chips();
        if (detected_num_chips != EXPECTED_NUM_CHIPS) {
            skip_tests = true;
        }
        if (char const* scale_number_of_tests_env = std::getenv("SCALE_NUMBER_OF_TESTS")) {
            scale_number_of_tests = std::atoi(scale_number_of_tests_env);
        }
    }

    virtual int get_detected_num_chips() { return detected_num_chips; }

    virtual bool is_test_skipped() { return skip_tests; }
};

int WormholeNebulaX2TestFixture::detected_num_chips = -1;
bool WormholeNebulaX2TestFixture::skip_tests = false;
uint32_t WormholeNebulaX2TestFixture::scale_number_of_tests = 1;

TEST_F(WormholeNebulaX2TestFixture, MixedRemoteTransfersMediumSmall) {
    int seed = 0;

    log_info(LogSiliconDriver, "Started MixedRemoteTransfersMediumSmall");

    std::vector<remote_transfer_sample_t> command_history;
    try {
        assert(cluster != nullptr);
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 0.25, .read = 0.25},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history);
    } catch (...) {
        print_command_history_executable_code(command_history);
    }
}

TEST_F(WormholeNebulaX2TestFixture, MultithreadedMixedRemoteTransfersMediumSmall) {
    int seed = 0;

    log_info(LogSiliconDriver, "Started MultithreadedMixedRemoteTransfersMediumSmall");

    assert(cluster != nullptr);
    std::vector<remote_transfer_sample_t> command_history0;
    std::vector<remote_transfer_sample_t> command_history1;
    std::vector<remote_transfer_sample_t> command_history2;
    std::vector<remote_transfer_sample_t> command_history3;
    std::thread t1([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 0.50, .read = 0.50},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history0);
    });
    std::thread t2([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            100,
            transfer_type_weights_t{.write = 0.25, .read = 0.50},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history1);
    });
    std::thread t3([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            23,
            transfer_type_weights_t{.write = 0.5, .read = 0.25},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history2);
    });
    std::thread t4([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            99,
            transfer_type_weights_t{.write = 1.0, .read = 0.0},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history3);
    });

    t1.join();
    t2.join();
    t3.join();
    t4.join();
}

TEST_F(WormholeNebulaX2TestFixture, MixedRemoteTransfersLarge) {
    int seed = 0;

    log_info(LogSiliconDriver, "Started MixedRemoteTransfersLarge");

    assert(cluster != nullptr);
    std::vector<remote_transfer_sample_t> command_history;
    try {
        RunMixedTransfersUniformDistributions(
            *cluster,
            10000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 0.15, .read = 0.15},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x10000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 300000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            // Set to true if you want to emit the command history code to command line
            std::uniform_int_distribution<transfer_size_t>(0x4, 300000),
            false,
            &command_history);
    } catch (...) {
        print_command_history_executable_code(command_history);
    }
}

TEST_F(WormholeNebulaX2TestFixture, WritesOnlyNormalDistributionMean10kStd3kMinSizeTruncate4) {
    int seed = 0;

    log_info(LogSiliconDriver, "Started WritesOnlyNormalDistributionMean10kStd3kMinSizeTruncate4");

    assert(cluster != nullptr);
    std::vector<remote_transfer_sample_t> command_history;

    auto write_size_generator = ConstrainedTemplateTemplateGenerator<transfer_size_t, double, std::normal_distribution>(
        seed, std::normal_distribution<>(10000, 3000), [](double x) -> transfer_size_t {
            return size_aligner_32B(static_cast<transfer_size_t>((x >= 4) ? x : 4));
        });

    auto dest_generator = get_default_full_dram_dest_generator(seed, cluster.get());
    auto address_generator = get_default_address_generator(seed, 0x100000, 0x5000000);

    try {
        RunMixedTransfers(
            *cluster,
            10000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 1., .read = 0.},
            WriteCommandGenerator(dest_generator, address_generator, write_size_generator),
            build_dummy_read_command_generator(*cluster),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history);
    } catch (...) {
        print_command_history_executable_code(command_history);
    }
}

TEST_F(WormholeNebulaX2TestFixture, MultithreadedMixedRemoteTransfersLMS) {
    int seed = 0;

    log_info(LogSiliconDriver, "Started MultithreadedMixedRemoteTransfersLMS");

    assert(cluster != nullptr);
    std::vector<remote_transfer_sample_t> command_history0;
    std::vector<remote_transfer_sample_t> command_history1;
    std::vector<remote_transfer_sample_t> command_history2;
    std::vector<remote_transfer_sample_t> command_history3;
    std::thread t1([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 0.50, .read = 0.50},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(4, 300000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history0);
    });
    std::thread t2([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            100,
            transfer_type_weights_t{.write = 0.25, .read = 0.50},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history1);
    });
    std::thread t3([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            23,
            transfer_type_weights_t{.write = 0.5, .read = 0.25},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history2);
    });
    std::thread t4([&]() {
        RunMixedTransfersUniformDistributions(
            *cluster,
            100000 * scale_number_of_tests,
            99,
            transfer_type_weights_t{.write = 1.0, .read = 0.0},
            // address generator distribution
            std::uniform_int_distribution<address_t>(0x100000, 0x200000),
            // WRITE_SIZE_GENERATOR_T const& write_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // UNROLL_COUNT_GENERATOR_T const& unroll_count_distribution
            std::uniform_int_distribution<int>(2, 4),
            0.75,
            0.75,
            // READ_SIZE_GENERATOR_T const& read_size_distribution,
            std::uniform_int_distribution<transfer_size_t>(0x4, 3000),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history3);
    });

    t1.join();
    t2.join();
    t3.join();
    t4.join();
}

TEST_F(WormholeNebulaX2TestFixture, MultithreadedMixedRemoteTransfersLargeWritesSmallReads) {
    int seed = 0;

    log_info(LogSiliconDriver, "Started MultithreadedMixedRemoteTransfersLargeWritesSmallReads");

    assert(cluster != nullptr);
    std::vector<remote_transfer_sample_t> command_history0;
    std::vector<remote_transfer_sample_t> command_history1;

    auto write_size_generator =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, std::uniform_int_distribution>(
            seed,
            std::uniform_int_distribution<transfer_size_t>(1000000, 30000000),
            [](transfer_size_t x) -> transfer_size_t {
                return size_aligner_32B(static_cast<transfer_size_t>((x >= 4) ? x : 4));
            });
    auto read_size_generator =
        ConstrainedTemplateTemplateGenerator<transfer_size_t, transfer_size_t, std::uniform_int_distribution>(
            seed, std::uniform_int_distribution<transfer_size_t>(16, 4096), [](transfer_size_t x) -> transfer_size_t {
                return size_aligner_32B(static_cast<transfer_size_t>((x >= 4) ? x : 4));
            });

    auto dest_generator = get_default_full_dram_dest_generator(seed, cluster.get());
    auto address_generator = get_default_address_generator(seed, 0x100000, 0x5000000);

    std::thread write_cmds_thread1([&]() {
        RunMixedTransfers(
            *cluster,
            10000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 1., .read = 0.},
            WriteCommandGenerator(dest_generator, address_generator, write_size_generator),
            build_dummy_read_command_generator(*cluster),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history0);
    });
    std::thread write_cmds_thread2([&]() {
        RunMixedTransfers(
            *cluster,
            10000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 1., .read = 0.},
            WriteCommandGenerator(dest_generator, address_generator, write_size_generator),
            build_dummy_read_command_generator(*cluster),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history0);
    });
    std::thread read_cmd_threads1([&]() {
        RunMixedTransfers(
            *cluster,
            10000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 0, .read = 1.},
            build_dummy_write_command_generator(*cluster),
            ReadCommandGenerator(dest_generator, address_generator, read_size_generator),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history0);
    });
    std::thread read_cmd_threads2([&]() {
        RunMixedTransfers(
            *cluster,
            10000 * scale_number_of_tests,
            0,
            transfer_type_weights_t{.write = 0, .read = 1.},
            build_dummy_write_command_generator(*cluster),
            ReadCommandGenerator(dest_generator, address_generator, read_size_generator),
            // Set to true if you want to emit the command history code to command line
            false,
            &command_history0);
    });

    write_cmds_thread1.join();
    write_cmds_thread2.join();
    read_cmd_threads1.join();
    read_cmd_threads2.join();
}
}  // namespace tt::umd::test::utils
