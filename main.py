from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('CyberKarty!')
root.geometry('1200x500')

'''
# Create definitions function
def definicje_zewnetrzne():
    pass

# Create player score function
def wyniki_gracz():
    pass

    '''

# Activate round
def activate_round():
    global clock
    clock = 0
    add_second()

# Create cyberkarty answers
def cyberkarty_answer():
    if capital_radio.get() == our_cyber_karty[answer]:
        response = "Prawidłowa odpowiedź!"
        cyber_karty()
    else:
        response = "Błędna odpowiedź! Spróbuj ponownie"

    answer_label_capitals.config(text=response)
        
#Create State Capital Flashcard Function
def cyber_karty():
    global clock
    clock = 0
    
    # Hide previous frames
    hide_all_frames()
    cyber_karty_frame.pack(fill="both", expand=1)
    
    global show_state
    show_state = Label(cyber_karty_frame)
    show_state.pack(pady=15)

    global our_numbers
    our_numbers = [1, 2, 3, 4, 5, 6]

    global our_cyber_karty
    our_cyber_karty = {
    1: 'Phishing',
    2: 'Wirus',
    3: 'Botnet',
    4: 'Firewall',
    5: 'DDoS',
    6: 'Antywirus',
    7: 'Haker',
    8: 'Malware',
    9: 'VPN',
    10: 'Bezpieczeństwo_informacji',
    11: 'Ransomware',
    12: 'Spyware',
    13: 'Zabezpieczenia_sieciowe',
    14: 'Weryfikacja_dwuetapowa',
    15: 'Filtrowanie_treści',
    16: 'Bezpieczeństwo_aplikacji'
    }

    global definitions_cyber
    definitions_cyber = {
    1: 'próba oszukania użytkownika przez podszywanie się pod zaufaną osobę lub organizację w celu pozyskania poufnych informacji',
    2: 'program komputerowy, który ma na celu infekowanie innych plików komputerowych w celu rozprzestrzeniania się i powodowania szkód',
    3: 'zdecentralizowana sieć zainfekowanych komputerów, które mogą być zdalnie sterowane przez cyberprzestępców do wykonywania złośliwych działań',
    4: 'system zabezpieczeń sieciowych, który kontroluje ruch sieciowy i chroni sieć przed niepożądanym dostępem',
    5: 'atak polegający na przeciążeniu serwera lub sieci przez wysłanie wielu zapytań z różnych źródeł, co prowadzi do spadku wydajności lub nawet do całkowitej przerwy w dostępie',
    6: 'program komputerowy, który wykrywa, blokuje i usuwa wirusy komputerowe',
    7: 'osoba, która używa swoich umiejętności informatycznych do nieuprawnionego dostępu do systemów informatycznych lub sieci',
    8: 'oprogramowanie złośliwe, które jest projektowane w celu szkodzenia systemom komputerowym lub sieciom',
    9: 'wirtualna sieć prywatna, która umożliwia bezpieczne połączenie między dwoma punktami na sieci publicznej, takiej jak Internet',
    10: 'praktyki i procedury zapobiegające nieautoryzowanemu dostępowi do informacji poufnych lub tajemnic handlowych',
    11: 'atak polegający na szyfrowaniu plików lub całych dysków twardych użytkownika, po czym cyberprzestępcy żądają okupu w zamian za odzyskanie dostępu do danych',
    12: 'program komputerowy, który zbiera poufne informacje o użytkowniku bez jego wiedzy lub zgody',
    13: 'procedury i narzędzia służące do ochrony sieci przed niepożądanymi atakami i zagrożeniami',
    14: 'proces weryfikacji tożsamości użytkownika za pomocą dwóch niezależnych metod, takich jak hasło i kod wysłany na telefon',
    15: 'proces blokowania niepożądanych treści, takich jak spam, złośliwe linki lub nieodpowiednie materiały',
    16: 'praktyki, procesy i narzędzia stosowane w celu zapewnienia ochrony aplikacji przed nieautoryzowanym dostępem, naruszeniem integralności danych, utratą poufności informacji oraz innymi zagrożeniami związanymi z ich wykorzystaniem'
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
            state_text = definitions_cyber[answer_list[0]].capitalize()
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

    global clock_label
    clock_label = Label(cyber_karty_frame, text=clock)
    clock_label.pack(pady=20)

    activate_round()

    

# Add clock to game
def add_second():
    global clock
    clock += 1
    global clock_label
    clock_label["text"] = clock
    clock_label.after(1000, add_second)

#Hide all previous frames
def hide_all_frames():
    # Loop through and destroy all children in previous frames
    for widget in cyber_karty_frame.winfo_children():
        widget.destroy()

    cyber_karty_frame.pack_forget() 

#Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Geography menu items
cyber_menu = Menu(my_menu)
my_menu.add_cascade(label="Moduły", menu=cyber_menu)
#cyber_menu.add_command(label="Dodaj definicję", command=definicje_zewnetrzne)
#cyber_menu.add_command(label="Moje wyniki", command=wyniki_gracz)
cyber_menu.add_command(label="CyberKarty", command=cyber_karty)
cyber_menu.add_separator()
cyber_menu.add_command(label="Wyjście", command=root.quit)

# Create our Frames
cyber_karty_frame = Frame(root, width=500, height=500)


root.mainloop()