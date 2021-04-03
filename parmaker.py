from tkinter import * 
SIZE = 256

def makerow(i):
    row = []
    for j in range(SIZE):
        row.append({"origin" : i, "goal" : j, "solved": False, "steps": ""})
    return row

def makesquare():
    pairs = []
    for i in range(SIZE):
        pairs.append(makerow(i))
    return pairs

pairchart = makesquare()

def maketable(data):
    root = Tk()
    
    height = SIZE
    width = SIZE
    for i in range(height): #Rows
        for j in range(width): #Columns
            content = str(data[i][j]["origin"]) + "=>" + str(data[i][j]["goal"]) + ":" + data[i][j]["steps"]
            b = Label(bg=("white" if data[i][j]["solved"] else "yellow"), text=content, borderwidth=2, width="12", relief="solid")
            b.grid(row=i, column=j)

    mainloop()
    
def increment(i):
    return i+1

def decrement(i):
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
