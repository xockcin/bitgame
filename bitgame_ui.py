import tkinter as tk
import bitgame_proto as bg
import random

# initialize window
window = tk.Tk()
window.title("bitgame")

# change the colors of the buttons according to the
# status of the byte array - white if off, black if on.
def update():
    for i in range(8):
        if bg.bitArray[i] == True:
            buttonList[i].config(bg="black", fg="white")
            buttonList[i].grid(row=1, column=(8-(i+1)))
        else:
            buttonList[i].config(bg="white", fg="black")
            buttonList[i].grid(row=1, column=(8-(i+1)))
            
# display decimal, hex and ASCII values above byte
    showDec.destroy
    showDec.config(text=bg.getDec())
    showDec.grid(row=0, column=1, columnspan=2)
    showHex.destroy
    showHex.config(text=bg.getHex())
    showHex.grid(row=0, column=3, columnspan=2)
    showChr.destroy
    showChr.config(text=bg.getASCII())
    showChr.grid(row=0, column=5, columnspan=2)
 
# function for bit buttons - each bit is represented
# as a button that switches, and changes color, if
# you click on it.   
def btnSwitch(i):
    bg.switch(i)
    update()

# functon for complement button
def btnComp():
    bg.complement()
    update()

# function for left-shift button
def btnLeft():
    bg.leftShift()
    update()

# function for right-shift button
def btnRight():
    bg.rightShift()
    update()
    
# function for increment button
def btnIncr():
    bg.increment()
    update()
    
# function for decrement button
def btnDecr():
    bg.decrement()
    update()

# decimal, hex and ASCII display widgets
showDec = tk.Label(text=bg.getDec())
showDec.grid(row=0, column=1, columnspan=2)
showHex = tk.Label(text=bg.getHex())
showHex.grid(row=0, column=3, columnspan=2)
showChr = tk.Label(text=bg.getASCII())
showChr.grid(row=0, column=5, columnspan=2)

# bit button widgets
button7 = tk.Button(master=window, text="7", bg="white", command=lambda: btnSwitch(7))
button6 = tk.Button(master=window, text="6", bg="white", command=lambda: btnSwitch(6))
button5 = tk.Button(master=window, text="5", bg="white", command=lambda: btnSwitch(5))
button4 = tk.Button(master=window, text="4", bg="white", command=lambda: btnSwitch(4))
button3 = tk.Button(master=window, text="3", bg="white", command=lambda: btnSwitch(3))
button2 = tk.Button(master=window, text="2", bg="white", command=lambda: btnSwitch(2))
button1 = tk.Button(master=window, text="1", bg="white", command=lambda: btnSwitch(1))
button0 = tk.Button(master=window, text="0", bg="white", command=lambda: btnSwitch(0))

# list for easier initialization
buttonList = [button0, button1, button2, button3, button4, button5, button6, button7]

# loop to display buttons
for i in range(8):
    buttonList[8-(i+1)].grid(row=1, column=i)

# complement button widget
buttonComp = tk.Button(master=window, text="~", command=btnComp)
buttonComp.grid(row=2, column=3, columnspan=2)

# left-shift button widget
buttonLeft = tk.Button(master=window, text="<<", command=btnLeft)
buttonLeft.grid(row=2, column=1, columnspan=2)

# right-shift button widget
buttonRight = tk.Button(master=window, text=">>", command=btnRight)
buttonRight.grid(row=2, column=5, columnspan=2)

# increment button widget
buttonIncr = tk.Button(master=window, text="+", command=btnIncr)
buttonIncr.grid(row=2, column=0)

# decrement button widget
buttonDecr = tk.Button(master=window, text="-", command=btnDecr)
buttonDecr.grid(row=2, column=7)

# here is the actual game
target = random.randint(0,255)
showTarget = tk.Label(text="target: " + str(target))
showDec.grid(row=3, column=1, columnspan=2)


# and we're off!
tk.mainloop()
