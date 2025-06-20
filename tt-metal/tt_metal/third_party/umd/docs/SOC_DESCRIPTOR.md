# Overview
The Tenstorrent (TT) software stack was intended to be used with a variety of Tenstorrent silicon devices, e.g.,
Wormhole™, etc. All of these devices have a particular, grid-like SoC architecture that the software
was tailored towards.

More specifically, here are some (but not all) of that assumptions that were considered when developing our
software stacks:
1. The SoC is built in a grid configuration, where each coordinate could be associated with a particular SoC
function, e.g., coordinate 0,0 is a Tensix Compute Core, coordinate 7,3 is a DRAM controller port, etc.
2. The SoC has some interchain links that are implemented using Ethernet and/or PCIe. Those inter-chip links
differ from one version of the TT SoC to another.
3. The DRAM coordinate address range starts from offset 0, and goes from 0 to the DRAM bank size that is
defined in the SoC descriptor YAML file. (see how to add an offset to DRAM addressing in [CUSTOM_MODIFICATION_GUIDE.md](./CUSTOM_MODIFICATION_GUIDE.md))
4. The traffic originating from different cores to other cores and/or to DRAM would be placed on different
NoC’s, potentially to increase throughput.
5. If the IP is reached through a PCIe, then both Tensix L1 memory and DRAM should have an address
allocated for a ‘barrier’ function, where higher software stacks can set / reset to synchronize between kernel dispatching and
data sending.

## SoC Descriptor explanation

The SoC descriptor file tells UMD what resources it could provide for a given workload on a particular SoC. Example SoC descriptors
can be found in [soc_descs folder](../tests/soc_descs/).

The following is a guide on how write up a custom SoC descriptor:
1. Set the proper grid size with X/Y coordinates (including all components that are placed on a Tensix NOC ,e.g. NoC2AXI,Tensix,Router_only,etc... coordinates).
2. Leave pcie/eth/arc/harvested_workers/routers_only empty, as these are SoC specific resources configured in a very specific way in our silicon devices.
3. Define the coordinates of Tensix Cores in the functional_workers section.
4. In the DRAM section, configure the coordinates for your NoC2AXI components in a two-dimensional structure. The first dimension, channel, corresponds to a DRAM
bank, and the second dimension, subchannel, lists NoC grid coordinates that can communicate with the DRAM bank. Different subchannels within the same channel are
used to access the same DRAM address space, these should be used for parallelization purposes, e.g within the same channel, accessing address 0x0 on two subchannels
should refer to the same memory location. in General , there is no strict guideline on how to allocate banks to different NOC2AXI, and how to divide each bank to subchannels.
These decisions are up to the user's discretion.
Here are some examples on how to set the dram section, assuming we have 4 endpoints to the soC NoC at positions 0-4 , 1-4 , 2-4 , 3-5:
   a. Route each end point to a different DRAM bank : 
     ```sh
       dram : [0-4 , 1-4 , 2-4 , 3-5]  ## Each endpoint is addressing a different bank, starting from address 0 for each respective bank.
     ```
   b. Route each 2 endpoint pair to the same DRAM bank :
   ```sh
     dram : [[0-4 , 1-4] , [2-4 , 3-5]] ## Each endpoint pair is routed to an individual DRAM bank. For example, you can reach bank 0 from either endpoint 0-4 or 1-4.
   ``` 
8. Set the dram_bank_size to the desired size to be allocated on the device, where the software stack
can store tensors, inter-op data that is not reused, etc.
9. The memory size in bytes of a single tensix core or cluster is defined in the entry `worker_l1_size`
10. The arch_name field defines at some places how our Driver initializes the device, mostly how harvesting is done. Legal values for this field
can be found in [arch type definition file](../device/api/umd/device/types/arch.h).
