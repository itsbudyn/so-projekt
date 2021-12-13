# Moduł pomagający w tworzeniu tablicy ramek
from keywords import exit_err

def create_calls():     # Tworzenie tablicy odwołań
    page_calls=[]
    try: page_calls=list(map(int,str(input("Podaj odwołania: ")).split(" ")))       # Dzielenie podanych wartości przez spacje i wpisywanie ich jako int
    except ValueError: exit_err("Jedna z wartości nie była liczbą całkowitą (int)!")# Zakończenie programu w przypadku wartości innej niż int 

    return page_calls   # Zwrot stworzonej tablicy

def create_frames():    # Pobieranie wartości liczbowej, która mówi na ilu ramkach będziemy pracować
    try: frames=int(input("Podaj ilość ramek: "))    # Pobieranie ilości ramek
    except ValueError: exit_err("Wartość nie była liczbą całkowitą (int)!")    # Zakończenie programu w przypadku podania wartości innej niż int

    if frames<=0: exit_err("Wartość nie może być mniejsza od zera!")     # Zakończenie programu w przypadku podania wartości mniejszej bądź równej 0
    return frames

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik