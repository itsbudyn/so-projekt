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

def process_table(processes_info,timeline,max_time):    # Część z tabelą
    print("PID\tArrv.\tBurst\tExit\tTA\tWait")

    # Liczenie średniej i wyświetlenie tabeli
    ta_total=0
    w_total=0
    for i in processes_info:
        # Czasy będą sumowane podczas wyświetlania tabeli
        ta_total+=i[TURNAROUND]     # Sumowanie czasów turnaround
        w_total+=i[WAIT]            # Sumowanie czasów oczekiwania
        for j in range(len(i)):     # Wyświetlanie tabeli
            if j!=REMAINING: print(i[j],end="\t")   # Warunek if aby nie wyświetlać pozostałego czasu - wiadomo, że wynosi on 0
        print("")

    # Obliczanie średnich
    avg_ta=round(ta_total/len(processes_info),2)
    avg_w=round(w_total/len(processes_info),2)

    print("średnie: \t\t\t{}\t{}".format(avg_ta,avg_w)) # Wyświetlanie średnich

    print("\n0",timeline,max_time)  # Wyświetlanie osi czasu

if __name__ == "__main__":  # Gdyby ktoś przypadkiem uruchomił ten plik
    print("Proszę uruchomić plik main.py")