// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include "gtest/gtest.h"
#include "gtest_initializer.hpp"

int main(int argc, char **argv) {
    initialize_gtest(argc, argv);
    return RUN_ALL_TESTS();
}
