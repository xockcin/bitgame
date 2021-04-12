from PIL import Image
import numpy as np
from tkinter import * 
SIZE = 16

import json
f = open('pairchart.json')
full_pairs = json.load(f)

def make_row(i):
    row = []
    for j in range(SIZE):
        row.append({"origin" : i, "goal" : j, "solved": False, "steps": ""})
    return row

def make_square():
    pairs = []
    for i in range(SIZE):
        pairs.append(make_row(i))
    return pairs

def make_stepcount_array(pairchart):
    array = []
    for row in pairchart:
        array.append([len(data["steps"]) for data in row])
    return array

def steps_to_colors(steps_array):
    colors_array = []
    for row in steps_array:
        colors_array.append([colors[x]["rgb"] for x in row])
    return colors_array

def steps_to_grayscale(steps_array):
    grayscale_array = []
    for row in steps_array:
        grayscale_array.append([[x*25, x*25, x*25] for x in row])
    return grayscale_array
            

colors = [
    {"name": "black", "rgb": [0,0,0]},
    {"name": "brown", "rgb": [165,42,42]},
    {"name": "red", "rgb": [255,0,0]},
    {"name": "orange", "rgb": [255,165,0]},
    {"name": "yellow", "rgb": [255,255,0]},
    {"name": "green", "rgb": [0,255,0]},
    {"name": "blue", "rgb": [0,0,255]},
    {"name": "violet", "rgb": [238,130,214]},
    {"name": "grey", "rgb": [128,128,128]},
    {"name": "white", "rgb": [255,255,255]},
    {"name": "gold", "rgb": [255,215,0]}
]

def makeimgarray(nparray):
    img_array = []
    for x in nparray.reshape(SIZE*SIZE):
        img_array.append(colors[x]["rgb"])
    return img_array

def makepiltable(data):
    colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
  ]
    im = Image.new("RGB", (SIZE, SIZE))
    height = SIZE
    width = SIZE
    for i in range(height): #Rows
        for j in range(width): #Columns
            stepcount = len(data[i][j]["steps"])
            im.putpixel((i,j), ImageColor(colors[stepcount], "RGB"))
    im.show()
    

def maketable(data):
    root = Tk()
    
    height = SIZE
    width = SIZE
    for i in range(height): #Rows
        for j in range(width): #Columns
            content = str(data[i][j]["origin"]) + "=>" + str(data[i][j]["goal"]) + ":" + data[i][j]["steps"]
            b = Label(
                bg=("white" if data[i][j]["solved"] else "yellow"),
                text=content,
                borderwidth=2, width="12",
                relief="solid")
            b.grid(row=i, column=j)

    mainloop()
    
def makesmalltable(data):
    colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
  ]
    
    root = Tk()
    
    height = SIZE
    width = SIZE
    for i in range(height): #Rows
        for j in range(width): #Columns
            stepcount = len(data[i][j]["steps"])
            b = Label(
                bg=(colors[stepcount]),
                borderwidth=1,
                height=1,
                width=1,
                relief="solid")
            b.grid(row=i, column=j)

    mainloop()

def increment(i):
    return i+1

def decrement(i):
    if i == 0:
        return 255
    else:
        return i-1

def complement(i):
    return SIZE - 1 - i

def leftshift(i):
    return (i*2) % SIZE
    
def rightshift(i):
    return int(i/2)

tokens = ["~","<",">","+","-"]

def doToken(token, origin):
    if token == "+":
        return increment(origin)
    if token == "-":
        return decrement(origin)
    if token == "~":
        return complement(origin)
    if token == ">":
        return rightshift(origin)
    if token == "<":
        return leftshift(origin)
    
def doTokenSet(tokenSet, origin):
    result = origin
    for token in tokenSet:
        result = doToken(token, result)
    return result

def zerostep():
    for i in range(SIZE):
        for j in range(SIZE):
            if i == j:
                pairchart[i][j]["solved"] = True

def onestep():
    answer = ""
    for i in range(SIZE):
        for j in range(SIZE):
            if j == increment(i):
                answer = "+"
            elif j == decrement(i):
                answer = "-"
            elif j == complement(i):
                answer = "~"
            elif j == leftshift(i):
                answer = "<"
            elif j == rightshift(i):
                answer = ">"
            else:
                continue
            if answer:
                pairchart[i][j]["solved"] = True
                pairchart[i][j]["steps"] = answer
                


doubles = []
for i in range(5):
    for j in range (5):
        doubles.append(tokens[i] + tokens[j])
        
threes = []
for item in doubles:
    for token in tokens:
        threes.append(item+token)

fours = []
for item in threes:
    for token in tokens:
        fours.append(item+token)

fives = []
for item in fours:
    for token in tokens:
        fives.append(item+token)
        
sixes = []
for item in fives:
    for token in tokens:
        sixes.append(item+token)
        
sevens = []
for item in sixes:
    for token in tokens:
        sevens.append(item+token)

eights = []
for item in sevens:
    for token in tokens:
        eights.append(item+token)
        
nines = []
for item in eights:
    for token in tokens:
        nines.append(item+token)
        
tens = []
for item in nines:
    for token in tokens:
        tens.append(item+token)
        
def doThing(tokenSets):
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for tokenSet in tokenSets:
                    number = doTokenSet(tokenSet, i)
                    if number == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = tokenSet 
                        

def find_unsolved():
    still_unsolved = []
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"] == False:
                still_unsolved.append(pairchart[i][j])
    return still_unsolved

def do_small_steps():
    print("zero step")
    zerostep()
    print("one step")
    onestep()
    print("two step")
    doThing(doubles)
    print("three step")
    doThing(threes)
    print("four step")
    doThing(fours)
    print("five step")
    doThing(fives)
    print("six step")
    doThing(sixes)
    print("seven step")
    doThing(sevens)


def do_the_steps():
    print("zero step")
    zerostep()
    print("one step")
    onestep()
    print("two step")
    doThing(doubles)
    print("three step")
    doThing(threes)
    print("four step")
    doThing(fours)
    print("five step")
    doThing(fives)
    print("six step")
    doThing(sixes)
    print("seven step")
    doThing(sevens)
    print("eight step")
    doThing(eights)
    print("nine step")
    doThing(nines)
    print("ten step")
    doThing(tens)
