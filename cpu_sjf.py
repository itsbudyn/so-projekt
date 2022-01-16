# Algorytm czasu procesora SJF
from keywords import *

def get_pid_pos(pid:int,arr):   # Uzyskiwanie PID-u procesu z dowolnej tabeli
    for i in arr:   # Iteracja przez tabelę
        if i[PID]==pid: return arr.index(i) # W przypadku wystąpienia - zwrot indeksu tabeli

def cpu_do_sjf(processes):
    if processes==None:     # W przypadku, gdy tablica processes nie istnieje - to się dzieje w przypadku złego wprowadzenia danych
        print("Algorytm nie może zostać wykonany.")
        return
    else: print("POCZĄTEK ALGORYTMU SJF")

    processes_info=processes[:] # Utwórz kopię kolejki procesów, potrzebne do tabeli końcowej

    # Obliczanie czasu wykonywania wszystkich procesów
    max_time=0
    for i in processes: 
        max_time+=i[BURST]
        max_time+=i[ARRIVAL]

    timeline=[0 for i in range(max_time)]   # Budowa osi czasu na podstawie czasu wykonywania algorytmu
    
    t=-1    # Przygotowanie do naniesienia procesów na oś czasu

    currentproc=False       # Obecny proces - Narazie żaden, za moment zobaczymy, który proces powinien być obsłużony najpierw
    p_queue=[]              # Kolejka procesów - Przechowuje tylko te procesy, które przybyły (i są niewykonane)
    for i in range(len(timeline)):  # Pętla nanosząca procesy na oś czasu
        t+=1

        if len(processes)==0: break # Jeżeli nie ma procesów do obsłużenia - wyjdź z pętli

        sort_again=False        # Flaga do ponownego sortowania tablicy
        if not currentproc:     # Jeżeli żaden proces nie jest obecny
            for j in processes:     # Iteracja przez tablice procesów
                if j not in p_queue and j[ARRIVAL] <= t:    # Jeżeli natkniemy się na proces, którego nie ma w kolejce, a czas przybycia minął (lub teraz jest)
                    p_queue.append(j)       # Dodajemy proces do końca tabeli
                    sort_again=True         # Ustawiamy flagę do ponownego sortowania
            if sort_again: p_queue=sorted(p_queue, key=lambda x: x[BURST])  # Kiedy flaga do ponownego sortowania jest ustawiona - sortujemy kolejkę po burst time
            if len(p_queue)!=0: currentproc=p_queue[0]      # Obecnym procesem zostaje pierwszy proces w kolejce

        if currentproc:     # Jeżeli mamy obecny proces
            timeline[t]=currentproc[PID]    # Nanosimy PID obecnego procesu na oś czasu
            currentproc[REMAINING]-=1       # Dekrementujemy pozostały czas obecnego procesu
            if currentproc[REMAINING]==0:   # Jeżeli proces zakończył swoją pracę
                del processes[get_pid_pos(currentproc[PID],processes)]  # Usuwamy proces z pierwotnej tabeli procesów
                del p_queue[get_pid_pos(currentproc[PID],p_queue)]      # Usuwamy proces z kolejki
                pos=get_pid_pos(currentproc[PID],processes_info)        # Otrzymujemy pozycję procesu w tabeli processes_info
                processes_info[pos][EXIT]=t+1     # Wpisanie czasu zakończenia procesu
                processes_info[pos][TURNAROUND]=processes_info[pos][EXIT]-processes_info[pos][ARRIVAL]    # Wpisanie czasu turnaround (od przybycia do zakończenia)
                processes_info[pos][WAIT]=processes_info[pos][TURNAROUND]-processes_info[pos][BURST]      # Wpisanie czasu oczekiwania procesu (od przybycia do rozpoczęcia wykonywania)
                currentproc=False   # Żaden proces nie jest teraz obecny

    process_table(processes_info,timeline,max_time)     # Wyświetlenie tabeli
    print("KONIEC ALGORYTMU SJF")

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik