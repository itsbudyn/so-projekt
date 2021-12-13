from cpu_create import create_processes             # Moduły do tworzenia danych wejściowych
from mem_create import create_calls, create_frames
from cpu_fifo import cpu_do_fifo                    # Moduły do algorytmów czasu procesora
from cpu_sjf import cpu_do_sjf
from mem_fifo import mem_do_fifo                    # Moduły do algorytmów zastępowania stron
from mem_lfu import mem_do_lfu
from keywords import clearscr                       # Pozostałe moduły
from sys import exit

while True:     # Menu główne programu
    clearscr()  # Czyszczenie okna terminala
    print( 
"""MENU GŁÓWNE
ALGORYTMY CZASÓW PROCESORA
    1. FCFS / FIFO
    2. SJF - NIEWYWŁASZCZENIOWY

ALBORYTMY ZASTĘPOWANIA STRON
    3. FIFO - BEZ MODYFIKACJI
    4. LFU

0. WYJŚCIE
""")
    try: choice=int(input("Proszę wybrać opcję: "))  # Pobieranie wyboru od użytkownika
    except: choice=9    # W przypadku podania nielegalnej opcji    

    clearscr()      # Czyszczenie ekranu
    match choice:   # Wybieranie obcji na podstawie podanej wartości
        case 1: cpu_do_fifo(create_processes())
        case 2: cpu_do_sjf(create_processes())
        case 3: mem_do_fifo(create_frames(),create_calls())
        case 4: mem_do_lfu(create_frames(),create_calls())
        case 0: exit(0)
        case default: print("Nie rozpoznano opcji!")
    input("Aby kontynuować, naciśnij enter... ")    # Po zakończeniu funkcji wstrzymuje program