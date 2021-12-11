from keywords import *

def create_processes():
    processes=[]
    try:
        arriv_times=list(map(int,str(input("Podaj czasy przybycia dla procesów: ")).split(" ")))
        burst_times=list(map(int,str(input("Podaj czasy wykonywania dla procesów: ")).split(" ")))
    except ValueError:
        exit_err("Jedna z wartości nie była liczbą całkowitą (int)!")

    if len(burst_times) != len(arriv_times):
        exit_err("Długości tablic nie są takie same!")

    for i in len(burst_times):
        if arriv_times[i]<0: exit_err("Co najmniej jeden z procesów miał czas przybycia mniejszy od 0!")
        if burst_times[i]<=0: exit_err("Co najmniej jeden z procesów miał czas wykonaia mniejszy bądź równy 0!")

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