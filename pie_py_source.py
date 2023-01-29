#importing required packages and libraries
import re
import os
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
import webbrowser
import pyttsx3 

root = Tk()
root.title('Pie')
root.iconbitmap("favi.ico")
root.resizable(0, 0)
#creating scrollable notepad window
notepad = ScrolledText(root, width = 90, height = 40)
btnp = str(notepad)
fileName = ' '
#defining functions for commands
main = str(root)

def cmdNew():     #file menu New option
    global fileName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("Pie", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, END)
    root.title("Pie")
def cmdOpen():     #file menu Open option
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     #t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)

    
    
def cmdSave():     #file menu Save option
    fd = filedialog.asksaveasfile(mode = "w")
    if fd!= None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
     
def cmdSaveAs():     #file menu Save As option
    fd = filedialog.asksaveasfile(mode='w')
    t = notepad.get(0.0, END)     #t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
def cmdExit():     #file menu Exit option
    if messagebox.askyesno("Pie", "Are you sure you want to exit?"):
        root.destroy()
def cmdCut():     #edit menu Cut option
    notepad.event_generate("<<Cut>>")
def cmdCopy():     #edit menu Copy option
    notepad.event_generate("<<Copy>>")
def cmdPaste():     #edit menu Paste option
    notepad.event_generate("<<Paste>>")
def cmdClear():     #edit menu Clear option
    notepad.event_generate("<<Clear>>")
def cmdSpeak():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    data = notepad.get('1.0', END)
    engine.say (data)
    engine.runAndWait()
       
def cmdFind():     #edit menu Find option
    notepad.tag_remove("Found",'1.0', END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'     #idx stands for index
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)
def click(event):     #handling click event
    notepad.tag_config('Found',background='white',foreground='black')
def cmdSelectAll():     #edit menu Select All option
    notepad.event_generate("<<SelectAll>>")
    
def cmdTimeDate():     #edit menu Time/Date option
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    notepad.insert(INSERT, dtString)
def cmdAbout():     #help menu About option
    label = messagebox.showinfo("About Pie V/0.85", "Pie by - \nCmSpeedrunner")
def cmdDark():     #help menu About option
    mainy = len(notepad.get("1.0", "end"))
    mainy2 = mainy*8
    mainy3 = ("CHAR COUNT: ",mainy,"\nBITS: ", mainy2)
    label = messagebox.showinfo("Details", mainy3)

def cmdLink():
    webbrowser.open_new("https://github.com/cmspeedrunner/pie")

def cmdDupe():
    os.startfile("Pie.exe")

def cmdSlate():
    os.startfile("cmd.exe")

def cmdSource():
    os.startfile("source.html")

def cmdDmt():
        notepad.config(background="#020620", foreground="White")
def cmdLmt():
        notepad.config(background="White", foreground="Black")


def cmdReload():
    os.startfile("Pie.exe")
    exit()

notepadMenu = Menu(root)
root.configure(menu=notepadMenu)
#file menu
fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)
#adding options in file menu
fileMenu.add_command(label='New', command = cmdNew)
fileMenu.add_command(label='Open...', command = cmdOpen)
fileMenu.add_command(label='Save', command = cmdSave)
fileMenu.add_command(label='Save As...', command = cmdSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Reload', command = cmdReload)
fileMenu.add_command(label='Exit', command = cmdExit)
#edit menu
editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)
#adding options in edit menu
editMenu.add_command(label='Cut', command = cmdCut)
editMenu.add_command(label='Copy', command = cmdCopy)
editMenu.add_command(label='Paste', command = cmdPaste)
editMenu.add_command(label='Delete', command = cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command = cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All', command = cmdSelectAll)
editMenu.add_command(label='Time/Date', command = cmdTimeDate)
editMenu.add_separator()
editMenu.add_command(label="Narrate", command = cmdSpeak)
editMenu.add_separator()
editMenu.add_command(label="Dark Mode", command = cmdDmt)
editMenu.add_command(label="Light Mode", command = cmdLmt)

#help menu
helpMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Info', menu = helpMenu)
editMenu.add_separator()


#adding options in help menu
helpMenu.add_command(label='About Pie', command = cmdAbout)
helpMenu.add_command(label='Link To Page', command = cmdLink)
helpMenu.add_command(label='Open Duplicate', command = cmdDupe)
helpMenu.add_command(label='Open CMD', command = cmdSlate)
helpMenu.add_command(label='Open Source', command = cmdSource)

viewMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Details', menu = viewMenu)
viewMenu.add_command(label='Main Details', command = cmdDark)

notepad.pack()
root.mainloop()