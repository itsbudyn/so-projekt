# Słowa kluczowe, pomagające w indeksowaniu tablic
PID         = 0
ARRIVAL     = 1
BURST       = 2
EXIT        = 3
TURNAROUND  = 4
WAIT        = 5
REMAINING   = 6

def exit_err(msg:str):
    print("Błąd:",msg)
    exit(-1)

if __name__ == "__main__":
    print("Proszę uruchomić plik main.py")