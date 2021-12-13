# Moduł pomagający w tworzeniu tablicy symulowanych procesów
from keywords import *

def create_processes():
    processes=[]    # tworzenie nowej tabeli, gdzie będą dodane procesy
    try:
        arriv_times=list(map(int,str(input("Podaj czasy przybycia dla procesów:\t")).split(" ")))        # Pobieranie czasów przybycia
        burst_times=list(map(int,str(input("Podaj czasy wykonywania dla procesów:\t")).split(" ")))      # Pobieranie czasów wykonywania
    except ValueError: exit_err("Jedna z wartości nie była liczbą całkowitą (int)!")   # Obsługa wyjątku ValueError - kiedy zostanie podane coś innego niż int

    if len(burst_times) != len(arriv_times): exit_err("Długości tablic nie są takie same!") # Zakończ działanie programu, jeżeli ilość czasów przybycia będzie rózna od ilości czasów wykonywania

    for i in range(len(burst_times)):  # Zakończ działanie programu, jeżeli zostanie podana gdzieś nieprawidłowa wartość
        if arriv_times[i]<0: exit_err("Co najmniej jeden z procesów miał czas przybycia mniejszy od 0!")
        if burst_times[i]<=0: exit_err("Co najmniej jeden z procesów miał czas wykonaia mniejszy bądź równy 0!")

    # Dodawanie procesów do tablicy
    for i in range(len(burst_times)):
        # PID , Arrival , Burst , Exit , TurnAround, Wait
        process=[0,0,0,0,0,0,0]             # Tworzenie pustego procesu
        process[PID]=i+1                    # Nadawanie PID-u
        process[ARRIVAL]=arriv_times[i]     # Nadawanie czasu przybycia
        process[BURST]=burst_times[i]       # Nadawanie czasu wykonania
        process[REMAINING]=process[BURST]   # Nadawanie pozostałego czasu - tutaj równego czasowi wykonywaniea
        processes.append(process)           # Dodawanie procesu do tabeli
    return processes        # Koniec funkcji - zwracanie tabeli

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik