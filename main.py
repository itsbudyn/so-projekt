from cpu_create import create_processes
from cpu_fifo import do_fifo
from cpu_sjf import do_sjf
from sys import exit
import os

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
            do_fifo(processes)
        case 2:
            processes=create_processes()
            do_sjf(processes)
        case 0:
            exit(0)
    input("Aby kontynuować, naciśnij enter... ")