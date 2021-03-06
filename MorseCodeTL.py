from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Morse Code TL")
window.configure(bg = '#c0c0c0')
window.geometry("1200x250")

AtoM = {'A': '.-'   , 'B': '-...'   , 'C': '-.-.'   , 'D': '-..', 
        'E': '.'    , 'F': '..-.'   , 'G': '--.'    , 'H': '....',
        'I': '..'   , 'J': '.---'   , 'K': '-.-'    , 'L': '.-..',
        'M': '--'   , 'N': '-.'     , 'O': '---'    , 'P': '.--.',
        'Q': '--.-' , 'R': '.-.'    , 'S': '...'    , 'T': '-',
        'U': '..-'  , 'V': '...-'   , 'W': '.--'    , 'X': '-..-',
        'Y': '-.--' , 'Z': '--..'   , '0': '-----'  , '1': '.----',
        '2': '..---', '3': '...--'  , '4': '....-'  , '5': '.....',
        '6': '-....', '7': '--...'  , '8': '---..'  , '9': '----.'}

MtoA = {}
for key, value in AtoM.items():
    MtoA[value] = key

def atom(msg):
    morse = []
    for i in msg:
        if i in AtoM:
            morse.append(AtoM[i])
    return " ".join(morse)

def mtoa(msg):
    msg = msg.split(" ")
    alph = []
    for i in msg:
        if i in MtoA:
            alph.append(MtoA[i])
    return " ".join(alph)

def main1():
    c = tfInput.get()
    alph = c.upper()
    morse = atom(alph)
    tfOutput.delete(0, END)
    tfOutput.insert(0, str(morse))

    if morse == "":
        messagebox.showwarning("", "Input tidak valid")

def main2():
    c = tfInput.get()
    morse = c
    alph = mtoa(morse)
    tfOutput.delete(0, END)
    tfOutput.insert(0, str(alph))
    if alph =="":
        messagebox.showinfo("", "Input tidak valid")

def cls():
    tfInput.delete(0, END)
    tfOutput.delete(0, END)
    

#Label
labTitle = Label(window, text= "Morse Code Translator",
                font=("comic sans ms", 30),
                bg= 'white', borderwidth= 3, 
                relief='groove', padx= 5).place(x = 380, y = 5) 
labInput = Label(window, text= "Input",
                font=("comic sans ms", 15),
                padx= 5, bg='#c0c0c0').place(x = 180, y = 55) 
labOutput = Label(window, text= "Output",
                font=("comic sans ms", 15),
                padx= 5, bg='#c0c0c0').place(x = 880, y = 55) 

#TextField
tfInput  = Entry(window ,width=40, borderwidth=5, font = ("comic sans ms", 14))
tfOutput = Entry(window, width=40, borderwidth=5, font = ("times new roman", 15))
tfInput.place(x=30, y=100)
tfOutput.place(x=720, y=100)

#button
b1 = Button(window, text="Alphabet to Morse", command=main1).place(x=565, y=100)
b2 = Button(window, text="Morse to Alphabet", command=main2).place(x=565, y=140)
b3 = Button(window, text="Clear", command=cls, width= 30).place(x=510,y=200)

window.mainloop()
