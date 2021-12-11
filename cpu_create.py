from sys import exit
from keywords import *

def invalid_process_err(msg:str):
    print(msg)
    exit(-1)

def create_processes():
    processes=[]
    arriv_times=list(map(int,str(input("Podaj czasy przybycia dla procesów: ")).split(" ")))
    burst_times=list(map(int,str(input("Podaj czasy wykonywania dla procesów: ")).split(" ")))

    for i in arriv_times:
        if i<0: invalid_process_err("Błąd: Co najmniej jeden z procesów miał czas przybycia mniejszy od 0!")

    for i in burst_times:
        if i<=0: invalid_process_err("Błąd: Co najmniej jeden z procesów miał czas wykonaia mniejszy bądź równy 0!")

    if len(burst_times) != len(arriv_times):
        invalid_process_err("Długości tablic nie są takie same!")

    for i in range(len(burst_times)):
        # PID , arrival , burst , Exit , TurnAround, Wait
        process=[0,0,0,0,0,0,0]
        process[PID]=i+1
        process[ARRIVAL]=arriv_times[i]
        process[BURST]=burst_times[i]
        process[REMAINING]=process[BURST]
        processes.append(process)
    return processes

if __name__ == "__main__":
    print("Proszę uruchomić plik main.py")