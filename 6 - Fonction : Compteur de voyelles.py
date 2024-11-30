# Tp : Créer une fonction pour calculer le nombre de voyelles dans un mot 
# Définir une fonction get_vowels_numbers(mot)
# Créer un compteur de voyelles
# Pour chaque lettre du mot , vérifiez s'il s'agit d'une voyelle
# Si c'est le cas, on ajoute un au compteur 
# à la fin de la fonction, vous allez renvoyer le compteur 

def get_vowels_numbers(word):
   
   # compteur de voyelles 
    counter = 0 

    # Vérifie pour chaque lettre de mot , s'il s'agit d'une voyelle
    for letter in word:
        if letter in ['a','e','i','o','u','y', 'A',"E","I","O","U","Y"]:
            # On ajoute un au compteur / on incrémente de 1 au compteur
            counter = counter + 1
            
    return counter  # En fin de fonction , on renvoie le compteur
        
word = input ("Veuillez renseigner votre mot")

print("Dans le mot", word , "il y a" , get_vowels_numbers(word), "voyelles")


