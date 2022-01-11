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

def clearscr(): os.system('cls' if os.name == 'nt' else 'clear')    # Funkcja czyszcząca okno terminalu, działająca na Windowsie i POSIX

def process_table(processes_info,timeline,max_time):    # Część z tabelą
    csvbuffer="PID,Czas przybycia,Czas wykonywania,Czas zakończenia,Czas istnienia,Czas Oczekiwania\n"
    print("PID\tArrv.\tBurst\tExit\tTA\tWait")

    # Liczenie średniej i wyświetlenie tabeli
    ta_total=0
    w_total=0
    for i in processes_info:
        # Czasy będą sumowane podczas wyświetlania tabeli
        ta_total+=i[TURNAROUND]     # Sumowanie czasów turnaround
        w_total+=i[WAIT]            # Sumowanie czasów oczekiwania
        for j in range(len(i)):     # Wyświetlanie tabeli
            if j!=REMAINING:        # Warunek if aby nie wyświetlać pozostałego czasu - wiadomo, że wynosi on 0
                print(i[j],end="\t")
                csvbuffer+="{},".format(i[j])
            else: csvbuffer=csvbuffer[:-1]
        csvbuffer+="\n"
        print("")

    # Obliczanie średnich
    avg_ta=round(ta_total/len(processes_info),2)
    avg_w=round(w_total/len(processes_info),2)

    print("średnie: \t\t\t{}\t{}".format(avg_ta,avg_w)) # Wyświetlanie średnich
    print("\n0",timeline,max_time)  # Wyświetlanie osi czasu
    
    while timeline[-1]==0: del timeline[-1]     # Usuwanie ciągu zerowych PID-ów (jeżeli występuje) na końcu osi czasu
    max_time=len(timeline)      # Ustalanie nowego czasu maksymalnego

    process_order(timeline)     # Wyświetlenie kolejności procesów

    filename=str(input("Nazwa pliku .csv? (pozostawić puste, aby nie generować): "))
    if filename:
        if not os.path.isdir("out"): os.mkdir("out") 
        try:
            f=open("./out/{}.csv".format(filename),"w",encoding="UTF-8")
            f.write(csvbuffer)
            f.close()
        except Exception as err:
            print("Wystąpił nieoczekiwany błąd {}. Sprawdź prawa do zapisu, i spróbuj ponownie.".format(err))
        else:
            print("Zapisano!")

def process_order(timeline):
    order=timeline[:]
    while 0 in order: order.remove(0)
    for i in order[:]: 
        if order.count(i)>1: order.remove(i)
    print("\nKolejnośc procesów: ")
    print(order)

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik