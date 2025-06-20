/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <cxxabi.h>
#include <execinfo.h>

#include <csignal>
#include <iostream>
#include <sstream>
#include <vector>

namespace tt::assert {

static std::string demangle(const char *str) {
    size_t size = 0;
    int status = 0;
    std::string rt(256, '\0');
    if (1 == sscanf(str, "%*[^(]%*[^_]%255[^)+]", &rt[0])) {
        char *v = abi::__cxa_demangle(&rt[0], nullptr, &size, &status);
        if (v) {
            std::string result(v);
            free(v);
            return result;
        }
    }
    return str;
}

// https://www.fatalerrors.org/a/backtrace-function-and-assert-assertion-macro-encapsulation.html

/**
 * @brief Get the current call stack
 * @param[out] bt Save Call Stack
 * @param[in] size Maximum number of return layers
 * @param[in] skip Skip the number of layers at the top of the stack
 */
inline std::vector<std::string> backtrace(int size = 64, int skip = 1, void *caller_address = nullptr) {
    std::vector<std::string> bt;
    void **array = (void **)malloc((sizeof(void *) * size));
    if (caller_address != nullptr) {
        array[1] = caller_address;
    }
    size_t s = ::backtrace(array, size);
    char **strings = backtrace_symbols(array, s);
    if (strings == NULL) {
        std::cout << "backtrace_symbols error." << std::endl;
        return bt;
    }
    for (size_t i = skip; i < s; ++i) {
        bt.push_back(demangle(strings[i]));
    }
    free(strings);
    free(array);

    return bt;
}

/**
 * @brief String to get current stack information
 * @param[in] size Maximum number of stacks
 * @param[in] skip Skip the number of layers at the top of the stack
 * @param[in] prefix Output before stack information
 */
inline std::string backtrace_to_string(
    int size = 64, int skip = 2, const std::string &prefix = "", void *caller_address = nullptr) {
    std::vector<std::string> bt = backtrace(size, skip, caller_address);
    std::stringstream ss;
    for (size_t i = 0; i < bt.size(); ++i) {
        ss << prefix << bt[i] << std::endl;
    }
    return ss.str();
}

inline void segfault_handler(int sig) {
    std::cerr << backtrace_to_string() << std::endl;
    exit(EXIT_FAILURE);
}

inline void register_segfault_handler() {
    if (std::signal(SIGSEGV, segfault_handler) == SIG_ERR) {
        std::cerr << "Error: cannot handle SIGSEGV" << std::endl;
        exit(EXIT_FAILURE);
    }
}
}  // namespace tt::assert
