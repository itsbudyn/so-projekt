from sys import exit
from cpu_create import create_processes
from cpu_fifo import do_fifo
from sys import exit
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print( 
"""MENU GŁÓWNE
1. FIFO

0. WYJŚCIE
""")
    choice=int(input("Proszę wybrać opcję: "))
    match choice:
        case 1:
            processes=create_processes()
            do_fifo(processes)
        case 0:
            exit(0)
    input("Aby kontynuować, naciśnij enter... ")