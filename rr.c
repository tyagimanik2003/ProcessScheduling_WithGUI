#include <stdio.h>
#include <stdlib.h>

struct process {
    int pid;
    int burst_time;
    int remaining_time;
    int waiting_time;
    int turnaround_time;
    int arrival_time;
};

int main(int argc, char *argv[]) {
    int num_processes = argc - 2;
    int quantum = atoi(argv[argc-1]);
    struct process processes[num_processes];
    int time = 0;
    int i, j;

    // Initialize the processes array from the command-line arguments
    for (i = 0; i < num_processes; i++) {
        processes[i].pid = i+1;
        processes[i].burst_time = atoi(argv[i+1]);
        processes[i].remaining_time = processes[i].burst_time;
        processes[i].waiting_time = 0;
        processes[i].turnaround_time = 0;
        processes[i].arrival_time = 0;
    }

    // Run the Round Robin scheduling algorithm
    while (1) {
        int all_done = 1;

        for (i = 0; i < num_processes; i++) {
            if (processes[i].remaining_time > 0) {
                all_done = 0;

                // Run the process for the quantum or until it finishes
                for (j = 0; j < quantum && processes[i].remaining_time > 0; j++) {
                    processes[i].remaining_time--;
                    time++;
                }

                // Update the waiting and turnaround times
                for (j = 0; j < num_processes; j++) {
                    if (j != i && processes[j].remaining_time > 0) {
                        processes[j].waiting_time += j < i ? quantum : j == i ? time - quantum : 0;
                    }
                }

                // Check if the process has finished
                if (processes[i].remaining_time == 0) {
                    processes[i].turnaround_time = time;
                }
            }
        }

        if (all_done) {
            break;
        }
    }

    // Calculate the average waiting and turnaround times
    float avg_waiting_time = 0;
    float avg_turnaround_time = 0;
    for (i = 0; i < num_processes; i++) {
        avg_waiting_time += processes[i].waiting_time;
        avg_turnaround_time += processes[i].turnaround_time;
    }
    avg_waiting_time /= num_processes;
    avg_turnaround_time /= num_processes;

    // Print the results to standard output
    printf("Average Waiting Time: %.2f\n", avg_waiting_time);
    printf("Average Turnaround Time: %.2f\n", avg_turnaround_time);

    return 0;
}
