# Algorytm zastępowania stron FIFO

def get_least_used_pid(freq):
    min_pid=freq[0][0]
    min_freq=freq[0][1]
    for i in freq:
        if i[1]<min_freq: 
            min_pid=i[0]
            min_freq=i[1]
    return min_pid

def get_pid_freq(pid:int,freq):
    pid_freq=0
    for i in freq:
        if i[0]==pid: pid_freq=i[1]
    return pid_freq

def frames_repr(frames:int,frames_arr,freq): # Funkcja do wyświetlania stanu ramek
    frames_repr=""  # Tworzenie pustego stringa
    for j in range(frames): # Iteracja przez ramki
        try:
            frames_repr+=str("{}({})".format(frames_arr[j],get_pid_freq(frames_arr[j],freq))) # Jeżeli ta ramka jest zajęta, to istnieje w tabeli, i dopisujemy do stringa wskazywaną wartość
        except IndexError:
            frames_repr+="____"    # W przypadku, kiedy ramka jest wolna
        if j!=frames-1: frames_repr+=" "    # Dopisywanie znaku spacji między wartościami
    return frames_repr  # Zwrot stringa

def mem_do_lfu(frames:int,calls):
    frames_arr=[]       # Tworzenie pustej tabeli stron
    freq=[]             # Tworzenie tabeli zliczającej ilość użyć danej strony
    different_pages=[]  # Tworzenie tabeli ze wszystkimi PID-ami stron

    for i in calls:
        if i not in different_pages:
            page_with_freq=[0,0]
            different_pages.append(i)
            page_with_freq[0]=i
            freq.append(page_with_freq)

    del different_pages

    print("Krok","Ramki\t","Wym.","Jest",sep="\t")  # Tworzenie pierwszej linijki tabeli z nazwami kolumn

    for i in range(len(calls)): # Iteracja przez odwołania
        print(i+1,"\t│ ",frames_repr(frames,frames_arr,freq)," │\t",calls[i],"\t",calls[i] in frames_arr,sep="\0")   # Wypisywanie linijki zawierająca: Krok, staan ramek, Następne odwołanie, Czy następne odwołanie znajduje się w ramce

        if calls[i] not in frames_arr[:]:  # Jeżeli nie ma strony w żadnej z ramek
            if len(frames_arr)==frames: # Jeżeli wszystkie ramki są zajęte
                freq_t=[]
                for k in frames_arr:
                    proc_t=[k,get_pid_freq(k,freq)]
                    freq_t.append(proc_t)
                least_used_pid=get_least_used_pid(freq_t)
                frames_arr[frames_arr.index(least_used_pid)]=calls[i]
            else: frames_arr.append(calls[i])

        for j in range(len(freq)):
            if freq[j][0]==calls[i]: 
                freq[j][1]+=1
                break

    print("END","\t│ ",frames_repr(frames,frames_arr,freq)," │",sep="\0")    # Wypisywanie ostatecznego stanu ramek

# Gdyby ktoś przypadkiem uruchomił ten plik
if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")