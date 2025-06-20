// SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
//
// SPDX-License-Identifier: Apache-2.0

/**
 * @file config.cpp
 * @brief Implementation of UMD (User Mode Driver) logging initialization
 *
 * This file contains the initialization code for the UMD logging system.
 * It creates a static instance of the TT LoggerInitializer with specific
 * environment variable names for UMD logging configuration.
 */

#include "umd/device/logging/config.h"

#include <spdlog/spdlog.h>

#include <tt-logger/tt-logger-initializer.hpp>

namespace tt::umd::logging {

constexpr auto file_env_var = "TT_UMD_LOGGER_FILE";
constexpr auto level_env_var = "TT_UMD_LOGGER_LEVEL";
constexpr auto log_pattern = "[%Y-%m-%d %H:%M:%S.%e] [%l] [%s:%#] %v";

/**
 * @brief Static instance of LoggerInitializer for UMD logging
 *
 * This static instance initializes the logging system with UMD-specific
 * environment variables:
 * - TT_UMD_LOGGER_FILE: Controls the log file path for UMD logging
 * - TT_UMD_LOGGER_LEVEL: Controls the log level for UMD logging
 *
 * The logger will be initialized when this translation unit is loaded,
 * setting up either file-based or console-based logging depending on
 * the environment variable configuration.
 */
static tt::LoggerInitializer loggerInitializer(file_env_var, level_env_var, log_pattern);

/// Map our internal enum to spdlog's level enum.
spdlog::level::level_enum to_spdlog_level(level lvl) {
    switch (lvl) {
        case level::trace:
            return spdlog::level::trace;
        case level::debug:
            return spdlog::level::debug;
        case level::info:
            return spdlog::level::info;
        case level::warn:
            return spdlog::level::warn;
        case level::error:
            return spdlog::level::err;
        case level::critical:
            return spdlog::level::critical;
        case level::off:
            return spdlog::level::off;
    }
    return spdlog::level::info;  // fallback
}

void set_level(level lvl) { spdlog::set_level(to_spdlog_level(lvl)); }

}  // namespace tt::umd::logging
