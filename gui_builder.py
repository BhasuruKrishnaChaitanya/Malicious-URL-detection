from tkinter import *
from tkinter import Canvas
from tkinter import Label
import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox
#from PIL import ImageTk

root = tk.Tk()
w=Label(root, text='URL Predictor--Malicious/Benign', font=("Helvetica", 16))
w.pack()
C =Canvas(root, height=250, width=300)
'''filename = ImageTk.PhotoImage(file ="project.jpg")
background_label = Label(root, image=filename)
background_label.place(x=0, y=30, relwidth=1, relheight=1)
w.pack()'''
C.pack()

class URL_Detector:
    def URL(string):
        string = textBox.get("1.0","end-1c")
        import predictor
        x = (predictor.prediction(string)) 
        w1 = Label(root, text=x, font=("Helvetica", 16))
        w1.pack()

a=URL_Detector()


u=Label(root, text='Enter URL', font=("Helvetica", 16))
u.pack()

textBox=Text(root, height=1, width=50)
textBox.pack()

result = Button(root , width=20, background='blue',foreground='white', text="Predict", command=lambda : a.URL())
result.pack()

button = tk.Button(root, text="Clear", command=lambda : clear_widget_text(w1))
button.pack()

root.mainloop()
