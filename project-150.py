# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:33:09 2022

@author: Keviweto
"""

from tkinter import *
import random

root=Tk()
root.title("Random Countries And Capitals")
root.geometry("900x750")

enter_country = Entry(root)
enter_country.place(relx = 0.5, rely = 0.2, anchor = CENTER)
enter_capital = Entry(root)
enter_capital.place(relx=0.5, rely=0.3, anchor = CENTER)

country_list = Label(root)
capital_list = Label(root)

random_country = Label(root)
random_capital = Label(root)

list_country = []
list_capital = []

def country_capital():
    country = enter_country.get()
    list_country.append(country)
    country_list["text"] = "Country Name " + str(list_country)
    capital = enter_capital.get()
    list_capital.append(capital)
    capital_list["text"] = "Capital Name " + str(list_capital) 
    
def random_country_capital():
    length1 = len(list_country)
    random_no1 = random.randint(0, length1-1)
    random_country["text"] = str(random_no1)
    generated_country = list_country[random_no1]
    country_list["text"]="Random Country : " + str(generated_country)
    length2 = len(list_capital)
    random_no2 = random.randint(0, length2-1)
    random_capital["text"] = str(random_no2)
    generated_capital = list_capital[random_no2]
    capital_list["text"]="Random Country : " + str(generated_capital)
    


    
btn = Button(root, text = "Add To The List", command = country_capital)
btn.place(relx = 0.5, rely=0.4, anchor = CENTER)

country_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)
capital_list.place(relx = 0.5, rely = 0.6, anchor = CENTER)

btn2 = Button(root, text="Generate Random Country And Capital?" , command = random_country_capital)
btn2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

random_country.place(relx= 0.5, rely = 0.7, anchor = CENTER)
random_capital.place(relx= 0.5, rely = 0.8, anchor = CENTER)

random_country.place(relx=0.5, rely=0.9, anchor = CENTER)
random_capital.place(relx=0.5, rely=0.10, anchor = CENTER)

root.mainloop()