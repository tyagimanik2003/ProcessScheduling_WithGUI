#include <stdio.h>

void sjf(int n, int bt[]) {
    int wt[n], tat[n], p[n], total_wt = 0, total_tat = 0;
    for (int i = 0; i < n; i++) {
        p[i] = i + 1;
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (bt[j] > bt[j + 1]) {
                int temp = bt[j];
                bt[j] = bt[j + 1];
                bt[j + 1] = temp;
                temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
    wt[0] = 0;
    for (int i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
        total_wt += wt[i];
    }
    for (int i = 0; i < n; i++) {
        tat[i] = wt[i] + bt[i];
        total_tat += tat[i];
    }
    printf("SJF Scheduling Algorithm\n");
    printf("Process Burst Time Waiting Time Turnaround Time\n");
    for (int i = 0; i < n; i++) {
        printf("%d \t %d \t\t %d \t\t %d\n", p[i], bt[i], wt[i], tat[i]);
    }
    printf("Average Waiting Time = %f\n", (float)total_wt / n);
    printf("Average Turnaround Time = %f\n", (float)total_tat / n);
}
