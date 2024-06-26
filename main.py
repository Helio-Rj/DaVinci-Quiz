import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

# Config Janela
janela = tk.Tk()
janela.title('DaVinc QUIZ')
janela.geometry('400x450')

# Config Cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"

janela.config(bg=background_color)
janela.option_add('*Font','Arial')

janela.mainloop()


