import streamlit as st
from FCFS import create_gantt_chart_fcfs
from SJF import create_gantt_chart_sjf
from RR import create_gantt_chart_round_robin

# Streamlit app
def main():
    st.title("Scheduling Algorithms Visualization")

    # Select scheduling algorithm
    algorithm = st.selectbox("Select Scheduling Algorithm", ["FCFS", "SJF", "Round Robin"])

    # FCFS scheduling algorithm
    if algorithm == "FCFS":
        st.header("First-Come, First-Served (FCFS) Scheduling")
        num_processes = st.number_input("Number of Processes", min_value=1, step=1, value=3)
        processes = []
        for i in range(num_processes):
            process_name = st.text_input(f"Process {i+1} Name", f"P{i+1}")
            arrival_time = st.number_input(f"Process {i+1} Arrival Time", min_value=0, step=1, value=0)
            burst_time = st.number_input(f"Process {i+1} Burst Time", min_value=1, step=1, value=1)
            processes.append((process_name, arrival_time, burst_time))

        if st.button("Generate Gantt Chart"):
            fig = create_gantt_chart_fcfs(processes)
            st.pyplot(fig)

    # SJF scheduling algorithm
    elif algorithm == "SJF":
        st.header("Shortest Job First (SJF) Scheduling")
        num_processes = st.number_input("Number of Processes", min_value=1, step=1, value=3)
        processes = []
        for i in range(num_processes):
            process_name = st.text_input(f"Process {i+1} Name", f"P{i+1}")
            burst_time = st.number_input(f"Process {i+1} Burst Time", min_value=1, step=1, value=1)
            processes.append((process_name, burst_time))

        if st.button("Generate Gantt Chart"):
            fig = create_gantt_chart_sjf(processes)
            st.pyplot(fig)

    # Round Robin scheduling algorithm
    elif algorithm == "Round Robin":
        st.header("Round Robin Scheduling")
        time_quantum = st.number_input("Time Quantum", min_value=1, step=1, value=1)
        num_processes = st.number_input("Number of Processes", min_value=1, step=1, value=3)
        processes = []
        for i in range(num_processes):
            process_name = st.text_input(f"Process {i+1} Name", f"P{i+1}")
            burst_time = st.number_input(f"Process {i+1} Burst Time", min_value=1, step=1, value=1)
            processes.append((process_name, burst_time))

        if st.button("Generate Gantt Chart"):
            fig = create_gantt_chart_round_robin(processes, time_quantum)
            st.pyplot(fig)

if __name__ == "__main__":
    main()
