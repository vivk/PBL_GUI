from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import tkinter.font as tkFont
import subprocess
from PIL import ImageTk, Image

exec = 'dep/chemistry.exe'

root = Tk()
root.title('Chemix')
root.geometry('680x610')
root.configure(background='#3E435F')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Chemistry Files', '*.c4')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Chemistry Files', '*.c4')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        code_output.delete('1.0', END)
        code_output.insert('1.0', "Please Save your Code!")
        return
    code_output.delete('1.0', END)
    # command = f'./dep/chemistry.exe \'{file_path}\''
    # with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as process:
    #     output, error = process.communicate()
    #     code_output.insert('1.0', process.returncode)
    #     code_output.insert('1.0',  error)

    process = subprocess.run([exec, file_path], capture_output=True, text=True)
    if (process.returncode == 0):
        code_output.insert('1.0', process.stdout)
    else:
        code_output.insert('1.0', process.stderr)



menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)
run_bar = Menu(menu_bar, tearoff=0)

root.config(menu=menu_bar)

# logo configuration
logo = ImageTk.PhotoImage(Image.open("Logo/logo.png"))
logo_label = Label(image=logo, width=180, height=50, bg="#3E435F")
logo_label.pack()

fontExample = tkFont.Font(family="Segoe UI Semilight", size=10,
                          weight="bold",)
# code editor
editor = Text(height=20, bg="#565C7B", fg="#CDD3EA",
              borderwidth=0, font=fontExample)
editor.pack()

# run button
run_button = Button(text="RUN", fg="#CDD3EA", bg="#383B4E",
                    borderwidth=0, height=1, width=6, activebackground="#CDD3EA", command=run)
run_button.pack()

# Console
code_output = Text(height=10, bg="#565C7B", fg="#CDD3EA",
                   borderwidth=0, font=fontExample)
code_output.pack()

root.mainloop()
