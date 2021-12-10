# algorytm czasu procesora FIFO

from sys import exit

def do_fifo(processes):
    # Słowa kluczowe, pomagające w indeksowaniu tablic
    PID         = 0
    ARRIVAL     = 1
    BURST       = 2
    EXIT        = 3
    TURNAROUND  = 4
    WAIT        = 5
    REMAINING   = 6

    # Sortowanie procesów po czasie przybycia
    processes=sorted(processes, key=lambda x: x[1])
    
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
    completed=0

    # Pętla nanosząca procesy na oś czasu
    for i in range(len(timeline)):
        t+=1
        if t<processes[0][1]:   # jeżeli proces jeszcze nie dotarł, czekamy na niego - nanosimy pid 0
            continue
        else:
            timeline[t]=processes[0][PID]       # wpisanie na pozycji osi czasu PID-u procesu
            processes[0][REMAINING]-=1          # Zbicie pozostałego czasu o 1 jednostkę
            if processes[0][REMAINING]==0:      # Jeżeli proces się zakończył
                del processes[0]                # Usuń go z kolejki
                processes_info[completed][EXIT]=t+1     # Wpisanie czasu zakończenia procesu
                processes_info[completed][TURNAROUND]=processes_info[completed][EXIT]-processes_info[completed][ARRIVAL]    # Wpisanie czasu turnaround (od przybycia do zakończenia)
                processes_info[completed][WAIT]=processes_info[completed][TURNAROUND]-processes_info[completed][BURST]      # Wpisanie czasu oczekiwania procesu (od przybycia do rozpoczęcia wykonywania)
                completed+=1    # aby w tablicy processes_info było wiadomo na którym wpisie pracujemy

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

# gdyby ktoś przypadkiem uruchomił ten plik
if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")