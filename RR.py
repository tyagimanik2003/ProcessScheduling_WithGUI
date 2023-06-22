import matplotlib.pyplot as plt

# Function to create the Gantt chart for Round Robin
def create_gantt_chart_round_robin(processes, time_quantum):
    fig, ax = plt.subplots()
    ax.set_ylim(0, len(processes))
    start_times = [0] * len(processes)
    end_times = [0] * len(processes)

    remaining_burst_times = [burst for (_, burst) in processes]
    current_time = 0
    while True:
        all_processes_completed = True
        for i, (process, burst) in enumerate(processes):
            if remaining_burst_times[i] > 0:
                all_processes_completed = False
                if remaining_burst_times[i] <= time_quantum:
                    current_burst = remaining_burst_times[i]
                else:
                    current_burst = time_quantum
                remaining_burst_times[i] -= current_burst
                start_times[i] = current_time
                current_time += current_burst
                end_times[i] = current_time
        if all_processes_completed:
            break

    total_timeline = max(end_times)
    ax.set_xlim(0, total_timeline)
    ax.set_yticks(range(len(processes)))
    ax.set_yticklabels(process for process, _ in processes)

    for i, (process, _) in enumerate(processes):
        ax.barh(i, end_times[i] - start_times[i], left=start_times[i], height=0.5, align='center', alpha=0.8)
        ax.text(start_times[i] + (end_times[i] - start_times[i]) / 2, i, str(end_times[i] - start_times[i]), ha='center', va='center')

    ax.set_title("Round Robin Gantt Chart")
    ax.set_xlabel("Time")

    return fig
