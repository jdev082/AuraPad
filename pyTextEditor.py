from tkinter import *
from tkinter import filedialog

root = Tk()
# use theme clam
root.configure(background='#0D1117')
root.title("py3editor")
root.geometry("800x600")

def save_file(arg):
    file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    file = open(file_name, "w")
    file.write(text_editor.get(1.0, END))
    file.close()

save_button = Button(root, text="Save", command=lambda: save_file(text_editor))
exit_button = Button(root, text="Exit", command=root.destroy)
save_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
exit_button.configure(background='#0D1117', fg='#FFFFFF', highlightthickness='0', bd='0')
save_button.grid(row=0, column=0)
exit_button.grid(row=0, column=1)
text_editor = Text(root, width=100, height=30)
text_editor.configure(background='#0D1117', highlightthickness='0', bd='0', fg='#FFFFFF')
text_editor.grid(row=1, column=0, columnspan=2)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()