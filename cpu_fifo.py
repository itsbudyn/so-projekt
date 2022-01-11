# Algorytm czasu procesora FIFO
from keywords import *

def cpu_do_fifo(processes):
    processes=sorted(processes, key=lambda x: x[ARRIVAL])   # Sortowanie procesów po czasie przybycia
    processes_info=processes[:] # Utwórz kopię kolejki procesów, potrzebne do tabeli końcowej

    # Obliczanie czasu wykonywania algorytmu
    max_time=0
    for i in processes: 
        max_time+=i[BURST]
        max_time+=i[ARRIVAL]

    timeline=[0 for i in range(max_time)]   # Budowa osi czasu na podstawie czasu wykonywania algorytmu

    # Przygotowanie do naniesienia procesów na oś czasu
    t=-1
    completed=0

    for i in range(len(timeline)):  # Pętla nanosząca procesy na oś czasu
        t+=1
        if len(processes)==0: break
        if t>=processes[0][1]:   # Jeżeli proces dotarł - czas na osi czasu jesst większy bądź równy czasu przybycia
            timeline[t]=processes[0][PID]       # Wpisanie na pozycji osi czasu PID-u procesu
            processes[0][REMAINING]-=1          # Zbicie pozostałego czasu o 1 jednostkę
            if processes[0][REMAINING]==0:      # Jeżeli proces się zakończył
                del processes[0]                # Usuń go z kolejki
                processes_info[completed][EXIT]=t+1     # Wpisanie czasu zakończenia procesu
                processes_info[completed][TURNAROUND]=processes_info[completed][EXIT]-processes_info[completed][ARRIVAL]    # Wpisanie czasu turnaround (od przybycia do zakończenia)
                processes_info[completed][WAIT]=processes_info[completed][TURNAROUND]-processes_info[completed][BURST]      # Wpisanie czasu oczekiwania procesu (od przybycia do rozpoczęcia wykonywania)
                completed+=1    # Aby w tablicy processes_info było wiadomo na którym wpisie pracujemy

    process_table(processes_info,timeline,max_time)     # Wyświetlenie tabeli

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik