from keywords import csvexport
# Algorytm zastępowania stron LFU

# Słowa kluczowe
PID     = 0
FREQ    = 1

def get_least_used_pid(freqs_arr):  # Funkcja do otrzymywania PID-u strony najrzadziej używanej
    min_pid=freqs_arr[0][PID]       # Przygotowanie do znalezienia minimum - przyjmowanie wartości z pierwszego elementu tabeli jako wartości początkowe
    min_freq=freqs_arr[0][FREQ]
    for i in freqs_arr:             # Iteracja przez tabelę używalności
        if i[FREQ]<min_freq:           # W przypadku znalezienia mniejszej wartości niż poprzenio wpisana
            min_pid=i[PID]          # Przyjmowanie nowego najmniejszego PID-u
            min_freq=i[FREQ]        # Przyjmowanie nowej najmniejszej częstotliwości
    return min_pid

def get_pid_freq(pid:int,freq_arr): # Funkcja do otrzymywania wartości, ile razy strona została użyta
    for i in freq_arr:      # Iteracja przez tablicę ze stronami
        if i[PID]==pid: return i[FREQ]      # Przy znalezieniu PIDu zwrot jego częstotliwości

def frames_repr(frames:int,frames_arr,freq): # Funkcja do wyświetlania stanu ramek
    frames_repr=""
    for j in range(frames): # Iteracja przez ramki
        try: frames_repr+=str("{} ({})".format(frames_arr[j],get_pid_freq(frames_arr[j],freq))) # Jeżeli ta ramka jest zajęta, to istnieje w tabeli, i dopisujemy do stringa wskazywaną wartość
        except IndexError: frames_repr+="_____" # Jeżeli nic nie jest wpisane do ramki, w tym miejscu dostaniemy IndexError - zamist kończyć działanie programu, wypiszemy co innego
        if j!=frames-1: frames_repr+=" "        # Dopisywanie znaku spacji między wartościami
    return frames_repr  # Zwrot stringa

def mem_do_lfu(frames:int,calls):   # Główna funkcja LFU
    if frames==None or calls==None:     # W przypadku, gdy tablica calls bądź wartość frames nie istnieje - to się dzieje w przypadku złego wprowadzenia danych
        print("Algorytm nie może zostać wykonany.")
        return
    else: print("POCZĄTEK ALGORYTMU LFU - Ciąg odwołań:",calls)

    # Tworzenie pierwszej linijki pliku CSV
    frames_txt=""
    for i in range(frames): frames_txt+="Ramka {},".format(i)   # Każda ramka ma swoją kolumnę
    csvbuffer="Krok,{}Wymagana,Jest,Trafień,Pudeł\n".format(frames_txt) # Gotowa pierwsza linijka

    frames_arr=[]       # Tworzenie tabeli stron (ramek)
    freq_arr=[]         # Tworzenie tabeli zliczającej ilość użyć danej strony
    different_pages=[]  # Tworzenie tymczasowej tabeli ze wszystkimi PID-ami stron
    miss=0  # licznik nietrafień stron
    hits=0  # licznik trafień stron

    for i in calls:     # Przygotowanie tablicy używalności stron
        if i not in different_pages:    # Aby każdy wpis miał unikalny PID
            page_with_freq=[0,0]        # Przygotowanie szablonowej tablicy strony z częstotliwością
            different_pages.append(i)   # Dodanie PID-u strony do tablicy unikalnych stron
            page_with_freq[PID]=i       # Przypisanie PID-u do szablonu
            freq_arr.append(page_with_freq) # Dopisanie tablicy do tabeli częstotliwości

    del different_pages # Tabela już nie jest nam potrzebna

    print("Krok","Ramki\t\t","Wym.","Jest","Traf.","Pudeł",sep="\t")  # Tworzenie pierwszej linijki tabeli z nazwami kolumn

    for i in range(len(calls)): # Iteracja przez odwołania
        print(i+1,"\t│ ",frames_repr(frames,frames_arr,freq_arr)," │\t",calls[i],"\t",calls[i] in frames_arr,"\t",hits,"\t",miss,sep="\0")   # Wypisywanie linijki zawierająca: Krok, stan ramek, Następne odwołanie, Czy następne odwołanie znajduje się w ramce

        # Dopisywanie linijki do pliku .CSV
        csvbuffer+="{},".format(i+1)    # Liczba porządkowa
        for j in range(frames):         # Iteracja przez ramki
            try: csvbuffer+="{},".format(frames_arr[j]) # Dopisywanie PID-u, który zajmuje ramkę
            except IndexError: csvbuffer+=","           # W przypadku wolnej ramki, czyli PID-u o wartości NULL
        csvbuffer+="{},{},{},{}\n".format(calls[i],calls[i] in frames_arr,hits,miss)    # Dopisywanie pozostałych linijek

        if calls[i] not in frames_arr[:]:   # Jeżeli nie ma strony w żadnej z ramek
            miss+=1    # Inkrementacja licznika nietrafień
            if len(frames_arr)==frames:     # Jeżeli wszystkie ramki są zajęte
                freq_t=[]   # Tworzenie tymczasowej tabeli
                for k in frames_arr:    # Iteracja przez tabelę
                    proc_t=[k,get_pid_freq(k,freq_arr)] # Tworzenie tymczasowego procesu..
                    freq_t.append(proc_t)               # ... który zostanie wpisany do tymczasowej tabeli
                least_used_pid=get_least_used_pid(freq_t)   # Znalezienie najrzadziej używanego PID-u
                frames_arr[frames_arr.index(least_used_pid)]=calls[i]   # Zastąpienie najrzadziej używanej strony
            else: frames_arr.append(calls[i])   # Jeżeli są wolne ramki, dopisujemy na koniec tabeli
        else: hits+=1

        # Zwięszenie licznika użyć dla danej strony
        for j in range(len(freq_arr)):      # Zwiększenie licznika użyć o 1
            if freq_arr[j][PID]==calls[i]:  # Znalezienie odpowiedniej strony po PID-zie
                freq_arr[j][FREQ]+=1        # Inkrementacja licznika użyć
                break                       # Wyjście z pętli for

    print("END","\t│ ",frames_repr(frames,frames_arr,freq_arr)," │",sep="\0")    # Wypisywanie ostatecznego stanu ramek
    print("Ilość trafień:\t",hits)
    print("Ilość pudeł:\t",miss)

    freq_arr=sorted(freq_arr, key=lambda x: x[PID])     # Sortowanie tablicy częstotliwości po PID-zie

    #   Wyświetlenie tabeli częstotliwości użycia stron
    print("PID:\t",end="\0")
    for i in freq_arr: print(i[PID],end="\t")
    print("\nUŻYĆ:\t",end="\0")
    for i in freq_arr: print(i[FREQ],end="\t")
    print("")

    # Linijka ze stanem ostatecznym
    csvbuffer+="KONIEC,"    # Krok o nazwie KONIEC
    for j in range(frames): # Iteracja przez ramki
            try: csvbuffer+="{},".format(frames_arr[j]) # Dopisywanie PID-u, który zajmuje ramkę
            except IndexError: csvbuffer+=","           # W przypadku wolnej ramki, czyli PID-u o wartości NULL
    csvbuffer+=",,{},{}".format(hits,miss)  # Dopisywanie pozostałych linijek, z pominięciem wymaganej strony, i czy takowa się znajduje w ramkach
    csvexport(csvbuffer)    # Eksport wyniku do pliku .CSV
    
    del csvbuffer   # Usunięcie buforu CSV
    print("KONIEC ALGORYTMU LFU")

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik