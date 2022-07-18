from tkinter import *
from tkinter import filedialog

root = Tk()
root.configure(background='#0D1117')
root.title("AuraPad")
root.geometry("800x600")

def saveas_file(arg):
    global file_name
    file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    filnm = file_name
    file = open(file_name, "w")
    file.write(text_editor.get(1.0, END))
    file.close()
    print(file_name)

def open_file(arg):
    file_name = filedialog.askopenfilename(defaultextension=".txt")
    file = open(file_name, "r")
    text_editor.delete(1.0, END)
    text_editor.insert(1.0, file.read())
    file.close()

def clear_text(arg):
    text_editor.delete(1.0, END)

# save to file "file_name"
def save_file(arg):
    file = open(file_name, "w")
    file.write(text_editor.get(1.0, END))
    file.close()

save_button = Button(root, text="Save", command=lambda: save_file(text_editor))
saveas_button = Button(root, text="Save As", command=lambda: saveas_file(text_editor))
exit_button = Button(root, text="Exit", command=root.destroy)
open_button = Button(root, text="Open", command=lambda: open_file(text_editor))
clear_button = Button(root, text="Clear", command=lambda: clear_text(text_editor))

save_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
saveas_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
open_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
exit_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
clear_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')

save_button.grid(row=0, column=5)
open_button.grid(row=0, column=3)
saveas_button.grid(row=0, column=2)
exit_button.grid(row=0, column=1)
clear_button.grid(row=0, column=4)

text_editor = Text(root, width=100, height=30)
text_editor.configure(background='#0D1117', highlightthickness='0', bd='0', fg='#FFFFFF')
text_editor.grid(row=1, column=0, columnspan=2)
text_editor.config(font=("Arial", 12))

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# the following code is for syntax highlighting
htmlSyntax = ["<html>", "<style>", "<center>", "<h1>", "<h2>", "<h3>", "<h4>", "<p>"]

# go through the text in text_editor and highlight the words if they are in htmlSyntax
def highlight_html(event):
    text = text_editor.get(1.0, END)
    for word in htmlSyntax:
        if word in text:
            text_editor.tag_add("html", "1.0", END)
            text_editor.tag_config("html", foreground="#FF0000")

# while loop
while True:
    highlight_html(text_editor)
    root.update()

root.mainloop()