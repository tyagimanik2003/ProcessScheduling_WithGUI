import tkinter as tk
import subprocess
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SchedulerApp:
    def __init__(self, master):
        self.master = master
        master.title("Scheduler App")

        # Create the input fields
        self.algorithm_label = tk.Label(master, text="Algorithm:")
        self.algorithm_label.grid(row=0, column=0)
        self.algorithm_var = tk.StringVar(master)
        self.algorithm_var.set("FCFS")
        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, "FCFS", "SJF", "RR")
        self.algorithm_menu.grid(row=0, column=1)
        self.processes_label = tk.Label(master, text="Processes:")
        self.processes_label.grid(row=1, column=0)
        self.processes_entry = tk.Entry(master)
        self.processes_entry.grid(row=1, column=1)
        self.burst_times_label = tk.Label(master, text="Burst Times:")
        self.burst_times_label.grid(row=2, column=0)
        self.burst_times_entry = tk.Entry(master)
        self.burst_times_entry.grid(row=2, column=1)
        self.arrival_times_label = tk.Label(master, text="Arrival Times:")
        self.arrival_times_label.grid(row=3, column=0)
        self.arrival_times_entry = tk.Entry(master)
        self.arrival_times_entry.grid(row=3, column=1)
        self.quantum_label = tk.Label(master, text="Quantum (for RR only):")
        self.quantum_label.grid(row=4, column=0)
        self.quantum_entry = tk.Entry(master)
        self.quantum_entry.grid(row=4, column=1)

        # Create the result field
        self.result_label = tk.Label(master, text="Results:")
        self.result_label.grid(row=5, column=0)
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=5, column=1)

        # Create the search button
        self.search_button = tk.Button(master, text="Run", command=self.run_algorithm)
        self.search_button.grid(row=6, column=0, columnspan=2)

        # # Create the Gantt chart
        # self.gantt_label = tk.Label(master, text="Gantt Chart:")
        # self.gantt_label.grid(row=6, column=0)
        # self.gantt_canvas = tk.Canvas(master, height=100)
        # self.gantt_canvas.grid(row=7, column=0, columnspan=2)

    def generate_gantt_chart(self,processes, arrival_times, burst_times,waiting_times):
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

        gantt_chart = "Gantt Chart:\n" + "-" * (sum(burst_times) + n + 1) + "\n"
        for i in range(n):
            gantt_chart += "|" + " " * (start_times[i] - 1) + f"P{processes[i]}" + " " * (end_times[i] - start_times[i] - 1) + "|"
        gantt_chart += "\n" + "-" * (sum(burst_times) + n + 1) + "\n"
        gantt_chart += "Timeline:\n"
        for i in range(n):
            gantt_chart += f"P{processes[i]}:\t{start_times[i]} - {end_times[i]}\tWT: {waiting_times[i]}\n"
        gantt_chart += f"Average waiting time: {sum(waiting_times) / n:.2f}\n"
        gantt_chart += f"Average turnaround time: {sum(turnaround_times) / n:.2f}\n"

        return gantt_chart


    def fcfs(self,processes, arrival_times, burst_times):
        n = len(processes)
        # Calculate the start times for each process
        start_times = [0] * n
        for i in range(1, n):
            start_times[i] = max(start_times[i-1] + burst_times[i-1], arrival_times[i])
        # Calculate the completion times for each process
        completion_times = [0] * n
        for i in range(n):
            completion_times[i] = start_times[i] + burst_times[i]
        # Calculate the waiting times for each process
        waiting_times = [0] * n
        for i in range(n):
            waiting_times[i] = start_times[i] - arrival_times[i]

        # Calculate the turnaround times for each process
        turnaround_times = [0] * n
        for i in range(n):
            turnaround_times[i] = completion_times[i] - arrival_times[i]
        # Calculate average waiting time and average turnaround time
        avg_waiting_time = sum(waiting_times) / n
        avg_turnaround_time = sum(turnaround_times) / n

        # Generate the Gantt chart
        gantt_chart = self.generate_gantt_chart(processes, arrival_times, burst_times,waiting_times)
        return gantt_chart

    def run_algorithm(self):
        # Get the input parameters from the GUI
        algorithm = self.algorithm_var.get()
        processes = self.processes_entry.get().split(",")
        burst_times = self.burst_times_entry.get().split(",")
        arrival_times = self.arrival_times_entry.get().split(",")
        quantum = self.quantum_entry.get()

        # Convert the burst times to integers
        burst_times = [int(x) for x in burst_times]
        arrival_times = [int(x) for x in arrival_times]

        # Define the command to execute based on the selected algorithm
        if algorithm == "FCFS":
            results = self.fcfs(processes,arrival_times, burst_times)
        elif algorithm == "SJF":
            results = self.sjf(processes,arrival_times, burst_times)
        elif algorithm == "RR":
            results = self.rr(processes,arrival_times, burst_times, int(quantum))
        else:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Invalid algorithm selected.")
            return

        # Display the results in the GUI
        self.result_text.delete("1.0", tk.END)
        # self.result_text.insert(tk.END, results["output"])
        # # Update the GUI with the results
        if type(results) == dict and "output" in results:
            self.result_text.insert(tk.END, results["output"])
        else:
            self.result_text.insert(tk.END, str(results))




    def sjf(self, processes, arrival_times, burst_times):
        n = len(processes)

        # Initialize the start times, completion times, and waiting times for each process
        start_times = [0] * n
        completion_times = [0] * n
        waiting_times = [0] * n

        # Sort the processes by arrival time
        sorted_processes = sorted(range(n), key=lambda i: arrival_times[i])

        # Initialize the list of completed processes
        completed = []

        # Loop through each process in order of arrival time
        for i in sorted_processes:
            # If the process has not yet arrived, skip it
            if arrival_times[i] > sum(completion_times):
                continue

            # Calculate the remaining burst times for each process
            remaining_burst_times = [burst_times[j] for j in sorted_processes if j not in completed and arrival_times[j] <= sum(completion_times)]

            # Select the process with the shortest remaining burst time
            next_process = sorted(range(len(remaining_burst_times)), key=lambda j: remaining_burst_times[j])[0]

            # Set the start time for the selected process
            start_times[sorted_processes[next_process]] = sum(completion_times)

            # Update the completion time for the selected process
            completion_times[sorted_processes[next_process]] = start_times[sorted_processes[next_process]] + burst_times[sorted_processes[next_process]]

            # Update the waiting time for the selected process
            waiting_times[sorted_processes[next_process]] = start_times[sorted_processes[next_process]] - arrival_times[sorted_processes[next_process]]

            # Add the selected process to the list of completed processes
            completed.append(sorted_processes[next_process])

        # Calculate the turnaround times for each process
        turnaround_times = [completion_times[i] - arrival_times[i] for i in range(n)]

        # Calculate the average waiting time and average turnaround time
        avg_waiting_time = sum(waiting_times) / n
        avg_turnaround_time = sum(turnaround_times) / n

        # Generate the Gantt chart
        gantt_chart = self.generate_gantt_chart(processes, arrival_times, burst_times,waiting_times)
        return gantt_chart




# Create the main window and pass it to the SchedulerApp class
root = tk.Tk()
app = SchedulerApp(root)

# Start the GUI main loop
root.mainloop()
