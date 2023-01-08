from tkinter import *
import json
from os import path
import pathlib as path
from tkinter import Tk as tk
from tkinter import filedialog
import tkinter.messagebox
import webview as webengine

# Application Metadata (don't remove)
global application_version
application_version = "v1.1.0"


file_name = "none"
root = Tk()
root.configure(background='#0D1117')
root.title("AuraPad")
root.geometry("800x600")
hardcoded_font = ("monospace", 12)

supported_preview_extensions = [
    "html",
    "png",
    "svg",
]

def saveas_file(arg):
    global file_name
    file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    filnm = file_name
    file = open(file_name, "w")
    file.write(text_editor.get(1.0, END))
    file.close()
    print(file_name)

def preview_file(arg):
    file_extension = path.Path(arg).suffix
    for x in supported_preview_extensions:
        if x in arg:
            file = open(arg, "r")
            webengine.create_window('Preview', arg)
            webengine.start()
            break
    tkinter.messagebox.showinfo("Preview Error",  "This file type cannot be previewed!")

def open_file(arg):
    global file_name
    file_name = filedialog.askopenfilename(defaultextension=".txt")
    print(file_name)
    file = open(file_name, "r")
    text_editor.delete(1.0, END)
    text_editor.insert(1.0, file.read())
    file.close()

def clear_text(arg):
    text_editor.delete(1.0, END)

def save_file(arg):
    file = open(file_name, "w")
    file.write(text_editor.get(1.0, END))
    file.close()

about_button = Button(root, text="About", command=lambda: tkinter.messagebox.showinfo("About AuraPad ",  "Version" + application_version))
save_button = Button(root, text="Save", command=lambda: save_file(text_editor))
sel_font = Button(root, text="Change Font", command=lambda: change_font_dialog())
saveas_button = Button(root, text="Save As", command=lambda: saveas_file(text_editor))
exit_button = Button(root, text="Exit", command=root.destroy)
open_button = Button(root, text="Open", command=lambda: open_file(text_editor))
clear_button = Button(root, text="Clear", command=lambda: clear_text(text_editor))
lang_indic = Label(root, text="None")
preview_button = Button(root, text="Preview", command=lambda: preview_file(file_name))

about_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
save_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
sel_font.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
saveas_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
open_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
exit_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
clear_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
lang_indic.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
preview_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')

save_button.grid(row=0, column=5)
sel_font.grid(row=0, column=6)
open_button.grid(row=0, column=3)
saveas_button.grid(row=0, column=2)
exit_button.grid(row=0, column=1)
clear_button.grid(row=0, column=4)
lang_indic.grid(row=0, column=7)
preview_button.grid(row=0, column=8)
about_button.grid(row=0, column=9)

text_editor = Text(root, width=100, height=30)
text_editor.configure(background='#0D1117', highlightthickness='0', bd='0', fg='#FFFFFF')
text_editor.grid(row=1, column=0, columnspan=2)
text_editor.config(font=("Arial", 12))

elems = [about_button, preview_button, lang_indic, sel_font, text_editor, save_button, open_button, saveas_button, exit_button, clear_button]

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

def setFont(fontName):
    for x in elems:
        x.configure(font = fontName)

def change_font_dialog():
    top = Tk()
    top.title = "Set Font"
    L1 = Label(top, text="Font Name:")
    L1.pack(side=LEFT)
    E1 = Entry(top, bd=5)
    E1.bind("<Return>", (lambda event: setFont(E1.get())))
    E1.pack(side=RIGHT)
    top.mainloop()

setFont(hardcoded_font)

#def highlight_html(event):
#    text = text_editor.get(1.0, END)
#    for word in HTML:
#        if word in text:
#            text_editor.tag_add("html", "1.0", END)
#            text_editor.tag_config("html", foreground="#FF0000")

def upd_lang_indic(lang):
    lang_indic.configure(text = lang)

def detect_lang():
    text = text_editor.get(1.0, END)

while True:
    #highlight_html(text_editor)
    detect_lang()
    root.update()

root.mainloop()