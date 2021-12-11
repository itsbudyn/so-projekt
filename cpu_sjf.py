# Algorytm czasu procesora SJF
from keywords import *

def cpu_do_sjf(processes):
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
        p_queue=[]              # Kolejka procesów, gdzie będą sortowane po burst time
        for i in processes:
            if i[ARRIVAL] <= t: p_queue.append(i)   # Dodawanie procesów, które przybyły

        if len(p_queue)==0:     # Jeżeli żaden proces nie przybył
            continue
        else:
            p_queue=sorted(p_queue, key=lambda x: x[BURST])     # Sortowanie procesów w kolejce po czasie wykonania
            pos_info=p_queue[0][PID]-1          # Uzyskiwanie pozycji procesu w tabeli processes_info
            pos=processes.index(p_queue[0])     # Uzyskiwanie pozycji procesu w tabeli processes - różnica pomiędzy tą a poprzednią tabelą jest taka, że z tamtej usuwamy procesy

            timeline[t]=p_queue[0][PID]         # Nanoszenie PID-u procesu na oś czasu

            processes[pos][REMAINING]-=1            # Zbijanie pozostałego czasu wykonywania procesu o 1
            if p_queue[0][REMAINING]==0:            # Jeżeli czas procesu się skończył
                del processes[pos]                  # Usunięcie procesu z tabeli processes
                processes_info[pos_info][EXIT]=t+1  # Wpisanie czasu zakończenia procesu
                processes_info[pos_info][TURNAROUND]=processes_info[pos_info][EXIT]-processes_info[pos_info][ARRIVAL]   # Wpisanie czasu turnaround (od przybycia do zakończenia)
                processes_info[pos_info][WAIT]=processes_info[pos_info][TURNAROUND]-processes_info[pos_info][BURST]     # Wpisanie czasu oczekiwania procesu (od przybycia do rozpoczęcia wykonywania)
                
    # Część z tabelą
    print("PID\tArrv.\tBurst\tExit\tTA\tWait")

    # Liczenie średniej i wyświetlenie tabeli
    ta_total=0
    w_total=0
    for i in processes_info:
        # Czasy będą sumowane podczas wyświetlania tabeli
        ta_total+=i[TURNAROUND]     # Sumowanie czasów turnaround
        w_total+=i[WAIT]            # Sumowanie czasów oczekiwania
        for j in range(len(i)):     # Wyświetlanie tabeli
            if j!=REMAINING: print(i[j],end="\t")   # Warunek if aby nie wyświetlać pozostałego czasu - wiadomo, że wynosi on 0
        print("")

    # Obliczanie średnich
    avg_ta=round(ta_total/len(processes_info),2)
    avg_w=round(w_total/len(processes_info),2)

    # Wyświetlanie średnich
    print("średnie: \t\t\t{}\t{}".format(avg_ta,avg_w))

    # Wyświetlanie osi czasu
    print("\n0",timeline,max_time)

# Gdyby ktoś przypadkiem uruchomił ten plik
if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")
