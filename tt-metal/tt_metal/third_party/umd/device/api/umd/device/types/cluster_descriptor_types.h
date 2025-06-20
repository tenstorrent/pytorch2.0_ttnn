/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <fmt/core.h>

#include <cstdint>
#include <functional>

#include "fmt/core.h"
#include "umd/device/types/harvesting.h"

// Small performant hash combiner taken from boost library.
// Not using boost::hash_combine due to dependency complications.
inline void boost_hash_combine(std::size_t &seed, const int value) {
    seed ^= value + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

using chip_id_t = int;
using ethernet_channel_t = int;

struct eth_coord_t {
    int cluster_id;  // This is the same for connected chips.
    int x;
    int y;
    int rack;
    int shelf;

    // in C++20 this should be defined as:
    // constexpr bool operator==(const eth_coord_t &other) const noexcept = default;
    constexpr bool operator==(const eth_coord_t &other) const noexcept {
        return (
            cluster_id == other.cluster_id and x == other.x and y == other.y and rack == other.rack and
            shelf == other.shelf);
    }
};

enum BoardType : uint32_t {
    E75,
    E150,
    E300,
    N150,
    N300,
    P100,
    P150,
    P300,
    GALAXY,
    UBB,
    UNKNOWN,
};

inline std::string board_type_to_string(const BoardType board_type) {
    switch (board_type) {
        case BoardType::E75:
            return "e75";
        case BoardType::E150:
            return "e150";
        case BoardType::E300:
            return "e300";
        case BoardType::N150:
            return "n150";
        case BoardType::N300:
            return "n300";
        case BoardType::P100:
            return "p100";
        case BoardType::P150:
            return "p150";
        case BoardType::P300:
            return "p300";
        case BoardType::GALAXY:
            return "galaxy";
        case BoardType::UBB:
            return "ubb";
        case BoardType::UNKNOWN:
            return "unknown";
    }

    throw std::runtime_error("Unknown board type passed for conversion to string.");
}

// We have two ways BH chips are connected to the rest of the system, either one of the two PCI cores can be active.
enum BlackholeChipType : uint32_t {
    Type1,
    Type2,
};

inline BlackholeChipType get_blackhole_chip_type(const BoardType board_type, const uint8_t asic_location) {
    if (asic_location != 0) {
        if (board_type != BoardType::P300) {
            throw std::runtime_error("Remote chip is supported only for Blackhole P300 board.");
        }
    }

    switch (board_type) {
        case BoardType::P100:
            return BlackholeChipType::Type1;
        case BoardType::P150:
            return BlackholeChipType::Type2;
        case BoardType::P300:
            switch (asic_location) {
                case 0:
                    return BlackholeChipType::Type2;
                case 1:
                    return BlackholeChipType::Type1;
                default:
                    throw std::runtime_error(
                        "Invalid asic location for Blackhole P300 board: " + std::to_string(asic_location));
            }
        default:
            throw std::runtime_error("Invalid board type for Blackhole architecture.");
    }
}

inline BoardType get_board_type_from_board_id(const uint64_t board_id) {
    uint64_t upi = (board_id >> 36) & 0xFFFFF;

    if (upi == 0x36) {
        return BoardType::P100;
    } else if (upi == 0x43) {
        return BoardType::P100;
    } else if (upi == 0x40 || upi == 0x41 || upi == 0x42) {
        return BoardType::P150;
    } else if (upi == 0x44 || upi == 0x45 || upi == 0x46) {
        return BoardType::P300;
    } else if (upi == 0x14) {
        return BoardType::N300;
    } else if (upi == 0x18) {
        return BoardType::N150;
    } else if (upi == 0xB) {
        return BoardType::GALAXY;
    } else if (upi == 0x35) {
        return BoardType::UBB;
    }

    throw std::runtime_error(fmt::format("No existing board type for board id 0x{:x}", board_id));
}

struct ChipUID {
    uint64_t board_id;
    uint8_t asic_location;

    bool operator<(const ChipUID &other) const {
        return std::tie(board_id, asic_location) < std::tie(other.board_id, other.asic_location);
    }

    bool const operator==(const ChipUID &other) const {
        return board_id == other.board_id && asic_location == other.asic_location;
    }
};

struct ChipInfo {
    tt::umd::HarvestingMasks harvesting_masks;
    BoardType board_type;
    ChipUID chip_uid;
    bool noc_translation_enabled;
};

enum class DramTrainingStatus : uint8_t {
    IN_PROGRESS = 0,
    FAIL = 1,
    SUCCESS = 2,
};

namespace std {
template <>
struct hash<eth_coord_t> {
    std::size_t operator()(eth_coord_t const &c) const {
        std::size_t seed = 0;
        boost_hash_combine(seed, c.cluster_id);
        boost_hash_combine(seed, c.x);
        boost_hash_combine(seed, c.y);
        boost_hash_combine(seed, c.rack);
        boost_hash_combine(seed, c.shelf);
        return seed;
    }
};

}  // namespace std
