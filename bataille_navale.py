from random import randint
# initialisation du plateau de jeu
plateau = []

for x in range(0, 5):	# taille 5x5
	plateau.append(["O"] * 5)

def afficher_plateau(plateau):
	for ligne in plateau:
		print (" ".join(ligne))

afficher_plateau(plateau)

def alea_ligne(plateau):
    return randint(0, len(plateau) - 1)

def alea_col(plateau):
    return randint(0, len(plateau[0]) - 1)

bateau_x = alea_ligne(plateau)
bateau_y = alea_col(plateau)

nbdetours = 10

for i in range(nbdetours+1):
    
    tir_x = int(input("Quelle ligne ?"))
    tir_y = int(input("Quelle colonne ?"))

    if tir_x == bateau_x and tir_y == bateau_y:
        print ("Bravo. Vous avez eu mon bateau.")
        plateau[bateau_x][bateau_y] = "B"
        afficher_plateau(plateau)
        break
    else:
        if (tir_x < 0 or tir_x > 4) or (tir_y < 0 or tir_y > 4):
            print ("Oups ! Vous devez viser l'ocean.")
        elif(plateau[tir_x ] [tir_y ] == "X"):
            print ("Cette case est deja decouverte.")
        else:
            print ("Dommage !")
            plateau[tir_x ][tir_y ] = "X"
        print (i)
    if i > (nbdetours - 1):
        print ("Game Over")
        plateau[bateau_x] [bateau_y] = "B"
    afficher_plateau(plateau)