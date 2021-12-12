# Algorytm zastępowania stron LFU

# Słowa kluczowe
PID     = 0
FREQ    = 1

def get_least_used_pid(freqs_arr):  # Funkcja do otrzymywania PID-u strony najrzadziej używanej
    min_pid=freqs_arr[0][PID]       # Przygotowanie do znalezienia minimum - przyjmowanie wartości z pierwszego elementu tabeli jako wartości początkowe
    min_freq=freqs_arr[0][FREQ]
    for i in freqs_arr:             # Iteracja przez tabelę używalności
        if i[FREQ]<min_freq:           # W przypadku znalezienia mniejszej wartości niż poprzenio wpisana
            min_pid=i[PID]
            min_freq=i[FREQ]
    return min_pid

def get_pid_freq(pid:int,freq_arr): # Funkcja do otrzymywania wartości, ile razy strona została użyta
    pid_freq=0
    for i in freq_arr:
        if i[PID]==pid: pid_freq=i[FREQ]
    return pid_freq

def frames_repr(frames:int,frames_arr,freq): # Funkcja do wyświetlania stanu ramek
    frames_repr=""
    for j in range(frames): # Iteracja przez ramki
        try:
            frames_repr+=str("{} ({})".format(frames_arr[j],get_pid_freq(frames_arr[j],freq))) # Jeżeli ta ramka jest zajęta, to istnieje w tabeli, i dopisujemy do stringa wskazywaną wartość
        except IndexError:                  # Jeżeli nic nie jest wpisane do ramki, w tym miejscu dostaniemy IndexError - zamist kończyć działanie programu, wypiszemy co innego
            frames_repr+="_____"
        if j!=frames-1: frames_repr+=" "    # Dopisywanie znaku spacji między wartościami
    return frames_repr  # Zwrot stringa

def mem_do_lfu(frames:int,calls):   # Główna funkcja LFU
    frames_arr=[]       # Tworzenie tabeli stron
    freq_arr=[]         # Tworzenie tabeli zliczającej ilość użyć danej strony
    different_pages=[]  # Tworzenie tymczasowej tabeli ze wszystkimi PID-ami stron

    for i in calls:     # Przygotowanie tablicy używalności stron
        if i not in different_pages:    # Aby każdy wpis miał unikalny PID
            page_with_freq=[0,0]
            different_pages.append(i)
            page_with_freq[PID]=i
            freq_arr.append(page_with_freq)

    del different_pages # Tabela już nie jest nam potrzebna

    print("Krok","Ramki\t","Wym.","Jest",sep="\t")  # Tworzenie pierwszej linijki tabeli z nazwami kolumn

    for i in range(len(calls)): # Iteracja przez odwołania
        print(i+1,"\t│ ",frames_repr(frames,frames_arr,freq_arr)," │\t",calls[i],"\t",calls[i] in frames_arr,sep="\0")   # Wypisywanie linijki zawierająca: Krok, staan ramek, Następne odwołanie, Czy następne odwołanie znajduje się w ramce

        if calls[i] not in frames_arr[:]:   # Jeżeli nie ma strony w żadnej z ramek
            if len(frames_arr)==frames:     # Jeżeli wszystkie ramki są zajęte
                freq_t=[]   # Tworzenie tymczasowej tabeli
                for k in frames_arr:    # Iteracja przez tabelę
                    proc_t=[k,get_pid_freq(k,freq_arr)] # Tworzenie tymczasowego procesu..
                    freq_t.append(proc_t)               # ... który zostanie wpisany do tymczasowej tabeli
                least_used_pid=get_least_used_pid(freq_t)   # Znalezienie najrzadziej używanego PID-u
                frames_arr[frames_arr.index(least_used_pid)]=calls[i]   # Zastąpienie najrzadziej używanej strony
            else: frames_arr.append(calls[i])   # Jeżeli są wolne ramki, dopisujemy na koniec tabeli

        for j in range(len(freq_arr)):      # Zwiększenie licznika użyć o 1
            if freq_arr[j][PID]==calls[i]: 
                freq_arr[j][FREQ]+=1
                break

    print("END","\t│ ",frames_repr(frames,frames_arr,freq_arr)," │",sep="\0")    # Wypisywanie ostatecznego stanu ramek

if __name__ == '__main__':  # Gdyby ktoś przypadkiem uruchomił ten plik
    print("Proszę uruchomić plik main.py")