import csv
import os
import random
import sys
import time
def afisa(file):
    f = open(file, 'r')
    x = csv.reader(f)
    karta = []
    for line in x:
        karta.append(line)
    return karta

def krasivo(m, map):
    m2 = m[:]
    os.system('cls')
    for item in map:
        m2[item[0]][item[1]] = "."
    m2[map[-1][0]][map[-1][1]] = "M"
    draw = " "
    for row in m2:
        for i in row:
            i = str(i).replace("1", "█")
            i = str(i).replace("0", " ")
            draw += i
        draw +="\n"
    print(draw)

def move(pers):
    time.sleep(0.000001)
    krasivo(labirint, pers)
    a = pers[-1]
    possibility = [(a[0], a[1]+1), (a[0], a[1]-1), (a[0]+1, a[1]), (a[0]-1, a[1])]
    random.shuffle(possibility)
    print(possibility)
    for item in possibility:
        if item[1] < 0 or item[0] < 0 or item[0] > len(labirint) or item[0] > len(labirint):
            continue
        elif labirint[item[0]][item[1]]=="1":
            continue
        elif labirint[item[0]][item[1]]==".":
            continue
        elif labirint[item[0]][item[1]]=="B":
            pers = pers + (item,)
            print("Конец игры)")
            sys.exit()
        else:
            new_pers = pers + (item,)
            move(new_pers)

labirint = afisa('maze.csv')
move(((1,0),))

