// SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
//
// SPDX-License-Identifier: Apache-2.0

#include "umd/device/tt_simulation_host.hpp"

#include <nng/nng.h>
#include <nng/protocol/pair1/pair.h>

#include <cassert>
#include <cstdlib>
#include <filesystem>
#include <iomanip>
#include <sstream>
#include <tt-logger/tt-logger.hpp>
#include <typeinfo>

#include "assert.hpp"

tt_SimulationHost::tt_SimulationHost() {
    // Initialize socket and dialer
    host_socket = std::make_unique<nng_socket>();
    host_dialer = std::make_unique<nng_dialer>();

    // Get current date time string
    std::time_t time = std::time(nullptr);
    std::tm local_time = *std::localtime(&time);
    char buffer[100];
    std::strftime(buffer, sizeof(buffer), "%m-%d-%H:%M:%S", &local_time);

    // Get socket name
    const char *nng_socket_name = std::getenv("NNG_SOCKET_NAME") ? std::getenv("NNG_SOCKET_NAME") : "nng_ipc";
    const char *user_name = std::getenv("USER");

    std::ostringstream ss;
    ss << NNG_SOCKET_PREFIX << user_name << "_" << buffer << "_" << nng_socket_name;
    std::string nng_socket_addr_str = ss.str();
    const char *nng_socket_addr = nng_socket_addr_str.c_str();
    setenv("NNG_SOCKET_ADDR", nng_socket_addr, 1);  // pass NNG_SOCKET_ADDR to remote

    // Open socket and create dialer
    log_info(tt::LogEmulationDriver, "Dialing: {}", nng_socket_addr);
    nng_pair1_open(host_socket.get());
    int rv = nng_dialer_create(host_dialer.get(), *host_socket, nng_socket_addr);
    TT_ASSERT(rv == 0, "Failed to create dialer: {} {}", nng_strerror(rv), nng_socket_addr);
}

tt_SimulationHost::~tt_SimulationHost() {
    nng_dialer_close(*host_dialer);
    nng_close(*host_socket);
}

void tt_SimulationHost::start_host() {
    // Establish connection with remote VCS simulator
    int rv;
    do {
        rv = nng_dialer_start(*host_dialer, 0);
        if (rv != 0) {
            log_info(tt::LogEmulationDriver, "Waiting for remote: {}", nng_strerror(rv));
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    } while (rv != 0);
}

void tt_SimulationHost::send_to_device(uint8_t *buf, size_t buf_size) {
    int rv;
    log_debug(tt::LogEmulationDriver, "Sending messsage to remote..");

    void *msg = nng_alloc(buf_size);
    std::memcpy(msg, buf, buf_size);

    rv = nng_send(*host_socket, msg, buf_size, NNG_FLAG_ALLOC);
    log_debug(tt::LogEmulationDriver, "Message sent.");
    if (rv != 0) {
        log_info(tt::LogEmulationDriver, "Failed to send message to remote: {}", nng_strerror(rv));
    }
}

size_t tt_SimulationHost::recv_from_device(void **data_ptr) {
    int rv;
    size_t data_size;
    log_debug(tt::LogEmulationDriver, "Receiving messsage from remote..");
    rv = nng_recv(*host_socket, data_ptr, &data_size, NNG_FLAG_ALLOC);
    log_debug(tt::LogEmulationDriver, "Message received.");
    if (rv != 0) {
        log_info(tt::LogEmulationDriver, "Failed to receive message from remote: {}", nng_strerror(rv));
    }
    return data_size;
}
