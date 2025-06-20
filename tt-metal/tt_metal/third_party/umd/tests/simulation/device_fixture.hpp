// SPDX-FileCopyrightText: © 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include <gtest/gtest.h>
#include <nng/nng.h>
#include <nng/protocol/pair1/pair.h>
#include <nng/protocol/pipeline0/pull.h>
#include <nng/protocol/pipeline0/push.h>

#include <stdexcept>

#include "tests/test_utils/generate_cluster_desc.hpp"
#include "umd/device/tt_simulation_device.h"

class SimulationDeviceFixture : public ::testing::Test {
protected:
    static void SetUpTestSuite() {
        // yaml path is dummy and won't change test behavior
        const char* simulator_path = getenv("TT_UMD_SIMULATOR");
        if (simulator_path == nullptr) {
            throw std::runtime_error(
                "You need to define TT_UMD_SIMULATOR that will point to simulator path. eg. build/versim-wormhole-b0");
        }
        device = std::make_unique<tt_SimulationDevice>(simulator_path);
        device->start_device();
    }

    static void TearDownTestSuite() { device->close_device(); }

    static std::unique_ptr<tt_SimulationDevice> device;
};

std::unique_ptr<tt_SimulationDevice> SimulationDeviceFixture::device = nullptr;
