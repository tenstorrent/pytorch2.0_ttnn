import matplotlib.pyplot as plt
import json


def plot_bar_chart(data_points, dest_file):
    # Convert the keys back to tuples
    data_points = {eval(key): value for key, value in data_points.items()}
    # Convert tensor sizes from bytes to megabytes (1 MB = 1024 * 1024 bytes)
    data_points_mb = [
        [(tid, size / (1024 * 1024)) for tid, size in value]
        for key, value in data_points.items()
    ]

    # Adjust the figure size
    plt.figure(figsize=(18, 8))

    bar_width = 1.2  # Set a wider bar width
    bar_spacing = 0.6  # Adjust the spacing between bars

    # Create a colormap
    colors = plt.cm.get_cmap("tab20", len(data_points_mb))

    sram_limit_mb = 100

    # Plot each tensor's size as a box at each time step
    for i, tensors in enumerate(data_points_mb):
        bottom = 1e-6  # Start from a small value to avoid log(0) issues

        if not tensors:  # Handle blank entries
            continue

        for j, (tensor_id, size) in enumerate(tensors):
            plt.bar(
                i * (bar_width + bar_spacing),
                size,
                bottom=bottom,
                color=colors(i),
                edgecolor="black",
                width=bar_width,
            )
            plt.text(
                i * (bar_width + bar_spacing),
                bottom + size / 2,
                f"{tensor_id}",
                ha="center",
                va="center",
                fontsize=8,
                color="black",
            )
            bottom += size

    # Draw horizontal line for SRAM memory limit (100 MB)
    plt.axhline(
        y=sram_limit_mb,
        color="red",
        linestyle="--",
        linewidth=2,
        label="SRAM Memory Limit (100 MB)",
    )

    plt.xlabel("TTNN Op Sequence")
    plt.ylabel("Tensor Size (MB)")
    plt.title("Tensor Sizes Over Time")
    plt.yscale("log")  # Set y-axis to logarithmic scale

    # Remove grid lines for a cleaner look
    plt.grid(False)

    # Add legend for the SRAM memory limit line only
    plt.legend(
        handles=[plt.Line2D([0], [0], color="red", linestyle="--", linewidth=2)],
        labels=["SRAM Memory Limit (100 MB)"],
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.tight_layout()

    # Save the plot as a JPEG or PNG file
    plt.savefig(dest_file, format="png", dpi=300)

    # Show the plot
    plt.show()


def plot_line_chart(data_points, dest_file):
    # Convert the keys back to tuples
    data_points = {eval(key): value for key, value in data_points.items()}
    # Convert tensor sizes from bytes to megabytes (1 MB = 1024 * 1024 bytes)
    data_points_mb = [
        [(tid, size / (1024 * 1024)) for tid, size in value]
        for key, value in data_points.items()
    ]

    # Calculate the total tensor size for each entry
    total_sizes = [sum(size for _, size in tensors) for tensors in data_points_mb]

    # Plot the total tensor sizes over time
    plt.figure(figsize=(18, 8))

    # Plot the line chart
    plt.plot(
        range(len(total_sizes)), total_sizes, marker="o", linestyle="-", color="blue"
    )

    # Draw horizontal line for SRAM memory limit (1 MB)
    sram_limit_mb = 100
    plt.axhline(
        y=sram_limit_mb,
        color="red",
        linestyle="--",
        linewidth=2,
        label="SRAM Memory Limit (100 MB)",
    )

    plt.xlabel("Time (Sequence of operations)")
    plt.ylabel("Total Tensor Size (MB)")
    plt.title("Total Tensor Sizes Over Time")
    plt.yscale("log")  # Set y-axis to logarithmic scale

    # Add legend for the SRAM memory limit line only
    plt.legend(
        handles=[plt.Line2D([0], [0], color="red", linestyle="--", linewidth=2)],
        labels=["SRAM Memory Limit (100 MB)"],
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.tight_layout()

    # Save the plot as a JPEG or PNG file
    plt.savefig(dest_file, format="png", dpi=300)

    # Show the plot
    plt.show()
