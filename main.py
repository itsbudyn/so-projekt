# Moduły do tworzenia danych wejściowych
from cpu_create import create_processes
from mem_create import create_calls, create_frames

# Moduły do algorytmów czasu procesora
from cpu_fifo import cpu_do_fifo
from cpu_sjf import cpu_do_sjf

# Moduły do algorytmów zastępowania stron
from mem_fifo import mem_do_fifo
from mem_lfu import mem_do_lfu

# Pozostałe moduły
from keywords import clearscr
from sys import exit

# Menu główne programu
while True:
    clearscr()  # Czyszczenie okna terminala
    print( 
"""MENU GŁÓWNE
ALGORYTMY CZASÓW PROCESORA
    1. FIFO
    2. SJF - NIEWYWŁASZCZENIOWY

ALBORYTMY ZASTĘPOWANIA STRON
    3. FIFO - BEZ MODYFIKACJI
    4. LFU

0. WYJŚCIE
""")
    try:
        choice=int(input("Proszę wybrać opcję: "))  # Pobieranie wyboru od użytkownika
    except:
        choice=9
        
    clearscr()      # Czyszczenie ekranu
    match choice:   # Wybieranie obcji na podstawie podanej wartości
        case 1:
            processes=create_processes()
            cpu_do_fifo(processes)
        case 2:
            processes=create_processes()
            cpu_do_sjf(processes)
        case 3:
            calls=create_calls()
            frames=create_frames()
            mem_do_fifo(frames,calls)
        case 4:
            calls=create_calls()
            frames=create_frames()
            mem_do_lfu(frames,calls)
        case 0: exit(0)
        case default: print("Nie rozpoznano opcji!")
    input("Aby kontynuować, naciśnij enter... ")    # Po zakończeniu funkcji wstrzymuje program