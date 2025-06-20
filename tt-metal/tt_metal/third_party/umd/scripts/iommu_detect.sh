#!/bin/bash

# Device IDs
TT_VID="1e52"
GS_PID="faca"
WH_PID="401e"
BH_PID="b140"

tt_devices=$(lspci -D -d ${TT_VID}: | cut -d' ' -f1)

if [ -z "$tt_devices" ]; then
    echo "No Tenstorrent devices found"
    exit 1
fi

found_gs_wh=false
found_bh=false

# First identify devices
for dev in $tt_devices; do
    device_id=$(lspci -D -n -s "$dev" | cut -d' ' -f3 | cut -d: -f2)
    case $device_id in
        $GS_PID|$WH_PID) found_gs_wh=true ;;
        $BH_PID) found_bh=true ;;
    esac
done

# Check and output for each device
for dev in $tt_devices; do
    device_id=$(lspci -D -n -s "$dev" | cut -d' ' -f3 | cut -d: -f2)
    echo "Checking device $dev (ID: $device_id):"
    
    # Check IOMMU status for this device
    iommu_enabled=false
    iommu_type="none"
    if [ -f "/sys/bus/pci/devices/${dev}/iommu_group/type" ]; then
        iommu_type=$(cat "/sys/bus/pci/devices/${dev}/iommu_group/type")
        [[ "$iommu_type" == *"DMA"* ]] && iommu_enabled=true
    fi

    if [[ "$device_id" == "$GS_PID" || "$device_id" == "$WH_PID" ]]; then
        if [ "$iommu_enabled" = true ]; then
            echo "  WARNING: Grayskull/Wormhole device with IOMMU enabled (type: $iommu_type) - this configuration is not supported"
        else
            echo "  Grayskull/Wormhole device detected - hugepages required"
        fi
    elif [[ "$device_id" == "$BH_PID" ]]; then
        if [ "$iommu_enabled" = true ]; then
            echo "  Blackhole device with IOMMU enabled (type: $iommu_type) - hugepages optional"
        else
            echo "  Blackhole device with no IOMMU/passthrough (type: $iommu_type) - hugepages required"
        fi
    else
        echo "  Unknown device ID: $device_id"
    fi
done

echo -e "\nSummary:"
if [ "$found_gs_wh" = true ]; then
    echo "- System has Grayskull/Wormhole devices - hugepages required"
    echo "- IOMMU must be disabled or in passthrough mode"
elif [ "$found_bh" = true ]; then
    echo "- System has Blackhole devices - check IOMMU status above to determine if hugepages are needed"
fi
