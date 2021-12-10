# algorytm czasu procesora FIFO

from sys import exit

def do_sjf(processes):
    # Słowa kluczowe, pomagające w indeksowaniu tablic
    PID         = 0
    ARRIVAL     = 1
    BURST       = 2
    EXIT        = 3
    TURNAROUND  = 4
    WAIT        = 5
    REMAINING   = 6

    # Sortowanie procesów po czasie przybycia
    processes=sorted(processes, key=lambda x: x[ARRIVAL])
    
    # Utwórz kopię kolejki procesów, potrzebne do tabeli końcowej
    processes_info=processes[:]

    # Obliczanie czasu wykonywania algorytmu
    max_time=0
    for i in processes:
        max_time+=i[2]

    # Budowa osi czasu na podstawie czasu wykonywania algorytmu
    timeline=[0 for i in range(max_time)]

    # Przygotowanie do naniesienia procesów na oś czasu
    t=-1

    # Pętla nanosząca procesy na oś czasu
    for i in range(len(timeline)):
        t+=1
        p_queue=[]
        for i in processes:
            if i[ARRIVAL] <= t: p_queue.append(i)

        print(processes)
        print(p_queue)

        if len(p_queue)==0:
            continue
        else:
            p_queue=sorted(p_queue, key=lambda x: x[BURST])
            pos_info=p_queue[0][PID]-1
            pos=processes.index(p_queue[0])

            timeline[t]=p_queue[0][PID]
            
            processes[pos][REMAINING]-=1
            if p_queue[0][REMAINING]==0:
                del processes[pos]
                processes_info[pos_info][EXIT]=t+1
                processes_info[pos_info][TURNAROUND]=processes_info[pos_info][EXIT]-processes_info[pos_info][ARRIVAL]
                processes_info[pos_info][WAIT]=processes_info[pos_info][TURNAROUND]-processes_info[pos_info][BURST]

    # Część z tabelą
    print("PID\tArrv.\tBurst\tExit\tTA\tWait")

    # Liczenie średniej i wyświetlenie tabeli
    ta_total=0
    w_total=0
    for i in processes_info:
        # czasy będą sumowane podczas wyświetlania tabeli
        ta_total+=i[TURNAROUND]     # Sumowanie czasów turnaround
        w_total+=i[WAIT]            # Sumowanie czasów oczekiwania
        for j in range(len(i)):     # Wyświetlanie tabeli
            if j!=REMAINING: print(i[j],end="\t")   # warunek if aby nie wyświetlać pozostałego czasu - wiadomo, że wynosi on 0
        print("")

    # Obliczanie średnich
    avg_ta=round(ta_total/len(processes_info),2)
    avg_w=round(w_total/len(processes_info),2)

    # Wyświetlanie średnich
    print("średnie: \t\t\t{}\t{}".format(avg_ta,avg_w))

    # Wyświetlanie osi czasu
    print("\n",timeline)

if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")
