from cpu_create import create_processes   # Moduły do tworzenia danych wejściowych
from mem_create import create_calls, create_frames
from cpu_fifo import cpu_do_fifo                    # Moduły do algorytmów czasu procesora
from cpu_sjf import cpu_do_sjf
from mem_fifo import mem_do_fifo                    # Moduły do algorytmów zastępowania stron
from mem_lfu import mem_do_lfu
from keywords import clearscr                       # Pozostałe moduły
from sys import exit
from copy import deepcopy   # Ten moduł jest wymagany do kopiowania listy procesów w przypadku
                            # uruchamiania obu algorytmów - z jakiegoś powodu nie jestem w stanie
                            # utworzyć kopii jakimikolwiek wbudowanymi metodami ani slicingiem
                            # [:], wobec czego jestem zmuszony użyć copy.deepcopy()

manual=True     # Czy użytkownik ma ręcznie definiować dane, czy mamy generować za niego?

while True:     # Menu główne programu
    clearscr()  # Czyszczenie okna terminala

    # Linijka wskazująca, czy dane będą generowane automatycznie, czy ręcznie
    modeselect=""
    if manual: modeselect="\t<RĘCZNE>\tAUTOMATYCZNE"
    else: modeselect="\tRĘCZNE\t<AUTOMATYCZNE>"

    print( 
"""MENU GŁÓWNE
ALGORYTMY CZASÓW PROCESORA
    1. FCFS / FIFO\t2. SJF - NIEWYWŁASZCZENIOWY\t3. URUCHOM OBA

ALBORYTMY ZASTĘPOWANIA STRON
    4. FIFO - BEZ MODYFIKACJI\t5. LFU\t6. URUCHOM OBA

7. PRZEŁĄCZ TRYB WPISYWANIA DANYCH: {}

0. WYJŚCIE
""".format(modeselect))
    try: choice=int(input("Proszę wybrać opcję: "))  # Pobieranie wyboru od użytkownika
    except ValueError: choice=-1    # W przypadku podania nielegalnej opcji    

    clearscr()      # Czyszczenie ekranu
    match choice:   # Wybieranie obcji na podstawie podanej wartości
        case 1: cpu_do_fifo(create_processes(manual))
        case 2: cpu_do_sjf(create_processes(manual))
        case 3:
            processes_fifo=create_processes(manual)
            processes_sjf=deepcopy(processes_fifo)
            cpu_do_fifo(processes_fifo)
            cpu_do_sjf(processes_sjf)
            del processes_fifo, processes_sjf
        case 4: mem_do_fifo(create_frames(),create_calls(manual))
        case 5: mem_do_lfu(create_frames(),create_calls(manual))
        case 6:
            frames=create_frames()
            calls_fifo=create_calls(manual)
            calls_lfu=deepcopy(calls_fifo)
            mem_do_fifo(frames,calls_fifo)
            mem_do_lfu(frames,calls_lfu)
            del calls_fifo, calls_lfu
        case 7:
            if manual: manual=False
            else: manual=True
            print("Przełączono tryb wpisywania danych")
        case 0: exit(0)
        case default: print("Nie rozpoznano opcji!")
    input("Aby kontynuować, naciśnij enter... ")    # Po zakończeniu funkcji wstrzymuje program