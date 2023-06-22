import matplotlib.pyplot as plt

# Function to create the Gantt chart for SJF
def create_gantt_chart_sjf(processes):
    sorted_processes = sorted(processes, key=lambda x: x[1])

    fig, ax = plt.subplots()
    ax.set_ylim(0, len(sorted_processes))
    start_times = [sum(burst for _, burst in sorted_processes[:i]) for i in range(len(sorted_processes))]
    end_times = [start + burst for (_, start, burst) in sorted_processes]
    total_timeline = max(end_times)
    ax.set_xlim(0, total_timeline)
    ax.set_yticks(range(len(sorted_processes)))
    ax.set_yticklabels(process for process, _, _ in sorted_processes)

    for i, (process, start, burst) in enumerate(sorted_processes):
        ax.barh(i, burst, left=start, height=0.5, align='center', alpha=0.8)
        ax.text(start + burst / 2, i, str(burst), ha='center', va='center')

    ax.set_title("SJF Gantt Chart")
    ax.set_xlabel("Time")

    return fig
