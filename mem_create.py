from keywords import exit_err

def create_pages():
    page_calls=[]
    try:
        page_calls=list(map(int,str(input("Podaj odwołania: ")).split(" ")))
    except ValueError:
        exit_err("Jedna z wartości nie była liczbą całkowitą (int)!")

    return page_calls

def create_frames():
    try:
        frames=int(input("Podaj ilość ramek: "))
    except ValueError:
        exit_err("Wartość nie była liczbą całkowitą (int)!")

    if frames<0: exit_err("Wartość nie może być mniejsza od zera!")
    return frames

if __name__ == "__main__":
    print("Proszę uruchomić plik main.py")