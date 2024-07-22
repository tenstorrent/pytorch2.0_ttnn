import matplotlib.pyplot as plt

# Data points for MNIST model
# data_points = [
#     [(0, 43264), (1, 43264)],
#     [],
#     [(2, 73728), (3, 73728)],
#     [],
#     [(4, 18432), (5, 18432)],
#     [],
#     [(6, 2359296), (7, 2359296)],
#     [(7, 2359296)],
#     [(7, 2359296), (8, 18432), (9, 256)],
#     [(9, 256)],
#     [(9, 256), (10, 256), (11, 256)],
#     [(11, 256)],
#     [(11, 256), (12, 256)],
#     [(12, 256)],
#     [(12, 256), (13, 256)],
#     [(13, 256)],
#     [(13, 256), (14, 2560), (15, 2560)],
#     [(13, 256), (15, 2560)],
#     [(13, 256), (15, 2560), (16, 20)],
#     [(16, 20)],
#     [(16, 20), (17, 20), (18, 20)],
#     []
# ]

# Data points for Resnet18 model
data_points = [
    [(0, 1605632), (1, 1605632)],
    [],
    [(2, 401408), (3, 401408)],
    [],
    [(4, 401408), (5, 401408), (6, 401408)],
    [(6, 401408)],
    [(6, 401408), (7, 401408)],
    [(7, 401408)],
    [(7, 401408), (8, 401408), (9, 401408)],
    [(7, 401408)],
    [(7, 401408), (10, 401408), (11, 401408)],
    [(11, 401408)],
    [(11, 401408), (12, 401408)],
    [],
    [(13, 200704), (14, 200704)],
    [],
    [(15, 200704), (16, 200704), (17, 200704)],
    [(17, 200704)],
    [(17, 200704), (18, 200704)],
    [(18, 200704)],
    [(18, 200704), (19, 200704), (20, 200704)],
    [(18, 200704)],
    [(18, 200704), (21, 200704), (22, 200704)],
    [(22, 200704)],
    [(22, 200704), (23, 200704)],
    [],
    [(24, 100352), (25, 100352)],
    [],
    [(26, 100352), (27, 100352), (28, 100352)],
    [(28, 100352)],
    [(28, 100352), (29, 100352)],
    [(29, 100352)],
    [(29, 100352), (30, 100352), (31, 100352)],
    [(29, 100352)],
    [(29, 100352), (32, 100352), (33, 100352)],
    [(33, 100352)],
    [(33, 100352), (34, 100352)],
    [],
    [(35, 50176), (36, 50176)],
    [],
    [(37, 50176), (38, 50176), (39, 50176)],
    [(39, 50176)],
    [(39, 50176), (40, 50176)],
    [(40, 50176)],
    [(40, 50176), (41, 50176), (42, 50176)],
    [(40, 50176)],
    [(40, 50176), (43, 50176), (44, 50176)],
    [(44, 50176)],
    [(44, 50176), (45, 50176)],
    [(45, 50176)],
    [(45, 50176), (46, 1024)],
    [],
    [(47, 1024000), (48, 1024000)],
    [(48, 1024000)],
    [(48, 1024000), (49, 1024), (50, 2000)],
    [(50, 2000)],
    [(50, 2000), (51, 2000), (52, 2000)],
    []
]

# Convert tensor sizes from bytes to megabytes (1 MB = 1024 * 1024 bytes)
data_points_mb = [[(tid, size / (1024 * 1024)) for tid, size in tensors] for tensors in data_points]

# Define colors for the boxes
colors = plt.cm.tab20.colors

plt.figure(figsize=(14, 8))

# Plot each tensor's size as a box at each time step
for i, tensors in enumerate(data_points_mb):
    bottom = 1e-6  # Start from a small value to avoid log(0) issues
    for j, (tensor_id, size) in enumerate(tensors):
        plt.bar(i, size, bottom=bottom, color=colors[tensor_id % len(colors)], edgecolor='black')
        plt.text(i, bottom + size / 2, f't{tensor_id}', ha='center', va='center', fontsize=8, color='black')
        bottom += size

# Draw horizontal line for SRAM memory limit (1 MB)
sram_limit_mb = 1
plt.axhline(y=sram_limit_mb, color='red', linestyle='--', linewidth=2, label='SRAM Memory Limit (1 MB)')

plt.xlabel('Time (Sequence of operations)')
plt.ylabel('Tensor Size (MB)')
plt.title('Tensor Sizes Over Time in SRAM memory')
plt.yscale('log')  # Set y-axis to logarithmic scale
plt.grid(True, axis='y', which='both', linestyle='--')

# Custom legend
handles = [plt.Rectangle((0,0),1,1, color=colors[i % len(colors)]) for i in range(max(max(tensor[0] for tensor in tensors) for tensors in data_points if tensors))]
labels = [f't{i}' for i in range(max(max(tensor[0] for tensor in tensors) for tensors in data_points if tensors))]
plt.legend(handles, labels, title='Tensors', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add legend for the SRAM memory limit line
plt.legend(handles=handles + [plt.Line2D([0], [0], color='red', linestyle='--', linewidth=2)], 
           labels=labels + ['SRAM Memory Limit (1 MB)'], 
           bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

# Save the plot as a JPEG or PNG file
# plt.savefig('memory_chart.jpg', format='jpg', dpi=300)
plt.savefig('tools/memory_models/assets/resnet18_memory_chart.png', format='png', dpi=300)

plt.show()
