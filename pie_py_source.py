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
import urllib.request
import sys
import keyboard
import tkinter.colorchooser
import cv2
import wikipedia
import requests

root = Tk()
root.title('Pie')
root.iconbitmap("favi.ico")
root.resizable(1, 0)
#creating scrollable notepad window
notepad = ScrolledText(root, width = 70, height = 55)
btnp = str(notepad)
fileName = ' '
#defining functions for commands
main = str(root)
foo = "foo"
bar = "bar"

#########################################################################################################

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
    label = messagebox.showinfo("About Pie V/0.75", "©CmSpeedrunner\nPie V/0.75\nPublic License")
def cmdDark():     #help menu About option
    mainy = len(notepad.get("0.0", "end"))
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

def cmdImporthtml():
        url = simpledialog.askstring("URL", "Enter URL")
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        notepad.insert(INSERT, mystr)





def cmdOpen2():     #file menu Open option
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     #t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    better = str(fd)
    better2 = better.lstrip("<_io.TextIOWrapper name='")
    better3 = better2.rstrip("' mode='r' encoding='cp1252'>")
    webbrowser.open(better3)

def cmdOpen3():     #file menu Open option
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     #t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    better = str(fd)
    better2 = better.lstrip("<_io.TextIOWrapper name='")
    better3 = better2.rstrip("' mode='r' encoding='cp1252'>")
    os.open(better3, "print")
    os.startfile(better3, "print")
    
def cmdFig():
     
     wiki = simpledialog.askstring("Write Essay", "Enter topic (keep short):")
     summary = wikipedia.summary(wiki, sentences=700)
    
     notepad.insert('0.0',summary)


def cmdRenderhtml():
    cmdOpen2()


#########################################################
def cmdClean():
    notepad.delete(0.0, END)

def cmdPaint():
    class Paint(object):

        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'

        def __init__(self):
            self.root2 = Tk()
            self.root2.iconbitmap("favi.ico")
            self.root2.title("Embedded Paint Playground")

            self.pen_button = Button(self.root2, text='pen', command=self.use_pen)
            self.pen_button.grid(row=0, column=0)


            self.color_button = Button(self.root2, text='color', command=self.choose_color)
            self.color_button.grid(row=0, column=1)



            self.choose_size_button = Scale(self.root2, from_=1, to=20, orient=HORIZONTAL)
            self.choose_size_button.grid(row=0, column=2)

            self.c = Canvas(self.root2, bg='white', width=400, height=400)
            self.c.grid(row=1, columnspan=3)

            self.setup()
            self.root2.mainloop()

        def setup(self):
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)

        def use_pen(self):
            self.activate_button(self.pen_button)

        def use_brush(self):
            self.activate_button(self.brush_button)

        def choose_color(self):
            self.eraser_on = False
            self.color = tkinter.colorchooser.askcolor(color=self.color)[1]

        def use_eraser(self):
            self.activate_button(self.eraser_button, eraser_mode=True)

        def activate_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=RAISED)
            some_button.config(relief=SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode

        def paint(self, event):
            self.line_width = self.choose_size_button.get()
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=self.line_width, fill=paint_color,
                                   capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.old_x = event.x
            self.old_y = event.y

        def reset(self, event):
            self.old_x, self.old_y = None, None


    if __name__ == '__main__':
        Paint()   

##########################################################################
def cmdPrint():
    notepad.insert(INSERT, "©CmSpeedrunner\nPie V/0.75\nPublic License")

def cmdLetterins():
    notepad.insert(INSERT,'''							  333 Pie Road                        								London                    							United Kingdom	
Dear Null,
						                         					             30th January 2023

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",


 ''')


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
editMenu.add_command(label='Clear All', command = cmdClean)
editMenu.add_separator()
editMenu.add_command(label='Find...', command = cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All*', command = cmdSelectAll)
editMenu.add_command(label='Time/Date*', command = cmdTimeDate)
editMenu.add_command(label='Letter Format*', command = cmdLetterins)
editMenu.add_separator()
editMenu.add_command(label="Narrate*", command = cmdSpeak)
editMenu.add_separator()
editMenu.add_command(label="Dark Mode", command = cmdDmt)
editMenu.add_command(label="Light Mode", command = cmdLmt)
editMenu.add_separator()
editMenu.add_command(label="Version Insert* ", command = cmdPrint)
#help menu
helpMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Info', menu = helpMenu)
editMenu.add_separator()




#adding options in help menu
helpMenu.add_command(label='About Pie', command = cmdAbout)
helpMenu.add_command(label='Link To Page', command = cmdLink)
helpMenu.add_command(label='Open Duplicate', command = cmdDupe)
helpMenu.add_command(label='Open CMD*', command = cmdSlate)
helpMenu.add_command(label='Open Source', command = cmdSource)


viewMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Details', menu = viewMenu)
viewMenu.add_command(label='Count', command = cmdDark)


#module menu
moduleMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Modules', menu = moduleMenu)
moduleMenu.add_command(label='Url2HTML5', command = cmdImporthtml)
moduleMenu.add_command(label ='Open HTML5', command = cmdRenderhtml)
moduleMenu.add_command(label = "AI-Essay Writer", command = cmdFig)
moduleMenu.add_separator()
moduleMenu.add_command(label = "Paint App*", command = cmdPaint)



keyboard.add_hotkey("ctrl+alt+p", lambda:cmdPaint())
keyboard.add_hotkey("ctrl+alt+o", lambda:cmdSlate())
keyboard.add_hotkey("ctrl+alt+n", lambda:cmdSpeak())
keyboard.add_hotkey("ctrl+alt+v", lambda:cmdPrint())
keyboard.add_hotkey("ctrl+alt+s", lambda:cmdSelectAll())
keyboard.add_hotkey("ctrl+alt+t", lambda:cmdTimeDate())
keyboard.add_hotkey("ctrl+alt+l", lambda:cmdLetterins())
keyboard.add_hotkey("ctrl+alt+s+d", lambda: webbrowser.open_new("https://static.wikia.nocookie.net/p__/images/8/8f/Scrappy-Doo_promo.png/revision/latest?cb=20190917160755&path-prefix=protagonist"))



notepad.pack()
root.mainloop()