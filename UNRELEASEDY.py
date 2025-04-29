from pygame import mixer
from time import sleep
from random import randint
import os

mixer.init()

specPathName = "UNRELEASEDYaudio" 
path = os.path.dirname(os.path.abspath(__file__))
dirs = [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]
def clear():
    os.system("clear")

if specPathName not in dirs:
    clear()
    os.system(f"mkdir {specPathName}")
    print(f"A {specPathName} folder has been added to the same folder this program is inside. Copy all your music to that directory and have fun playing it! Dismiss this message by pressing enter")
    input()

specPath = path + '/' + specPathName + '/'

songs = [entry for entry in os.listdir(specPath) if os.path.isfile(os.path.join(specPath, entry))]

def default():
    clear()
    print('='*20,"UNRELEASEDY","="*20,"\n")
    print("[Q] Quit\n[R] Shuffled\n[L] Loop\n")
    for i in range(len(songs)): print(f"[{i}] {songs[i]}")

def menu(song):
    clear()
    print(f"Now playing: {song}")
    opt = str(input("[Q] Quit\n[V] Volume\n[F] Filters\n[ANY] Pause\n: ")).upper()
    if opt == 'Q': 
        mixer.music.stop() 
        main() 
    elif opt == 'V':
        opt = float(input("Insert the volume you wish [0-100]: "))/100
        mixer.music.set_volume(opt)
        menu(song)
    else:
        mixer.music.pause()
        opt = input("Insert anything, even blank to unpause: ")
        mixer.music.unpause()
        menu(song)

def loop():
    default()
    opt = str(input("Choose a song to play indefinetly! [X]: ")).upper()
    try:
        clear()
        mixer.music.load(specPath + songs[int(opt)])
        mixer.music.play(-1)
        menu(songs[int(opt)])
    except:
        if opt == 'Q': main()
        elif opt == 'L': loop()
        elif opt == 'R':
            while True:
                clear()
                opt = randint(0, len(songs)-1)
                mixer.music.load(specPath + songs[int(opt)])
                mixer.music.play()
                while mixer.music.get_busy: sleep(1)

def main():
    default()
    opt = str(input("Choose a song to play! [X]: ")).upper()
    try:
        mixer.music.load(specPath + songs[int(opt)])
        mixer.music.play()
        menu(songs[int(opt)])
    except:
        if opt == 'Q': exit()
        elif opt == 'L': loop()
        elif opt == 'R':
            opt = randint(0, len(songs)-1)
            mixer.music.load(specPath + songs[int(opt)])
            mixer.music.play(-1)
            menu(songs[int(opt)])

main()