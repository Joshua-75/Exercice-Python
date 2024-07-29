# tp : Jeu du Juste Prix
# Choisir un nombre entre 1 et 1000
#while choose_number != good_number:
# tant que le jeu n'est pas fini
#   -> demander à l'utilisateur "entrer un prix"
#   -> si il trouve le juste prix "c'est gagné !"
#   -> sinon on affiche "c'est moins" ou "c'est plus"

good_number = 69

choose_number = int(input("Choisissez un nombre entre 1 et 1000: "))

while choose_number != good_number:

    if choose_number < good_number:
        print("C'est plus !")
    elif choose_number > good_number:
        print("C'est moins")

    choose_number = int(input("Choisissez un nombre entre 1 et 1000: "))

print("Oui, oui ,oui Et c'est gagné !!")