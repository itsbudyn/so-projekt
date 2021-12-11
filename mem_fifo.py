def mem_do_fifo(frames:int,calls):
    frames_arr=[None for i in range(frames)]

    for i in calls:
        if i not in frames_arr:
            if frames_arr.count(None)==0:
                del frames_arr[0]
            frames_arr.append(i)
        print(frames_arr)

# gdyby ktoś przypadkiem uruchomił ten plik
if __name__ == '__main__':
    print("Proszę uruchomić plik main.py")