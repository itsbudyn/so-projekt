import os

# Słowa kluczowe, pomagające w indeksowaniu tablic
PID         = 0
ARRIVAL     = 1
BURST       = 2
EXIT        = 3
TURNAROUND  = 4
WAIT        = 5
REMAINING   = 6

def clearscr(): os.system('cls' if os.name == 'nt' else 'clear')    # Funkcja czyszcząca okno terminalu, działająca na Windowsie i POSIX

def process_table(processes_info,timeline,max_time):    # Część z tabelą i eksportem do .CSV
    processes_info=sorted(processes_info, key=lambda x: x[PID]) # Sortowanie tabeli końcowej po PID-zie    
    csvbuffer="PID,Czas przybycia,Czas wykonywania,Czas zakończenia,Czas istnienia,Czas Oczekiwania\n"  # Pierwsza linijka pliku .CSV

    print("PID\tArrv.\tBurst\tExit\tTA\tWait")  # Pierwsza linijka drukowanej tabeli

    # Liczenie średniej i wyświetlenie tabeli
    ta_total=0
    w_total=0
    for i in processes_info:
        # Czasy będą sumowane podczas wyświetlania tabeli
        ta_total+=i[TURNAROUND]     # Sumowanie czasów turnaround
        w_total+=i[WAIT]            # Sumowanie czasów oczekiwania
        for j in range(len(i)):     # Wyświetlanie tabeli
            if j!=REMAINING:        # Warunek if aby nie wyświetlać pozostałego czasu - wiadomo, że wynosi on 0
                print(i[j],end="\t")    # Drukowanie elementów tabeli
                csvbuffer+="{},".format(i[j])   # Dopisywanie elementów tabeli do bufora .CSV
            else: csvbuffer=csvbuffer[:-1]      # Wycięcie ostatniego przecinka z linijki
        csvbuffer+="\n"     # Nowy wiersz tabeli w buforze .CSV
        print("")

    # Obliczanie średnich
    avg_ta=round(ta_total/len(processes_info),2)
    avg_w=round(w_total/len(processes_info),2)

    while timeline[-1]==0: del timeline[-1]     # Usuwanie ciągu zerowych PID-ów (jeżeli występuje) na końcu osi czasu
    max_time=len(timeline)      # Ustalanie nowego czasu maksymalnego

    print("średnie: \t\t\t{}\t{}".format(avg_ta,avg_w)) # Wyświetlanie średnich
    print("\n0",timeline,max_time)  # Wyświetlanie osi czasu

    process_order(timeline)     # Wyświetlenie kolejności procesów

    csvbuffer+="ŚREDNIA,,,,{},{}".format(avg_ta,avg_w)
    csvexport(csvbuffer)    # Eksport tabeli procesów do .CSV
    del csvbuffer   # Usunięcie niepotrzebnego buforu

def process_order(timeline):    # Otrzymywanie kolejności występujących procesów na podstawie osi czasu
    order=timeline[:]           # Tworzenie kopii tablicy
    while 0 in order: order.remove(0)   # Usuwanie PID-ów o wartości 0
    for i in order[:]:      # Iteracja przez tablicę
        if order.count(i)>1: order.remove(i)    # Usuwanie wartości występujących więcej niż raz
    print("\nKolejnośc procesów: ",order)       # Drukowanie gotowej tabliccy

def csvexport(csvbuffer):
    filename=str(input("Nazwa pliku .csv? (pozostawić puste, aby nie generować): "))    # Zapytanie o plik .CSV
    if filename:    # W razie zgody
        try: 
            if not os.path.isdir("out"): os.mkdir("out")    # Próba utworzenia katalogu out, jeżeli ten nie istnieje
        except Exception as err: print("Nie można utworzyć katalogu out, ponieważ wystąpił nieoczekiwany błąd {}. Sprawdź prawa do zapisu, i spróbuj ponownie.".format(err))    # W przypadku błędu informujemy użytkownika i przerywamy zapis
        else:
            try:
                f=open("./out/{}.csv".format(filename),"w",encoding="UTF-8")    # Utworzenie, bądź otworzenie istniejącego pliku o podanej nazwie
                f.write(csvbuffer)      # Zapis do pliku
                f.close()       # Zamknięcie pliku po zakończonym działaniu
            except Exception as err: print("Nie można utworzyć pliku, ponieważ wystąpił nieoczekiwany błąd {}. Sprawdź prawa do zapisu, i spróbuj ponownie.".format(err))   # W razie błędu z zapisem do pliku
            else: print("Zapisano!")

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik