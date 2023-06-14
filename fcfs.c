#include <stdio.h>

void fcfs(int n, int bt[]) {
    int wt[n], tat[n], total_wt = 0, total_tat = 0;
    wt[0] = 0;
    for (int i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
        total_wt += wt[i];
    }
    for (int i = 0; i < n; i++) {
        tat[i] = wt[i] + bt[i];
        total_tat += tat[i];
    }
    printf("FCFS Scheduling Algorithm\n");
    printf("Process Burst Time Waiting Time Turnaround Time\n");
    for (int i = 0; i < n; i++) {
        printf("%d \t %d \t\t %d \t\t %d\n", i + 1, bt[i], wt[i], tat[i]);
    }
    printf("Average Waiting Time = %f\n", (float)total_wt / n);
    printf("Average Turnaround Time = %f\n", (float)total_tat / n);
}
