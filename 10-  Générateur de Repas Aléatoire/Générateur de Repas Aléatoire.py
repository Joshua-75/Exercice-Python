import os
import random
from tkinter import *

def generate_meal():
    # Vérifie l'existence du fichier "meals.txt"
    if os.path.exists("meals.txt"):
        with open("meals.txt", "r+") as file:  # Ouvre le fichier "meals.txt" en mode lecture et écriture
            meals_list = file.readlines()  # Lit toutes les lignes du fichier et les stocke dans une liste
            if meals_list:  # Vérifie que la liste n'est pas vide
                meal_random_choice = random.choice(meals_list).strip()  # Sélectionne aléatoirement un repas et supprime les espaces inutiles
                result_label.config(text="Je vous propose aujourd'hui, le repas : " + meal_random_choice)
            else:
                # Met à jour le texte pour signaler que le fichier est vide
                result_label.config(text="Le fichier est vide ! Ajoutez des repas.")
    else:
        # Met à jour le texte pour signaler que le fichier n'existe pas
        result_label.config(text="Le document n'existe pas ! Faites attention !")

# Création de la fenêtre principal
window = Tk()
window.title("Générateur de Repas Aléatoire")
window.geometry("420x280")
window.config(bg="grey")

# Ajout d'un titre
label_title = Label(window,
                    text="Générateur de Repas",
                    font=("Helvetica", 20),
                    bg="grey",
                    fg="white"
                    )
label_title.pack()

# Création d'un bouton 
meals_button = Button(window,
                    font=("Helvetica", 20),
                    text="Cliquez-ici",
                    bg="grey",
                    fg="black",
                    command=generate_meal
                    )  
meals_button.pack() 

result_label = Label(window, 
                     text="", 
                     font=("Helvetica", 14))
result_label.pack(pady=20)                   

window.mainloop()

