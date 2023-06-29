# Scheduler App

This is a Python application that simulates different process scheduling algorithms. It provides a graphical user interface (GUI) built using the Tkinter library.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- Tkinter

## Getting Started

To run the Scheduler App, follow these steps:

1. Clone the repository or download the source code files.
2. Open a terminal or command prompt.
3. Navigate to the directory where the files are located.
4. Run the following command to start the application:

   ```
   python scheduler_app.py
   ```

## Usage

Once the application is running, you can perform the following steps:

1. Choose the scheduling algorithm from the dropdown menu. The available options are "FCFS" (First-Come, First-Served), "SJF" (Shortest Job First), and "RR" (Round Robin).
2. Enter the processes, burst times, and arrival times in the corresponding input fields. Separate multiple values with commas.
3. If you selected the "RR" algorithm, enter the quantum value in the designated input field.
4. Click the "Run" button to execute the selected algorithm and view the results.
5. The results will be displayed in the "Results" section of the GUI. If applicable, a Gantt chart and additional information will be shown.

Note: The Gantt chart functionality is currently commented out in the code. If you want to enable it, uncomment the related code blocks.

## Algorithms

### First-Come, First-Served (FCFS)

The FCFS algorithm schedules processes in the order they arrive. It does not consider the burst time or any other factor when making scheduling decisions.

### Shortest Job First (SJF)

The SJF algorithm schedules processes based on their burst time. It selects the process with the shortest burst time first.

### Round Robin (RR)

The RR algorithm schedules processes by assigning them a fixed time quantum. Each process gets a certain amount of time to execute before being preempted and allowing the next process to run.

## Authors

This application was developed by Manik Tyagi.
