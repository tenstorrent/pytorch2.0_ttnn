/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <iostream>
#include <memory>

#include "gtest/gtest.h"

namespace testing {
// Testing flag verbose can be accessed with GTEST_FLAG(verbose), and set with macro GTEST_VERBOSE=1
bool verbose = testing::internal::BoolFromGTestEnv("verbose", false);
}  // namespace testing

// GoogleTest event listener which only prints test suite name, how many tests are run, and failed tests.
class SilentEventListener : public testing::TestEventListener {
public:
    explicit SilentEventListener(testing::TestEventListener* default_event_listener) :
        m_default_event_listener(default_event_listener) {}

    virtual void OnTestProgramStart(const testing::UnitTest& unit_test) override {
        m_default_event_listener->OnTestProgramStart(unit_test);
    }

    virtual void OnTestIterationStart(const testing::UnitTest& unit_test, int iteration) override {
        m_default_event_listener->OnTestIterationStart(unit_test, iteration);
    }

    virtual void OnEnvironmentsSetUpStart(const testing::UnitTest& unit_test) override {}

    virtual void OnEnvironmentsSetUpEnd(const testing::UnitTest& unit_test) override {}

    virtual void OnTestStart(const testing::TestInfo& test_info) override {}

    virtual void OnTestPartResult(const testing::TestPartResult& result) override {}

    virtual void OnTestEnd(const testing::TestInfo& test_info) override {}

    virtual void OnTestSuiteEnd(const testing::TestSuite& test_suite) override {
        m_default_event_listener->OnTestSuiteEnd(test_suite);
    }

#ifndef GTEST_REMOVE_LEGACY_TEST_CASEAPI_
    virtual void OnTestCaseEnd(const testing::TestCase& test_case) {
        m_default_event_listener->OnTestCaseEnd(test_case);
    }
#endif  // GTEST_REMOVE_LEGACY_TEST_CASEAPI_

    virtual void OnEnvironmentsTearDownStart(const testing::UnitTest& unit_test) override {}

    virtual void OnEnvironmentsTearDownEnd(const testing::UnitTest& unit_test) override {}

    virtual void OnTestIterationEnd(const testing::UnitTest& unit_test, int iteration) override {
        m_default_event_listener->OnTestIterationEnd(unit_test, iteration);
    }

    virtual void OnTestProgramEnd(const testing::UnitTest& unit_test) override {
        m_default_event_listener->OnTestProgramEnd(unit_test);
        // Separating test outputs for different projects.
        std::cout << std::endl;
    }

private:
    std::unique_ptr<testing::TestEventListener> m_default_event_listener;
};

void initialize_gtest(int argc, char** argv) {
    // Default gtest initializer
    testing::InitGoogleTest(&argc, argv);
    bool overwrite_env = false;

    // Replacing default event listener with silent event listener.
    if (testing::verbose == false) {
        testing::TestEventListeners& listeners = testing::UnitTest::GetInstance()->listeners();
        listeners.Append(new SilentEventListener(listeners.Release(listeners.default_result_printer())));
        setenv("LOGGER_LEVEL", "Warning", overwrite_env);
    } else {
        setenv("LOGGER_LEVEL", "Debug", overwrite_env);
    }
}
