// SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
//
// SPDX-License-Identifier: Apache-2.0

#pragma once

/**
 * @brief UMD logger configuration and utilities.
 *
 * This namespace contains functionality for configuring the logging system
 * used by the UMD (User Mode Driver).
 */
namespace tt::umd::logging {

/**
 * @brief Logging severity levels
 *
 * Defines the different severity levels for logging messages, from most
 * verbose (trace) to most severe (critical), with an option to disable
 * logging completely (off).
 */
enum class level {
    trace,     ///< Most detailed logging level, for tracing program execution
    debug,     ///< Debugging information, useful during development
    info,      ///< General informational messages about program operation
    warn,      ///< Warning messages for potentially harmful situations
    error,     ///< Error messages for serious problems
    critical,  ///< Critical errors that may lead to program termination
    off        ///< Disables all logging
};

/**
 * @brief Sets the global logging level
 *
 * @param lvl The new logging level to set. Messages with severity levels
 *            lower than this level will not be logged.
 */
void set_level(level lvl);

}  // namespace tt::umd::logging
