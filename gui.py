##Lars Höhn

from pathlib import Path
import string
import random
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

bustabens = ""
zeichens = ""
numbers =""
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main():
    canvas.delete("error")
    canvas.delete("passwortgen")
    global bustabens
    global zeichens
    global numbers
    psw_random=""
    x=""
    letters = string.ascii_letters
    digits = string.digits
    letter_zeichen = string.punctuation
    if bustabens == "True":
        psw_random = letters
    if zeichens == "True":
        psw_random = psw_random + letter_zeichen
    if numbers == "True":
        psw_random = psw_random + digits
    try:
            for i in range(int(entry_1.get())):
                x = x + random.choice(psw_random)
            print(x)
    except:
        print("invalid lenght")
        canvas.create_text(
            627.0,
            823.0,
            anchor="nw",
            tags="error",
            text="invalid lenght",
            fill="#000000",
            font=("Quicksand Regular", 36 * -1)
        )
    canvas.delete("passwortgen")
    canvas.create_text(
        627.0,
        823.0,
        anchor="nw",
        tags="passwortgen",
        text=x,
        fill="#000000",
        font=("Quicksand Regular", 36 * -1)
    )



def unpack():
    global button_4

    button_4_pressed.place(
        x=0,
        y=0,
        width=0,
        height=0
    )
    bustabens = "false"
    print("bustaben flase")

def unpack_3():
    global button_3
    global zeichens
    button_3_pressed.place(
        x=0,
        y=0,
        width=0,
        height=0
    )
    zeichens = "false"
    print("zeichen flase")
def unpack_2():
    global button_2
    global numbers
    button_2_pressed.place(
        x=0,
        y=0,
        width=0,
        height=0
    )
    numbers= "false"
    print("number off")

window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main(),
    relief="flat"
)
button_1.place(
    x=623.0,
    y=886.0,
    width=208.88218688964844,
    height=68.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    985.0,
    299.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=943.0,
    y=282.0,
    width=84.0,
    height=33.0
)
def number():
    global numbers
    button_2_pressed.place(
        x=117.0,
        y=558.0,
        width=67.0,
        height=68.0
    )
    numbers= "True"
    print("numbers on")


def bustaben():
    global bustabens
    button_4_pressed.place(
        x=117.0,
        y=282.0,
        width=67.0,
        height=68.0
    )
    bustabens = "True"
    print("bustabens on")


def zeichen():
    global zeichens
    button_3_pressed.place(
        x=117.0,
        y=420.0,
        width=67.0,
        height=68.0
    )
    zeichens = "True"
    print("zeichen on")


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: number(),
    relief="flat"
)
button_2_pressed = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: unpack_2(),
    relief="flat"
)
button_2.place(
    x=117.0,
    y=558.0,
    width=67.0,
    height=68.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: zeichen(),
    relief="flat"
)

button_3_pressed = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: unpack_3(),
    relief="flat"
)
button_3.place(
    x=117.0,
    y=420.0,
    width=67.0,
    height=68.0
)

canvas.create_text(
    197.0,
    568.0,
    anchor="nw",
    text="Numbers\n",
    fill="#000000",
    font=("Quicksand Regular", 36 * -1)
)

canvas.create_text(
    197.0,
    431.0,
    anchor="nw",
    text="Zeichen\n",
    fill="#000000",
    font=("Quicksand Regular", 36 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: bustaben(),
    relief="flat"
)

button_4_pressed = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: unpack(),
    relief="flat"
)
button_4.place(
    x=117.0,
    y=282.0,
    width=67.0,
    height=68.0
)

canvas.create_text(
    197.0,
    293.0,
    anchor="nw",
    text="Bustaben\n",
    fill="#000000",
    font=("Quicksand Regular", 36 * -1)
)



canvas.create_text(
    96.0,
    90.0,
    anchor="nw",
    text="Passwort Generator\n",
    fill="#000000",
    font=("Quicksand SemiBold", 36 * -1)
)

canvas.create_text(
    939.0,
    235.0,
    anchor="nw",
    text="passlenght\n",
    fill="#000000",
    font=("Quicksand Regular", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
