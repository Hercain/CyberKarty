from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('CyberKarty!')
root.geometry('600x500')

#Def states
def state_capitals():
    state_capitals_frame.pack(fill="both", expand=1)
    #my_label = Label(state_capitals_frame, text="Capitals").pack()
    
    global show_state
    show_state = Label(state_capitals_frame, text=value_def, font=("Helvetica", 15))
    show_state.pack(pady=15)

    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska', 'nevada', 'newyork', 'oregon', 'texas', 'vermont']

    global our_state_capitals
    our_state_capitals = {
    "1":"sacramento",
    "2":"tallahasee",
    "3":"springfield",
    "4":"frankfort",
    "5":"lincoln",
    "6":"carson city",
    "7":"albany",
    "8":"salem",
    "9":"austin",
    "10":"montpelier"
    }

    definitions_cyber = {
    "1":"Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "2":"Suspendisse finibus ipsum quis placerat elementum.",
    "3":"Nulla aliquam velit id laoreet lobortis.",
    "4":"Donec vel arcu ut felis pharetra rhoncus.",
    "5":"Nam suscipit nulla eget justo egestas, sed maximus lacus semper.",
    "6":"Nulla vel eros vehicula ex bibendum pharetra.",
    "7":"Suspendisse tempor tellus at velit elementum, sit amet hendrerit nisi luctus.",
    "8":"Donec rutrum ex ac justo ultrices accumsan.",
    "9":"Donec vel enim ac sem semper tincidunt.",
    "10":"Fusce in odio ut massa elementum feugiat ac ut eros." 
    }
    rando = randint(0, len(our_state_capitals)-1)
    
    value_def = definitions_cyber.values(rando)

    

#Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

states_menu = Menu(my_menu)
my_menu.add_cascade(label="Moduły", menu=states_menu)
states_menu.add_command(label="CyberKarty", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Wyjście", command=root.quit)

# Create our Frames
global state_frame
state_frame = Frame(root, width=500, height=500, bg="white")
global state_capitals_frame
state_capitals_frame = Frame(root, width=500, height=500)

root.mainloop()