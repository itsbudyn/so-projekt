import os

# Słowa kluczowe, pomagające w indeksowaniu tablic
PID         = 0
ARRIVAL     = 1
BURST       = 2
EXIT        = 3
TURNAROUND  = 4
WAIT        = 5
REMAINING   = 6

# Funkcja kończąca działanie programu, która też drukuje wiadomość odpowiednią do błędu, jaki popełnił użytkownik
def exit_err(msg:str):
    print("Błąd:",msg)
    exit(-1)

def clearscr(): # Funkcja czyszcząca okno terminalu, działająca na Windowsie i POSIX
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":  # Gdyby ktoś przypadkiem uruchomił ten plik
    print("Proszę uruchomić plik main.py")