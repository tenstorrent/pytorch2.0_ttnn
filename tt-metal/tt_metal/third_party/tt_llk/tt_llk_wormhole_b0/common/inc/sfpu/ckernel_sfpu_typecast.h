// SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
//
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include "ckernel.h"
#include "sfpi.h"

namespace ckernel
{
namespace sfpu
{

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_fp16b_to_uint16_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 0, 3, 0);
        TTI_SFPSETCC(0, 0, 0, 0);
        TTI_SFPLOADI(0, 0, 0);
        TTI_SFPENCC(0, 0, 0, 0);
        TTI_SFP_STOCH_RND(0, 0, 2, 0, 1, 14);
        TTI_SFPSTORE(1, 6, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_uint16_to_fp16b_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 6, 3, 0);
        TTI_SFPCAST(0, 1, 0);
        TTI_SFP_STOCH_RND(0, 0, 3, 1, 2, 1);
        TTI_SFPSTORE(2, 2, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_int32_to_fp16b_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 12, 3, 0);
        TTI_SFPCAST(0, 1, 0);
        TTI_SFP_STOCH_RND(0, 0, 3, 1, 2, 1);
        TTI_SFPSTORE(2, 2, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_fp16b_to_int32_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        sfpi::vFloat in = sfpi::dst_reg[0];

        // extract exponent
        sfpi::vInt exp = exexp(in);

        v_if (exp < 0)
        {
            sfpi::dst_reg[0] = 0;
        }
        v_elseif (exp > 30)
        {
            // set to int32 max value in case of overflow
            sfpi::vInt tmp = std::numeric_limits<int32_t>::max();
            // check sign
            v_if (in < 0)
            {
                tmp = sfpi::reinterpret<sfpi::vInt>(sfpi::setsgn(sfpi::reinterpret<sfpi::vFloat>(tmp), 1));
            }
            v_endif sfpi::dst_reg[0] = tmp;
        }
        v_else
        {
            // extract mantissa
            sfpi::vInt man = exman8(in);
            // shift the mantissa by (23-exponent) to the right
            sfpi::vInt shift = exp - 23;
            man              = sfpi::shft(sfpi::reinterpret<sfpi::vUInt>(man), shift);
            // check sign
            v_if (in < 0)
            {
                man = sfpi::reinterpret<sfpi::vInt>(sfpi::setsgn(sfpi::reinterpret<sfpi::vFloat>(man), 1));
            }
            v_endif sfpi::dst_reg[0] = man;
        }
        v_endif

            sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_fp32_to_fp16b_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 0, 3, 0);
        TTI_SFP_STOCH_RND(0, 0, 2, 0, 1, 1);
        TTI_SFPSTORE(1, 0, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_uint16_to_fp32_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 6, 3, 0);
        TTI_SFPCAST(0, 1, 0);
        TTI_SFPSTORE(1, 3, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_int32_to_fp32_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 12, 3, 0);
        TTI_SFPCAST(0, 1, 0);
        TTI_SFPSTORE(1, 3, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_fp16b_to_uint32_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        sfpi::vFloat in = sfpi::dst_reg[0];

        // check sign
        v_if (in <= 0)
        {
            sfpi::dst_reg[0] = 0;
        }
        v_else
        {
            // extract exponent
            sfpi::vInt exp = exexp(in);

            v_if (exp < 0)
            {
                sfpi::dst_reg[0] = 0;
            }
            v_elseif (exp > 31)
            {
                // set to uint32 max value in case of overflow
                sfpi::vInt tmp   = std::numeric_limits<int32_t>::max();
                sfpi::dst_reg[0] = sfpi::setsgn(sfpi::reinterpret<sfpi::vFloat>(tmp), 1);
            }
            v_elseif (exp == 31)
            {
                // extract mantissa without hidden bit
                sfpi::vInt man = exman9(in);
                // shift the mantissa by (23-exponent) to the right
                sfpi::vInt shift = exp - 23;
                man              = sfpi::shft(sfpi::reinterpret<sfpi::vUInt>(man), shift);
                // add hidden bit back (due to bug when shifting a 1 into MSB)
                sfpi::dst_reg[0] = sfpi::setsgn(sfpi::reinterpret<sfpi::vFloat>(man), 1);
            }
            v_else
            {
                // extract mantissa
                sfpi::vInt man = exman8(in);
                // shift the mantissa by (23-exponent) to the right
                sfpi::vInt shift = exp - 23;
                man              = sfpi::shft(sfpi::reinterpret<sfpi::vUInt>(man), shift);
                sfpi::dst_reg[0] = man;
            }
            v_endif
        }
        v_endif

            sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_uint32_to_fp16b_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 4, 3, 0);
        TTI_SFPSETSGN(0, 0, 1, 1);
        TTI_SFPCAST(1, 2, 0);
        TTI_SFP_STOCH_RND(0, 0, 4, 2, 3, 1);
        TTI_SFPSETCC(0, 0, 0, 0);
        TTI_SFPADDI(0x4f00, 3, 0); // 2^31
        TTI_SFPENCC(0, 0, 0, 0);
        TTI_SFPSTORE(3, 2, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_uint32_to_fp32_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 4, 3, 0);
        TTI_SFPSETSGN(0, 0, 1, 1);
        TTI_SFPCAST(1, 2, 0);
        TTI_SFPSETCC(0, 0, 0, 0);
        TTI_SFPADDI(0x4f00, 2, 0); // 2^31
        TTI_SFPENCC(0, 0, 0, 0);
        TTI_SFPSTORE(2, 3, 3, 0);
        sfpi::dst_reg++;
    }
}

template <bool APPROXIMATION_MODE, int ITERATIONS>
inline void _calculate_typecast_uint16_to_uint32_()
{
#pragma GCC unroll 0
    for (int d = 0; d < ITERATIONS; d++)
    {
        TTI_SFPLOAD(0, 6, 3, 0);
        TTI_SFPSTORE(0, 4, 3, 0);
        sfpi::dst_reg++;
    }
}

} // namespace sfpu
} // namespace ckernel
