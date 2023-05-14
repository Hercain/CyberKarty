from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('CyberKarty!')
root.geometry('800x800')

# Create definitions function
def definicje_zewnetrzne():
    pass

# Create player score function
def wyniki_gracz():
    pass

# Create state capital answers
def cyberkarty_answer():
    if capital_radio.get() == our_cyber_karty[answer]:
        response = "Prawidłowa odpowiedź!"
        cyber_karty()
    else:
        response = "Błędna odpowiedź! Spróbuj ponownie"
    answer_label_capitals.config(text=response)
        
#Create State Capital Flashcard Function
def cyber_karty():
    # Hide previous frames
    hide_all_frames()
    cyber_karty_frame.pack(fill="both", expand=1)
    #my_label = Label(cyber_karty_frame, text="Capitals").pack()
    
    global show_state
    show_state = Label(cyber_karty_frame)
    show_state.pack(pady=15)

    global our_numbers
    our_numbers = [1, 2, 3, 4, 5, 6]

    global our_cyber_karty
    our_cyber_karty = {
    1:"antywirus",
    2:"certyfikatSSL",
    3:"firewall",
    4:"hacker",
    5:"hasło",
    6:"spearphishing"
    }

    global definitions_cyber
    definitions_cyber = {
    1:"Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    2:"Suspendisse finibus ipsum quis placerat elementum.",
    3:"Nulla aliquam velit id laoreet lobortis.",
    4:"Donec vel arcu ut felis pharetra rhoncus.",
    5:"Nam suscipit nulla eget justo egestas, sed maximus lacus semper.",
    6:"Nulla vel eros vehicula ex bibendum pharetra.",
    }

    # Create empty answer list and counter
    answer_list = []
    count = 1
    global answer

    # Generate 3 random capitals
    while count < 5:
        rando = randint(0, len(our_numbers)-1)
        
        # Add our first selection to a new list
        answer_list.append(our_numbers[rando])

        # If first selection, make it our answer
        if count == 1:
            answer = our_numbers[rando]
            global state_text
            state_text = definitions_cyber[answer_list[0]]
            show_state.config(text=state_text)
            
        #Remove from old list
        our_numbers.remove(our_numbers[rando])

        # Shuffle our original list
        random.shuffle(our_numbers)

        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_cyber_karty[answer_list[0]])

    capital_radio_button1 = Radiobutton(cyber_karty_frame, text=our_cyber_karty[answer_list[0]].title(), variable=capital_radio, value=our_cyber_karty[answer_list[0]]).pack()
    capital_radio_button2 = Radiobutton(cyber_karty_frame, text=our_cyber_karty[answer_list[1]].title(), variable=capital_radio, value=our_cyber_karty[answer_list[1]]).pack()
    capital_radio_button3 = Radiobutton(cyber_karty_frame, text=our_cyber_karty[answer_list[2]].title(), variable=capital_radio, value=our_cyber_karty[answer_list[2]]).pack()
    capital_radio_button4 = Radiobutton(cyber_karty_frame, text=our_cyber_karty[answer_list[3]].title(), variable=capital_radio, value=our_cyber_karty[answer_list[3]]).pack()

    print(our_cyber_karty[answer_list[0]])

    # Add A Pass Button
    pass_button = Button(cyber_karty_frame, text="Pass", command=cyber_karty)
    pass_button.pack(pady=15)

    # Create a button to answer
    capital_answer_button = Button(cyber_karty_frame, text="Answer", command=cyberkarty_answer)
    capital_answer_button.pack(pady=15)

    #Create an answer label
    global answer_label_capitals
    answer_label_capitals = Label(cyber_karty_frame, text="", font=("Helvetica", 15))
    answer_label_capitals.pack(pady=15)

#Hide all previous frames
def hide_all_frames():
    # Loop through and destroy all children in previous frames
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in cyber_karty_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget() 
    cyber_karty_frame.pack_forget() 

#Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Geography menu items
cyber_menu = Menu(my_menu)
my_menu.add_cascade(label="Moduły", menu=cyber_menu)
cyber_menu.add_command(label="Dodaj definicję", command=definicje_zewnetrzne)
cyber_menu.add_command(label="Moje wyniki", command=wyniki_gracz)
cyber_menu.add_command(label="CyberKarty", command=cyber_karty)
cyber_menu.add_separator()
cyber_menu.add_command(label="Exit", command=root.quit)

# Create our Frames
state_frame = Frame(root, width=500, height=500, bg="white")
global cyber_karty_frame
cyber_karty_frame = Frame(root, width=500, height=500)

root.mainloop()