import tkinter as tk
import subprocess
# Create the GUI
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
        self.quantum_label = tk.Label(master, text="Quantum (for RR only):")
        self.quantum_label.grid(row=3, column=0)
        self.quantum_entry = tk.Entry(master)
        self.quantum_entry.grid(row=3, column=1)

        # Create the result field
        self.result_label = tk.Label(master, text="Results:")
        self.result_label.grid(row=4, column=0)
        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=4, column=1)

        # Create the search button
        self.search_button = tk.Button(master, text="Run", command=self.run_algorithm)
        self.search_button.grid(row=5, column=0, columnspan=2)

    def run_algorithm(self):
        # Get the input parameters from the GUI
        algorithm = self.algorithm_var.get()
        processes = self.processes_entry.get()
        burst_times = self.burst_times_entry.get()
        quantum = self.quantum_entry.get()

        # Define the command to execute based on the selected algorithm
        if algorithm == "FCFS":
            cmd = f"fcfs.c {processes} {burst_times}"
        elif algorithm == "SJF":
            cmd = f"fcfs.c {processes} {burst_times}"
        elif algorithm == "RR":
            cmd = f"fcfs.c {processes} {burst_times} {quantum}"
        else:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Invalid algorithm selected.")
            return

        # Execute the command and capture the output
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            result = e.output

        # Display the results in the GUI
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

    def __init__(self, master):
        self.master = master
        master.title("Scheduler App")

        # Create the input fields and other widgets

        # Create the canvas for the Gantt chart
        self.chart_canvas = tk.Canvas(master, width=500, height=200)
        self.chart_canvas.grid(row=6, column=0, columnspan=2)

    def draw_gantt_chart(self, processes, burst_times, completion_times):
        # Clear the previous chart
        self.chart_canvas.delete(tk.ALL)

        # Calculate the total time taken by all the processes
        total_time = sum(burst_times)

        # Define the dimensions of the chart
        chart_width = 500
        chart_height = 200
        y_offset = 50

        # Calculate the width of each rectangle
        rect_width = chart_width / total_time

        # Draw the rectangles and labels for each process
        for i in range(len(processes)):
            start_time = sum(burst_times[:i])
            end_time = completion_times[i]

            x1 = start_time * rect_width
            y1 = y_offset + i * 25
            x2 = end_time * rect_width
            y2 = y_offset + (i + 1) * 25

            self.chart_canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            self.chart_canvas.create_text(x1 + 5, y1 + 5, anchor=tk.NW, text=processes[i])



# Create the main window and pass it to the SchedulerApp class
root = tk.Tk()
app = SchedulerApp(root)

# Start the GUI main loop
root.mainloop()
