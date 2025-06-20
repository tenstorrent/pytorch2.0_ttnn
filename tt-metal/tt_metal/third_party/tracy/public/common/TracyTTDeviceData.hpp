#ifndef __TRACYTTDEVICEDATA_HPP__
#define __TRACYTTDEVICEDATA_HPP__

namespace tracy
{
    static std::string riscName[] = {"BRISC", "NCRISC", "TRISC_0", "TRISC_1", "TRISC_2", "ERISC"};

    enum TTDeviceEventPhase
    {
        begin,
        end,
        sum
    };

    struct TTDeviceEvent
    {
        static constexpr uint64_t RISC_BIT_COUNT =  3;
        static constexpr uint64_t CORE_X_BIT_COUNT =  4;
        static constexpr uint64_t CORE_Y_BIT_COUNT =  4;
        static constexpr uint64_t CHIP_BIT_COUNT =  8;
        static constexpr uint64_t RUN_NUM_BIT_COUNT =  16;

        static constexpr uint64_t CORE_X_BIT_SHIFT = RISC_BIT_COUNT;
        static constexpr uint64_t CORE_Y_BIT_SHIFT = CORE_X_BIT_SHIFT + CORE_X_BIT_COUNT;
        static constexpr uint64_t CHIP_BIT_SHIFT = CORE_Y_BIT_SHIFT + CORE_Y_BIT_COUNT;
        static constexpr uint64_t RUN_NUM_BIT_SHIFT = CHIP_BIT_SHIFT + CHIP_BIT_COUNT;

        static constexpr uint64_t INVALID_NUM = 1LL << 63;

        static_assert ((RISC_BIT_COUNT +
                    CORE_X_BIT_COUNT +
                    CORE_Y_BIT_COUNT +
                    CHIP_BIT_COUNT +
                    RUN_NUM_BIT_COUNT) <= (sizeof(uint64_t) * 8));

        uint64_t run_num;
        uint64_t chip_id;
        uint64_t core_x;
        uint64_t core_y;
        uint64_t risc;
        uint64_t marker;
        uint64_t timestamp;
        uint64_t line;
        std::string file;
        std::string zone_name;
        TTDeviceEventPhase zone_phase;

        TTDeviceEvent (): 
            run_num(INVALID_NUM),
            chip_id(INVALID_NUM),
            core_x(INVALID_NUM),
            core_y(INVALID_NUM),
            risc(INVALID_NUM),
            marker(INVALID_NUM),
            timestamp(INVALID_NUM),
            line(INVALID_NUM),
            file(""),
            zone_name(""),
            zone_phase(begin)
        {
        }

        TTDeviceEvent (
                uint64_t run_num,
                uint64_t chip_id,
                uint64_t core_x,
                uint64_t core_y,
                uint64_t risc,
                uint64_t marker,
                uint64_t timestamp,
                uint64_t line,
                std::string file,
                std::string zone_name,
                TTDeviceEventPhase zone_phase
                ): run_num(run_num),chip_id(chip_id),core_x(core_x),core_y(core_y),risc(risc),marker(marker),timestamp(timestamp),line(line),file(file),zone_name(zone_name),zone_phase(zone_phase)
        {
        }

        TTDeviceEvent (uint64_t threadID) :run_num(-1),marker(-1)
        {
            risc = (threadID) & ((1 << RISC_BIT_COUNT) - 1);
            core_x = (threadID >> CORE_X_BIT_SHIFT) & ((1 << CORE_X_BIT_COUNT) - 1);
            core_y = (threadID >> CORE_Y_BIT_SHIFT) & ((1 << CORE_Y_BIT_COUNT) - 1);
            chip_id = (threadID >> CHIP_BIT_SHIFT) & ((1 << CHIP_BIT_COUNT) - 1);
        }

        friend bool operator<(const TTDeviceEvent& lhs, const TTDeviceEvent& rhs) {
            if (lhs.timestamp != rhs.timestamp) {
                return lhs.timestamp < rhs.timestamp;
            }
            if (lhs.chip_id != rhs.chip_id) {
                return lhs.chip_id < rhs.chip_id;
            }
            if (lhs.core_x != rhs.core_x) {
                return lhs.core_x < rhs.core_x;
            }
            if (lhs.core_y != rhs.core_y) {
                return lhs.core_y < rhs.core_y;
            }
            if (lhs.risc != rhs.risc) {
                return lhs.risc < rhs.risc;
            }
            return lhs.marker < rhs.marker;
        }

        friend bool operator==(const TTDeviceEvent& lhs, const TTDeviceEvent& rhs) {
            return lhs.timestamp == rhs.timestamp && lhs.chip_id == rhs.chip_id && lhs.core_x == rhs.core_x &&
                   lhs.core_y == rhs.core_y && lhs.risc == rhs.risc && lhs.marker == rhs.marker;
        }

        uint64_t get_thread_id() const
        {
            uint64_t threadID = risc |\
                               core_x << CORE_X_BIT_SHIFT |\
                               core_y << CORE_Y_BIT_SHIFT |\
                               chip_id << CHIP_BIT_SHIFT;

            return threadID;
        }
    };
}

namespace std {
template <>
struct hash<tracy::TTDeviceEvent> {
    std::size_t operator()(const tracy::TTDeviceEvent& obj) const {
        std::hash<uint64_t> hasher;
        std::size_t hash_value = 0;
        constexpr std::size_t hash_combine_prime = 0x9e3779b9;
        hash_value ^= hasher(obj.timestamp) + hash_combine_prime + (hash_value << 6) + (hash_value >> 2);
        hash_value ^= hasher(obj.chip_id) + hash_combine_prime + (hash_value << 6) + (hash_value >> 2);
        hash_value ^= hasher(obj.core_x) + hash_combine_prime + (hash_value << 6) + (hash_value >> 2);
        hash_value ^= hasher(obj.core_y) + hash_combine_prime + (hash_value << 6) + (hash_value >> 2);
        hash_value ^= hasher(obj.risc) + hash_combine_prime + (hash_value << 6) + (hash_value >> 2);
        hash_value ^= hasher(obj.marker) + hash_combine_prime + (hash_value << 6) + (hash_value >> 2);
        return hash_value;
    }
};
}  // namespace std
#endif
