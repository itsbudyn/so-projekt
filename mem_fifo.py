def frames_repr(frames:int,frames_arr):
    frames_repr=""
    for j in range(frames):
        try:
            frames_repr+=str(frames_arr[j])
        except IndexError:
            frames_repr+="_"
        if j!=frames-1: frames_repr+=" "
    return frames_repr


def mem_do_fifo(frames:int,calls):
    frames_arr=[]

    print("Krok","Ramki\t","Wym.","Jest",sep="\t")

    for i in range(len(calls)):
        print(i+1,"\t│ ",frames_repr(frames,frames_arr)," │\t",calls[i],"\t",calls[i] in frames_arr,sep="\0")

        if calls[i] not in frames_arr:
            if len(frames_arr)==frames:
                del frames_arr[0]
            frames_arr.append(calls[i])

    print("END","\t│ ",frames_repr(frames,frames_arr)," │",sep="\0")

# gdyby ktoś przypadkiem uruchomił ten plik
if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")