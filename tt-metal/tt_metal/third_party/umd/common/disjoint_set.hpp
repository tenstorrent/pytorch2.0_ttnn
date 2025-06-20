/*
 * SPDX-FileCopyrightText: (c) 2024 Tenstorrent Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#pragma once

#include <unordered_map>
#include <unordered_set>

// A standard disjoint set data structure to track connected components.
template <typename T>
class DisjointSet {
public:
    void add_item(T item) { parent[item] = item; }

    int get_set(T item) {
        while (parent[item] != item) {
            item = parent[item];
        }
        return item;
    }

    void merge(T item1, T item2) {
        T set1 = get_set(item1);
        T set2 = get_set(item2);
        parent[set1] = parent[set2] = std::min(set1, set2);
    }

    bool are_same_set(T item1, T item2) { return get_set(item1) == get_set(item2); }

    int get_num_sets() {
        std::unordered_set<T> sets;
        for (auto [item, _] : parent) {
            sets.insert(get_set(item));
        }
        return sets.size();
    }

private:
    std::unordered_map<T, T> parent;
};
