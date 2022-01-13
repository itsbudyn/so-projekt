# Moduł pomagający w tworzeniu tablicy ramek
from random import randint

def create_frames():    # Pobieranie wartości liczbowej, która mówi na ilu ramkach będziemy pracować
    try: 
        frames=int(input("Podaj ilość ramek (min=1): "))    # Pobieranie ilości ramek
        assert frames > 0
    except ValueError: 
        print("Wartość nie była liczbą całkowitą (int)!")    # Niedopuszczenie do uruchomienia algorytmu w przypadku podania wartości innej niż int
        return
    except AssertionError:
        print("Wartość nie może być mniejsza od zera!")     # Niedopuszczenie do uruchomienia algorytmu w przypadku podania wartości mniejszej bądź równej 0
        return
    return frames

def create_calls_manual():     # Tworzenie tablicy odwołań
    page_calls=[]
    try: page_calls=list(map(int,str(input("Podaj odwołania: ")).split(" ")))       # Dzielenie podanych wartości przez spacje i wpisywanie ich jako int
    except ValueError: 
        print("Jedna z wartości nie była liczbą całkowitą (int)!")  # Niedopuszczenie do uruchomienia algorytmu w przypadku wartości innej niż int 
        return

    return page_calls   # Zwrot stworzonej tablicy

def create_calls_auto(page_count:int,max_page_pid:int): return list(randint(1,max_page_pid) for i in range(page_count))

def create_calls(manual:bool):
    if manual: return create_calls_manual()     # Czy użytkownik stworzy tablicę odwołań ręcznie, czy pomoże w ich generowaniu
    else: 
        while True:
            try:
                # Przyjęcie wartości page_count i max_page_pid, słowo kluczowe assert
                # wywoła wyjątek, który zostanie obsłużony, i użytkownikowi zostanie
                # podany komunikat o błędzie, oraz dostanie kolejną szansę na wpisanie
                # danych.
                page_count=int(input("Podaj ilość stron (min=1): "))
                assert page_count > 0
                max_page_pid=int(input("Podaj ilość unikalnych stron (min=1): "))
                assert max_page_pid > 0
            except ValueError: print("Wartość nie była liczbą całkowitą (int)!")
            except AssertionError: print("Wartość nie może być mniejsza od jeden!")
            else: return create_calls_auto(page_count,max_page_pid)

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik