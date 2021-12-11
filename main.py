from cpu_create import create_processes
from mem_create import create_calls, create_frames
from cpu_fifo import cpu_do_fifo
from cpu_sjf import cpu_do_sjf
from sys import exit
import os

from mem_fifo import mem_do_fifo

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
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
    choice=int(input("Proszę wybrać opcję: "))
    match choice:
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
            pass
        case 0:
            exit(0)
    input("Aby kontynuować, naciśnij enter... ")