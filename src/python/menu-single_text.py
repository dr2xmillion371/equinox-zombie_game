from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=1920, height=1080)#the geometry

canvas.create_text(123,123,text="welcome to the equinox zombie game!",fill='orange',
font=('Arial', 23))
