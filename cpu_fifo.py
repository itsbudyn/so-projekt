# algorytm czasu procesora FIFO

from sys import exit

def do_fifo(processes):
    # PID , arrival , burst , Exit , TurnAround, Wait
    PID         = 0
    ARRIVAL     = 1
    BURST       = 2
    EXIT        = 3
    TURNAROUND  = 4
    WAIT        = 5
    REMAINING   = 6

    
    processes=sorted(processes, key=lambda x: x[1])

    processes_info=processes[:]

    max_time=0
    for i in processes:
        max_time+=i[2]

    timeline=[0 for i in range(max_time)]

    t=-1
    completed=0
    for i in range(len(timeline)):
        t+=1
        current_process=processes[0]
        if t<processes[0][1]:
            continue
        else:
            timeline[t]=current_process[0]
            processes[0][REMAINING]-=1
            if processes[0][REMAINING]==0: 
                del processes[0]
                processes_info[completed][EXIT]=t+1
                processes_info[completed][TURNAROUND]=processes_info[completed][EXIT]-processes_info[completed][ARRIVAL]
                processes_info[completed][WAIT]=processes_info[completed][TURNAROUND]-processes_info[completed][BURST]
                completed+=1

    print("PID\tArrv.\tBurst\tExit\tTA\tWait")
    ta_total=0
    w_total=0
    for i in processes_info:
        ta_total+=i[TURNAROUND]
        w_total+=i[WAIT]
        for j in range(len(i)):
            if j!=REMAINING: print(i[j],end="\t")
        print("")

    avg_ta=round(ta_total/len(processes_info),2)
    avg_w=round(w_total/len(processes_info),2)

    print("średnie: \t\t\t{}\t{}".format(avg_ta,avg_w))

    print("\n",timeline)

if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")