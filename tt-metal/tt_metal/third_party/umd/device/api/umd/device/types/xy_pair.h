/*
 * SPDX-FileCopyrightText: (c) 2023 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <string>

namespace tt::umd {

struct xy_pair {
    constexpr xy_pair() : x{}, y{} {}

    constexpr xy_pair(std::size_t x, std::size_t y) : x(x), y(y) {}

    std::size_t x;
    std::size_t y;

    std::string str() const;
};

constexpr inline bool operator==(const xy_pair &a, const xy_pair &b) { return a.x == b.x && a.y == b.y; }

constexpr inline bool operator!=(const xy_pair &a, const xy_pair &b) { return !(a == b); }

constexpr inline bool operator<(const xy_pair &left, const xy_pair &right) {
    return (left.x < right.x || (left.x == right.x && left.y < right.y));
}

struct cxy_pair : public xy_pair {
    cxy_pair() : xy_pair{}, chip{} {}

    cxy_pair(std::size_t ichip, xy_pair pair) : xy_pair(pair.x, pair.y), chip(ichip) {}

    cxy_pair(std::size_t ichip, std::size_t x, std::size_t y) : xy_pair(x, y), chip(ichip) {}

    std::size_t chip;

    std::string str() const;
};

constexpr inline bool operator==(const cxy_pair &a, const cxy_pair &b) {
    return a.x == b.x && a.y == b.y && a.chip == b.chip;
}

constexpr inline bool operator!=(const cxy_pair &a, const cxy_pair &b) { return !(a == b); }

constexpr inline bool operator<(const cxy_pair &left, const cxy_pair &right) {
    return (
        left.chip < right.chip || (left.chip == right.chip && left.x < right.x) ||
        (left.chip == right.chip && left.x == right.x && left.y < right.y));
}

}  // namespace tt::umd

namespace std {
template <>
struct hash<tt::umd::xy_pair> {
    std::size_t operator()(tt::umd::xy_pair const &o) const {
        std::size_t seed = 0;
        seed = std::hash<std::size_t>()(o.x) ^ std::hash<std::size_t>()(o.y) << 1;
        return seed;
    }
};
}  // namespace std

namespace std {
template <>
struct hash<tt::umd::cxy_pair> {
    std::size_t operator()(tt::umd::cxy_pair const &o) const {
        std::size_t seed = 0;
        seed = std::hash<std::size_t>()(o.chip) ^ (std::hash<std::size_t>()(o.x) << 1) ^
               (std::hash<std::size_t>()(o.y) << 2);
        return seed;
    }
};
}  // namespace std
