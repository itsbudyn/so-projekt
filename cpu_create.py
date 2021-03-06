# Moduł pomagający w tworzeniu tablicy symulowanych procesów
from keywords import *
from random import randint

def export_processes(processes):
    filename=str(input("Nazwa pliku .txt? (pozostawić puste, aby nie generować): "))    # Zapytanie o plik .TXT
    if filename:    # W razie zgody
        try: 
            if not os.path.isdir("in"): os.mkdir("in")    # Próba utworzenia katalogu out, jeżeli ten nie istnieje
        except Exception as err: print("Nie można utworzyć katalogu in, ponieważ wystąpił nieoczekiwany błąd {}. Sprawdź prawa do zapisu, i spróbuj ponownie.".format(err))    # W przypadku błędu informujemy użytkownika i przerywamy zapis
        else:
            try:
                f=open("./in/{}.txt".format(filename),"w",encoding="UTF-8")    # Utworzenie, bądź otworzenie istniejącego pliku o podanej nazwie
                strbuffer=["",""]       # Przygotowanie bufora tekstowego, do zapisania do pliku
                for i in processes:     # Iteracja przez procesy
                    strbuffer[0]+="{} ".format(i[ARRIVAL])  # Pobranie wszystkich czasów przybycia
                    strbuffer[1]+="{} ".format(i[BURST])    # Pobranie wszystkich czasów wykonywania
                strbuffer[0]=strbuffer[0][:-1]      # Wycięcie zbędnych spacji na końcu
                strbuffer[1]=strbuffer[1][:-1]
                # Zapis do pliku
                f.write(strbuffer[0])
                f.write("\n")      
                f.write(strbuffer[1])
                f.write("\n")
                f.close()       # Zamknięcie pliku po zakończonym działaniu
            except Exception as err: print("Nie można utworzyć pliku, ponieważ wystąpił nieoczekiwany błąd {}. Sprawdź prawa do zapisu, i spróbuj ponownie.".format(err))   # W razie błędu z zapisem do pliku
            else: print("Zapisano!")

def create_processes_manual():
    processes=[]    # tworzenie nowej tabeli, gdzie będą dodane procesy
    try:
        arriv_times=list(map(int,str(input("Podaj czasy przybycia dla procesów:\t")).split(" ")))        # Pobieranie czasów przybycia
        burst_times=list(map(int,str(input("Podaj czasy wykonywania dla procesów:\t")).split(" ")))      # Pobieranie czasów wykonywania
    except ValueError:  # Obsługa wyjątku ValueError - kiedy zostanie podane coś innego niż int
        print("Jedna z wartości nie była liczbą całkowitą (int)!")
        return

    if len(burst_times) != len(arriv_times):    # Nie dopuść do uruchomienia algorytmu, jeżeli ilość czasów przybycia będzie rózna od ilości czasów wykonywania
        print("Długości tablic nie są takie same!")
        return

    for i in range(len(burst_times)):  # Nie dopuść do uruchomienia algorytmu, jeżeli zostanie podana gdzieś nieprawidłowa wartość
        if arriv_times[i]<0: 
            print("Co najmniej jeden z procesów miał czas przybycia mniejszy od 0!")
            return
        if burst_times[i]<=0: 
            print("Co najmniej jeden z procesów miał czas wykonaia mniejszy od 1!")
            return

    # Dodawanie procesów do tablicy
    for i in range(len(burst_times)):
        # PID , Arrival , Burst , Exit , TurnAround, Wait
        process             =[0,0,0,0,0,0,0]# Tworzenie pustego procesu
        process[PID]        =i+1            # Nadawanie PID-u
        process[ARRIVAL]    =arriv_times[i] # Nadawanie czasu przybycia
        process[BURST]      =burst_times[i] # Nadawanie czasu wykonania
        process[REMAINING]  =process[BURST] # Nadawanie pozostałego czasu - tutaj równego czasowi wykonywaniea
        processes.append(process)           # Dodawanie procesu do tabeli

    processes=sorted(processes, key=lambda x: x[ARRIVAL])   # Sortowanie procesów po czasie przybycia
    export_processes(processes)
    return processes        # Koniec funkcji - zwracanie tabeli

def create_processes_auto(count:int,arrival_max:int,burst_max:int):
    processes=[]    # tworzenie nowej tabeli, gdzie będą dodane procesy
    
    for i in range(count):
        # PID , Arrival , Burst , Exit , TurnAround, Wait
        process             =[0,0,0,0,0,0,0]        # Tworzenie pustego procesu
        process[PID]        =i+1                    # Nadawanie PID-u
        process[ARRIVAL]    =randint(0,arrival_max) # Nadawanie czasu przybycia
        process[BURST]      =randint(1,burst_max)   # Nadawanie czasu przybycia
        process[REMAINING]  =process[BURST]         # Nadawanie pozostałego czasu - tutaj równego czasowi wykonywaniea
        processes.append(process)           # Dodawanie procesu do tabeli

    processes=sorted(processes, key=lambda x: x[ARRIVAL])   # Sortowanie procesów po czasie przybycia
    export_processes(processes)
    return processes        # Koniec funkcji - zwracanie tabeli

def create_processes(manual:bool): 
    if manual: return create_processes_manual()     # Czy użytkownik stworzy procesy ręcznie, czy pomoże w ich generowaniu
    else: 
        while True:
            try: 
                # Pobieramy wartości count, max_arrival, max_burst
                # assert wywoła wyjątek w przypadku podania wartości
                # spoza zakresu, który zostanie złapany, po czym zostanie
                # wydrukowany odpowiedni komunikat, a użytkownik dostanie
                # kolejną szansę na wprowadzenie danych.
                count=int(input("Ile procesów utworzyć? (min=0) "))
                assert count        > 0
                max_arrival=int(input("Maksymalny zakres czasów przybycia? (min=0) "))
                assert max_arrival  >= 0
                max_burst=int(input("Maksymalny czas wykonywania? (min=1) "))
                assert max_burst    > 0
            except ValueError: print("Wartość nie jest liczbą całkowitą!")
            except AssertionError: print("Wartość wykracza poza zakres")
            else: return create_processes_auto(count,max_arrival,max_burst)     # W przypadku poprawności podanych danych

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik