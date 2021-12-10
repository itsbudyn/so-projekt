from sys import exit
from keywords import *

def create_processes():
    processes=[]
    arriv_times=list(map(int,str(input("Podaj czasy przybycia dla procesów: ")).split(" ")))
    burst_times=list(map(int,str(input("Podaj czasy wykonywania dla procesów: ")).split(" ")))

    if len(burst_times) != len(arriv_times):
        print("Długości tablic nie są takie same!")
        exit(-1)

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