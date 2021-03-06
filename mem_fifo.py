from keywords import csvexport
from mem_create import export_calls
# Algorytm zastępowania stron FIFO

def frames_repr(frames:int,frames_arr): # Funkcja do wyświetlania stanu ramek
    frames_repr=""
    for j in range(frames): # Iteracja przez ramki
        try: frames_repr+=str(frames_arr[j])    # Jeżeli ta ramka jest zajęta, to istnieje w tabeli, i dopisujemy do stringa wskazywaną wartość
        except IndexError: frames_repr+="_"     # W przypadku, kiedy ramka jest wolna
        if j!=frames-1: frames_repr+=" "        # Dopisywanie znaku spacji między wartościami
    return frames_repr  # Zwrot stringa

def mem_do_fifo(frames:int,calls):
    if frames==None or calls==None:     # W przypadku, gdy tablica calls bądź wartość frames nie istnieje - to się dzieje w przypadku złego wprowadzenia danych
        print("Algorytm nie może zostać wykonany.")
        return
    else:
        export_calls(frames,calls)      # Pytamy użytkownika, czy chce wyeksportować tablicę wejściową do pliku txt
        print("POCZĄTEK ALGORYTMU FIFO - Ciąg odwołań:",calls)

    # Tworzenie pierwszej linijki pliku CSV
    frames_txt=""
    for i in range(frames): frames_txt+="Ramka {},".format(i)   # Każda ramka ma swoją kolumnę
    csvbuffer="Krok,{}Wymagana,Jest,Trafień,Pudeł\n".format(frames_txt) # Gotowa pierwsza linijka

    frames_arr=[]   # Tworzenie tabeli stron (ramek)
    miss=0  # licznik nietrafień stron
    hits=0  # licznik trafień stron

    print("Krok","Ramki\t","Wym.","Jest","Traf.","Pudeł",sep="\t")  # Tworzenie pierwszej linijki tabeli z nazwami kolumn

    for i in range(len(calls)): # Iteracja przez odwołania
        print(i+1,"\t│ ",frames_repr(frames,frames_arr)," │\t",calls[i],"\t",calls[i] in frames_arr,"\t",hits,"\t",miss,sep="\0")   # Wypisywanie linijki zawierająca: Krok, stan ramek, Następne odwołanie, Czy następne odwołanie znajduje się w ramce

        # Dopisywanie linijki do pliku .CSV
        csvbuffer+="{},".format(i+1)    # Liczba porządkowa
        for j in range(frames):         # Iteracja przez ramki
            try: csvbuffer+="{},".format(frames_arr[j]) # Dopisywanie PID-u, który zajmuje ramkę
            except IndexError: csvbuffer+=","           # W przypadku wolnej ramki, czyli PID-u o wartości NULL
        csvbuffer+="{},{},{},{}\n".format(calls[i],calls[i] in frames_arr,hits,miss)    # Dopisywanie pozostałych linijek

        if calls[i] not in frames_arr:  # Jeżeli nie ma strony w żadnej z ramek
            miss+=1 # Inkrementacja licznika pudeł
            if len(frames_arr)==frames: del frames_arr[0]     # Jeżeli wszystkie ramki są zajęte, zwalniamy pierwszą zajętą ramkę
            frames_arr.append(calls[i]) # Dopisywanie strony do pierwszej wolnej ramki
        else: hits+=1   # Inkrementacja licznika trafień

    print("END","\t│ ",frames_repr(frames,frames_arr)," │",sep="\0")    # Wypisywanie ostatecznego stanu ramek
    print("Ilość trafień:\t",hits)
    print("Ilość pudeł:\t",miss)

    # Linijka ze stanem ostatecznym
    csvbuffer+="KONIEC,"    # Krok o nazwie KONIEC
    for j in range(frames): # Iteracja przez ramki
            try: csvbuffer+="{},".format(frames_arr[j]) # Dopisywanie PID-u, który zajmuje ramkę
            except IndexError: csvbuffer+=","           # W przypadku wolnej ramki, czyli PID-u o wartości NULL
    csvbuffer+=",,{},{}".format(hits,miss)  # Dopisywanie pozostałych linijek, z pominięciem wymaganej strony, i czy takowa się znajduje w ramkach
    csvexport(csvbuffer)    # Eksport wyniku do pliku .CSV
    
    del csvbuffer   # Usunięcie buforu CSV
    print("KONIEC ALGORYTMU FIFO")

if __name__ == "__main__": print("Proszę uruchomić plik main.py")   # Gdyby ktoś przypadkiem uruchomił ten plik