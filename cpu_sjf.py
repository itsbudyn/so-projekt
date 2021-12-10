# algorytm czasu procesora FIFO

from sys import exit
from keywords import *

def do_sjf(processes):
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
        p_queue=[]              # kolejka procesów, gdzie będą sortowane po burst time
        for i in processes:
            if i[ARRIVAL] <= t: p_queue.append(i)   # dodawanie procesów, które przybyły

        if len(p_queue)==0:     # jeżeli żaden proces nie przybył
            continue
        else:
            p_queue=sorted(p_queue, key=lambda x: x[BURST])     # sortowanie procesów w kolejce po czasie wykonania
            pos_info=p_queue[0][PID]-1          # uzyskiwanie pozycji procesu w tabeli processes_info
            pos=processes.index(p_queue[0])     # uzyskiwanie pozycji procesu w tabeli processes - różnica pomiędzy tą a poprzednią tabelą jest taka, że z tamtej usuwamy procesy

            timeline[t]=p_queue[0][PID]         # nanoszenie PID-u procesu na oś czasu

            processes[pos][REMAINING]-=1        # zbijanie pozostałego czasu wykonywania procesu o 1
            if p_queue[0][REMAINING]==0:        # jeżeli czas procesu się skończył
                del processes[pos]              # usunięcie procesu z tabeli processes
                processes_info[pos_info][EXIT]=t+1  # Wpisanie czasu zakończenia procesu
                processes_info[pos_info][TURNAROUND]=processes_info[pos_info][EXIT]-processes_info[pos_info][ARRIVAL]   # Wpisanie czasu turnaround (od przybycia do zakończenia)
                processes_info[pos_info][WAIT]=processes_info[pos_info][TURNAROUND]-processes_info[pos_info][BURST]     # Wpisanie czasu oczekiwania procesu (od przybycia do rozpoczęcia wykonywania)
                
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
    print("\n0",timeline,max_time)

if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")
