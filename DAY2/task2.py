#!/usr/bin/python3

f = open("../input", "r")
o = open("../output", "w")

def validgame(game):
    red=[]
    blue=[]
    green=[]
    showed = game.split(":")[1].split(";")
    for t in showed:
        z=t.split(",")
        for color in z:
            x=color.split()
            if x[1]=="red":
                red.append(int(x[0]))
            if x[1]=="green":
                green.append(int(x[0]))
            if x[1]=="blue":
                blue.append(int(x[0]))
    return(max(red)*max(blue)*max(green))
result=0

for l in f:
    result+=validgame(l)

o.write(str(result))

