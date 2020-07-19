from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.colorchooser import *
import tkinter as tk
import sys, codecs


# opens settings window
def Settings():
    
    settings = Tk()

    c=Checkbutton(settings, text="hide StatusBar")
    c.grid(row=0, column=1, sticky= W)

    c=Checkbutton(settings, text="hide toolbar")
    c.grid(row=1, column=1, sticky= W)
    
    settings.maxsize(width=200, height=200)

    button1 = Button(settings, text="Ok")
    button1.grid(row=2, column=1)
    button2 = Button(settings, text="cancel", command=cancel)
    button2.grid(row=2, column=2)
    button3 = Button(settings, text="apply")
    button3.grid(row=2, column=3)
    
    settings.mainloop()

# opens help window
def Help():
    Help = Tk()
    Help.minsize(width=200, height=200)
    label = Label(Help, text="This window is for help with the program")
    label.pack()

    Help.mainloop()

#opens about window
def About():

    About = Tk()

    label = Label(About, text=("This program was made by Daniel Hayes. \
This is my first program. I hope to learn from this to make \
better programs in the future"))
    label.pack()

    About.mainloop()

#declares file name
filename = None

# allows you to make a new file
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
       
# allows you to append saved file
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = Open(filename, 'w')
    f.write(t)
    
# allows you to make a saved file
def saveAs():
    f = asksaveasfile(mode =  'w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="opps!", message="unable to save file...")

# allows you to open a saved file
def openFile(): 
    f = askopenfile(mode= 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

#allows you to quit application
def Quit():
    root.destroy('<Escape>', close)

def OnVsb(*args):
    text.yview(*args)
    numbers.yview(*args)

# allows you to undo 
def undo(*argv):
    text.edit_undo()
    text.event_generate('<Control-z>')

# allows you to bring back something you undid
def redo(*argv):
    text.edit_redo()
    text.event_generate('<Control-Shift-z>')

# cut command key
lambda: text.event_generate('<Control-x>')


lambda: text.event_generate('<Control-n>')

# paste command key
lambda: text.event_generate('<Control-v>')

# copy command key
lambda: text.event_generate('<Control-c>')


# makes a status bar so you can see the current status of file
class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

def callback():
    print ("called the callback!")

# tkinter blank template file 
def tkinterblank():
    f = open("tkinterblank.py")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

# monodevelop blank template file
def monoblank():
    f = open("monoblank.py")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    

# main window
root = tk.Tk()

root.bind('<Escape>', quit)
root.bind('<Control-z>', undo)
root.minsize(width=400, height=400)
root.maxsize(width=1000, height=700)

# creates a tool bar for quick use of some commands
toolbar = Frame(root)

b = Button(toolbar, text="new", width=4, command=newFile)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="open", width=4, command=openFile)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="Save As", width=5, command=saveAs)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# puts status bar in the main window
status = StatusBar(root)
status.pack(side=BOTTOM, fill=X)

text = ScrolledText(root, width=200, height=200, undo = True,)

text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))

text.tag_configure('big', font=('Verdana', 24, 'bold'))

text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))

text.tag_configure('groove', relief=GROOVE, borderwidth=2)

text.tag_bind('bite', '<1>',
              lambda e, t=text: t.insert(END, "I'll bite your legs off!"))

text.pack()


# makes a main menu bar with drop down menu's
menu = Menu(root)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="new", command=newFile, accelerator="<Ctrl+N>")
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
Template=Menu(menu)
filemenu.add_cascade(label="Template", menu=Template)
csharp = Menu(menu)
Template.add_cascade(label="C#", menu=csharp)
csharp.add_command(label="monoblank", command=monoblank)
Python = Menu(menu)
Template.add_cascade(label="Python", menu=Python)
Python.add_command(label="tkinter basic", command=tkinterblank)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=Quit)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="undo", command=undo, accelerator="Ctrl+Z")
editmenu.add_command(label="redo", command=redo, accelerator="Ctrl+Shift+Z")
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text.event_generate('<<Cut>>'))
editmenu.add_command(label="paste", accelerator="Ctrl+v", command=lambda: text.event_generate('<<Paste>>'))
editmenu.add_command(label="copy", accelerator="Ctrl+c", command=lambda: text.event_generate('<<Copy>>'))
editmenu.add_separator()
textcolour = Menu(menu)
editmenu.add_cascade(label="Text Colour", menu=textcolour)
textcolour.add_command(label="black")
textcolour.add_command(label="green")
textcolour.add_command(label="red")

toolmenu = Menu(menu)
menu.add_cascade(label="Tools", menu=toolmenu)
toolmenu.add_command(label="Status Bar")
Language = Menu(menu)
toolmenu.add_cascade(label="Language", menu=Language)
toolmenu.add_command(label="dictionary")

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Settings", command=Settings)
helpmenu.add_command(label="Help", command = Help)
helpmenu.add_separator()
helpmenu.add_command(label="About TextCode", command = About)

root.update()

status.set("Connecting...")

root.config(menu=menu, bg="black")
root.mainloop()
