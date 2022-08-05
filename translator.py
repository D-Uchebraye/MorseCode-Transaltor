
from tkinter import *
#from __init__ import eng2mors
#entry widget is a textbox that accepts a single line of input

# entry widget = textbox that accepts a single line of user input

from tkinter import *

def  submit():
  
   message = entry.get()

   morse_dict =  { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
   
   for i in message: 
      morsemessage = message + morse_dict[i]
     labelb = Label('300,300'text = (morsemessage))
     labelb.pack()






def delete():
    entry.delete(0,END) #deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character

window = Tk()
window.title("user input")
label = Label(window,text="username: ")
label.config(font=("Consolas",30))
label.pack(side=LEFT)

submit = Button(window,text="submit",command=submit)
submit.pack(side = RIGHT)

delete = Button(window,text="delete",command=delete)
delete.pack(side = RIGHT)

backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Ink Free',50)) #change font
entry.config(bg='#111111') #background
entry.config(fg='#00FF00') #foreground
entry.config(width=10) #width displayed in characters
#entry.insert(0,'Spongebob') #set default text
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(show='*') #replace characters shown with x character
entry.pack()
window.mainloop()



