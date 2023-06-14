def generate_gantt_chart(processes, arrival_times, burst_times,waiting_times):
    n = len(processes)
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n
    start_times = [0] * n
    end_times = [0] * n

    for i in range(n):
        if i == 0:
            start_times[i] = arrival_times[i]
        else:
            start_times[i] = max(completion_times[i-1], arrival_times[i])
        end_times[i] = start_times[i] + burst_times[i]
        completion_times[i] = end_times[i]
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    print("Gantt Chart:\n" + "-" * (sum(burst_times) + n + 1))
    for i in range(n):
        print("|" + " " * (start_times[i] - 1) + f"P{processes[i]}" + " " * (end_times[i] - start_times[i] - 1), end="|")
    print("\n" + "-" * (sum(burst_times) + n + 1))
    print("Timeline:")
    for i in range(n):
        print(f"P{processes[i]}:\t{start_times[i]} - {end_times[i]}\tWT: {waiting_times[i]}")
    print(f"Average waiting time: {sum(waiting_times) / n:.2f}")
    print(f"Average turnaround time: {sum(turnaround_times) / n:.2f}")

def generate_gantt_chart(processes, arrival_times, burst_times, waiting_times):
    n = len(processes)
    completion_times = [0] * n
    turnaround_times = [0] * n
    start_times = [0] * n
    end_times = [0] * n

    for i in range(n):
        if i == 0:
            start_times[i] = arrival_times[i]
        else:
            start_times[i] = max(completion_times[i-1], arrival_times[i])
        end_times[i] = start_times[i] + burst_times[i]
        completion_times[i] = end_times[i]
        turnaround_times[i] = completion_times[i] - arrival_times[i]

    print("Gantt Chart:\n" + "-" * (sum(burst_times) + n + 1))
    for i in range(n):
        print("|" + " " * (start_times[i] - 1) + f"P{processes[i]}" + " " * (end_times[i] - start_times[i] - 1), end="|")
    print("\n" + "-" * (sum(burst_times) + n + 1))

    return completion_times, turnaround_times, waiting_times, start_times, end_times

processes = [1, 2, 3]
arrival_times = [0, 2, 3]
burst_times = [4, 5, 6]
waiting_times = [0, 1, 4]


generate_gantt_chart(processes, arrival_times, burst_times, waiting_times)