# Goal: find the best solution to every bigame-ultra puzzle
from tkinter import * 
SIZE = 64

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

def zerostep():
    for i in range(SIZE):
        for j in range(SIZE):
            if i == j:
                pairchart[i][j]["solved"] = True

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
                
def doToken(token, origin):
    if token == "+":
        return increment(origin)
    if token == "-":
        return decrement(origin)
    if token == "~":
        return complement(origin)
    if token == "<":
        return rightshift(origin)
    if token == ">":
        return leftshift(origin)
    
tokens = ["~","<",">","+","-"]

doubles = []
for i in range(5):
    for j in range (5):
        doubles.append(tokens[i] + tokens[j])

triples = []
for i in range(5):
    for j in range (5):
        for k in range(5):
            triples.append(tokens[i] + tokens[j] + tokens[k])

            
quadruples = []
for i in range(5):
    for j in range (5):
        for k in range(5):
            for l in range(5):
                quadruples.append(tokens[i] + tokens[j] + tokens[k] + tokens[l])

fives = []
for i in range(5):
    for j in range (5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    fives.append(tokens[i] + tokens[j] + tokens[k] + tokens[l] + tokens[m])

sixes = []
for i in range(5):
    for j in range (5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    for n in range(5):
                        sixes.append(tokens[i] + tokens[j] + tokens[k] + tokens[l] + tokens[m] + tokens[n])
                        
sevens = []
for i in range(5):
    for j in range (5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    for n in range(5):
                        for o in range(5):
                            sevens.append(tokens[i] + tokens[j] + tokens[k] + tokens[l] + tokens[m] + tokens[n] + tokens[o])



eights = []
for i in range(5):
    for j in range (5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    for n in range(5):
                        for o in range(5):
                            for p in range(5):
                                eights.append(tokens[i] + tokens[j] + tokens[k] + tokens[l] + tokens[m] + tokens[n] + tokens[o] + tokens[p])

nines = []
for item in eights:
    for token in tokens:
        nines.append(item+token)

tens = []
for item in nines:
    for token in tokens:
        tens.append(item + token)

def twostep():
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for double in doubles:
                    stepone = doToken(double[0], i)
                    steptwo = doToken(double[1], stepone)
                    if steptwo == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = double
                        break

def threestep():
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for triple in triples:
                    stepone = doToken(triple[0], i)
                    steptwo = doToken(triple[1], stepone)
                    stepthree = doToken(triple[2], steptwo)
                    if stepthree == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = triple
                        break

def fourstep():
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for quadruple in quadruples:
                    stepone = doToken(quadruple[0], i)
                    steptwo = doToken(quadruple[1], stepone)
                    stepthree = doToken(quadruple[2], steptwo)
                    stepfour = doToken(quadruple[3], stepthree)
                    if stepfour == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = quadruple
                        break

def fivestep(stepsets):
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for stepset in stepsets:
                    stepone = doToken(stepset[0], i)
                    steptwo = doToken(stepset[1], stepone)
                    stepthree = doToken(stepset[2], steptwo)
                    stepfour = doToken(stepset[3], stepthree)
                    stepfive = doToken(stepset[4], stepfour)
                    if stepfive == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = stepset
                        break

def sixstep(stepsets):
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for stepset in stepsets:
                    stepone = doToken(stepset[0], i)
                    steptwo = doToken(stepset[1], stepone)
                    stepthree = doToken(stepset[2], steptwo)
                    stepfour = doToken(stepset[3], stepthree)
                    stepfive = doToken(stepset[4], stepfour)
                    stepsix = doToken(stepset[5], stepfive)
                    if stepsix == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = stepset
                        break
                    
def sevenstep(stepsets):
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for stepset in stepsets:
                    stepone = doToken(stepset[0], i)
                    steptwo = doToken(stepset[1], stepone)
                    stepthree = doToken(stepset[2], steptwo)
                    stepfour = doToken(stepset[3], stepthree)
                    stepfive = doToken(stepset[4], stepfour)
                    stepsix = doToken(stepset[5], stepfive)
                    stepseven = doToken(stepset[6], stepsix)
                    if stepseven == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = stepset
                        break
                    
def eightstep(stepsets):
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for stepset in stepsets:
                    stepone = doToken(stepset[0], i)
                    steptwo = doToken(stepset[1], stepone)
                    stepthree = doToken(stepset[2], steptwo)
                    stepfour = doToken(stepset[3], stepthree)
                    stepfive = doToken(stepset[4], stepfour)
                    stepsix = doToken(stepset[5], stepfive)
                    stepseven = doToken(stepset[6], stepsix)
                    stepeight = doToken(stepset[7], stepseven)
                    if stepeight == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = stepset
                        break

def doThing(sets):
    for i in range(SIZE):
        for j in range(SIZE):
            if pairchart[i][j]["solved"]:
                continue
            else:
                for tokenset in sets:
                    number = i
                    for token in tokenset:
                        number = doToken(number, token)
                    if number == j:
                        pairchart[i][j]["solved"] = True
                        pairchart[i][j]["steps"] = stepset
                        break
    
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
    twostep()
    print("three step")
    threestep()
    print("four step")
    fourstep()
    print("five step")
    fivestep(fives)
    print("six step")
    sixstep(sixes)
    print("seven step")
    sevenstep(sevens)
    print("eight step")
    eightstep(eights)
    
