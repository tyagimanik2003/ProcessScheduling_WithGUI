import matplotlib.pyplot as plt

# Define the processes with their arrival times and burst times
processes = [
    ("P1", 0, 10),
    ("P2", 3, 6),
    ("P3", 4, 8),
    ("P4", 7, 3),
    ("P5", 9, 5)
]

# Sort the processes based on their arrival times
sorted_processes = sorted(processes, key=lambda x: x[1])

# Create a figure and axis
fig, ax = plt.subplots()

# Set y-axis limits
ax.set_ylim(0, len(sorted_processes))

# Calculate the total timeline span
start_times = [start for _, start, _ in sorted_processes]
end_times = [start + burst for _, start, burst in sorted_processes]
total_timeline = max(end_times)

# Set x-axis limits
ax.set_xlim(0, total_timeline)

# Set y-axis labels
ax.set_yticks(range(len(sorted_processes)))
ax.set_yticklabels(process for process, _, _ in sorted_processes)

# Plot the Gantt chart
for i, (process, start, burst) in enumerate(sorted_processes):
    ax.barh(i, burst, left=start, height=0.5, align='center', alpha=0.8)
    ax.text(start + burst / 2, i, str(burst), ha='center', va='center')

# Set the title and labels
ax.set_title("FCFS Gantt Chart")
ax.set_xlabel("Time")

# Show the plot
plt.show()
