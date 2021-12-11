import os

# Słowa kluczowe, pomagające w indeksowaniu tablic
PID         = 0
ARRIVAL     = 1
BURST       = 2
EXIT        = 3
TURNAROUND  = 4
WAIT        = 5
REMAINING   = 6

# Funkcja kończąca działanie programu, która też drukuję wiadomość
# odpowiednią do błędu, jaki popełnił użytkownik
def exit_err(msg:str):
    print("Błąd:",msg)
    exit(-1)

# Funkcja czyszcząca okno terminalu, działająca na Windowsie i POSIX
def clearscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gdyby ktoś przypadkiem uruchomił ten plik
if __name__ == "__main__":
    print("Proszę uruchomić plik main.py")