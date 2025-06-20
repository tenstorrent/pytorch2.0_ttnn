# Tools

## Build flow

In general, see the common build instructions in the main [README](../README.md)

Short instructions for building tools:
```
cmake -B build -G Ninja
cmake --build build --target umd_tools
```

## Topology tool

The topology tool can be used to generate cluster descriptor which describes system topology of tenstorrent devices.
It shows information such as pci connected chips, remote chips, ethernet connections, harvesting, etc.

You can run the following for more information:
```
./build/tools/umd/topology --help
```

## Telemetry tool

The telemetry tool can be used to read telemetry from ARC. You can provide which pci chips should be polled, the frequency of polling and which telemetry to read.
It has a special mode where it can read some important factors for Wormhole device.

If you want to save the values, you can also pass an output file to write to.

You can run the following for more information:
```
./build/tools/umd/telemetry --help
```
