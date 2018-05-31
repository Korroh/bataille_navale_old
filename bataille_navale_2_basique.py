#--------------
# fonction Stan
#--------------

def choix_joueur_J1():
    """
    Demande au joueur la case a torpiller
    depart: True si c'est au lancement du jeu, False si c'est en cours de jeu
    choix_lettre: numero de la colonne correspondant au choix du joueur
    choix_chiffre: numero de la ligne correspondant au choix du joueur
    """
    global depart, nb_bateau_places

    verif_lettre = False
    while verif_lettre == False:
        if depart == True: # Au lancement du jeu
            if nb_bateau_places >= 0 and nb_bateau_places <= 3:
                choix_lettre = input("Indiquer la colonne (lettre) ou vous voulez placer un morceau de votre croiseur (4 cases) :")
            elif nb_bateau_places >= 4 and nb_bateau_places <= 6:
                choix_lettre = input("Indiquer la colonne (lettre) ou vous voulez placer un morceau de votre contre-torpilleur (3 cases) :")
            elif nb_bateau_places >= 7 and nb_bateau_places <= 8:
                choix_lettre = input("Indiquer la colonne (lettre) ou vous voulez placer un morceau de votre torpilleur (2 cases) :")
        elif depart == False: # Durant la partie
            choix_lettre = input("Choisissez la colonne (lettre) que vous voulez torpillez :")

        # Diffeentes possibilites que le joueur peut donner
        if choix_lettre == 'A' or choix_lettre == 'a': # Si le joueur donne la lettre A ou a
            choix_lettre = 3 # La lettre se transforme en le numero de la colonne correspondante
            verif_lettre = True # On arrete la boucle qui verifie si le joueur donne une bonne lettre
        elif choix_lettre == 'B' or choix_lettre == 'b':
            choix_lettre = 5
            verif_lettre = True
        elif choix_lettre == 'C' or choix_lettre == 'c':
            choix_lettre = 7
            verif_lettre = True
        elif choix_lettre == 'D' or choix_lettre == 'd':
            choix_lettre = 9
            verif_lettre = True
        elif choix_lettre == 'E' or choix_lettre == 'e':
            choix_lettre = 11
            verif_lettre = True
        elif choix_lettre == 'F' or choix_lettre == 'f':
            choix_lettre = 13
            verif_lettre = True
        elif choix_lettre == 'G' or choix_lettre == 'g':
            choix_lettre = 15
            verif_lettre = True
        elif choix_lettre == 'H' or choix_lettre == 'h':
            choix_lettre = 17
            verif_lettre = True
        else: # Si le joueur n'a pas saisi une lettre compris dans le plan d'eau
            print("Vous n'avez pas saisi une lettre comprise entre A et H (inclus)") # On affiche ce texte et la boucle qui demande la lettre recommence

    verif_chiffre = False
    while verif_chiffre == False:
        if depart == False: # Durant la partie
            try:
                choix_chiffre = int(input("Choisissez la case (chiffre) que vous voulez torpillez :"))
            except ValueError: # Au cas ou le joueur donne autre chose qu'un entier
                print("Vous n'avez pas donne de chiffre")
                continue # On relance la boucle
        elif depart == True: # Au lancement du jeu
            try:
                if nb_bateau_places >= 0 and nb_bateau_places <= 3:
                    choix_chiffre = int(input("Indiquer la ligne (chiffre) ou vous voulez placer un morceau de votre croiseur (4 cases) :"))
                elif nb_bateau_places >= 4 and nb_bateau_places <= 6:
                    choix_chiffre = int(input("Indiquer la ligne (chiffre) ou vous voulez placer un morceau de votre contre-torpilleur (3 cases) :"))
                elif nb_bateau_places >= 7 and nb_bateau_places <= 8:
                    choix_chiffre = int(input("Indiquer la ligne (chiffre) ou vous voulez placer un morceau de votre torpilleur (2 cases) :"))
            except ValueError:
                print("Vous n'avez pas donne de chiffre")
                continue

        choix_chiffre = choix_chiffre*2 # La ligne correspondante equivaut a 2*le chiffre donne
        if choix_chiffre >= 2 and choix_chiffre <= 16: # Si le chiffre est compris entre la ligne 2 et 16, autrement dit entre les lignes 1 et 8 du plan d'eau
            verif_chiffre = True # On arrete la boucle
        else: # Sinon
            print("Vous n'avez pas saisi un nombre compris entre 1 et 8 (inclus)") # On affiche ce texte et on relance la boucle

    if depart == True: # Si c'est au lancement du jeu
        verification_placement_depart_J1(choix_chiffre, choix_lettre)
    elif depart == False: # Si c'est durant la partie
        verification_torpille_J1(choix_chiffre, choix_lettre)


def verification_placement_depart_J1(choix_chiffre, choix_lettre):
    """
    Permet de verifier le placement de nos navires
    plan_decouvert_J1: notre plan d'eau decouvert
    nb_bateau_places: nombre de morceau de navire place
    M, L, K: morceau de navire
    """
    global plan_decouvert_J1, nb_bateau_places, depart, choix_chiffre_1, choix_lettre_1, choix_chiffre_2, choix_lettre_2, choix_chiffre_3, choix_lettre_3, choix_chiffre_4, choix_lettre_4, choix_chiffre_5, choix_lettre_5, choix_chiffre_6, choix_lettre_6


    if plan_decouvert_J1[choix_chiffre][choix_lettre] == " ": # Si la case choisi est une case vide alors

        # Pour le croiseur M (4 cases)
        if nb_bateau_places == 0: # Si le nombre de bateau place est de 0 alors
            # On remplace la case correspondante par un "M", c'est a dire un morceau de croiseur
            plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "M" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
            plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
            choix_chiffre_1 = choix_chiffre
            choix_lettre_1 = choix_lettre
        elif nb_bateau_places == 1: # Si le nombre de bateau place est de 1 alors
            # Il faut que le nouveau morceau de navire soit a cote d'un autre morceau
            if choix_chiffre == choix_chiffre_1-2 or choix_chiffre == choix_chiffre_1+2 or choix_lettre == choix_lettre_1-2 or choix_lettre == choix_lettre_1+2:
                plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "M" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
                plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
                choix_chiffre_2 = choix_chiffre
                choix_lettre_2 = choix_lettre
            else: # Si le nouveau morceau n'est pas a cote d'un autre morceau
                print("Vous devez placer votre morceau de navire a coter d'un autre morceau de navire") # On affiche cela
                choix_joueur_J1() # Et on appelle la fonction choix_joueur_J1 pour recommencer l'emplacement du navire
        elif nb_bateau_places == 2:
            if choix_chiffre == choix_chiffre_1-2 and choix_chiffre == choix_chiffre_2-4 or choix_chiffre == choix_chiffre_2-2 and choix_chiffre == choix_chiffre_1-4 or choix_chiffre == choix_chiffre_1+2 and choix_chiffre == choix_chiffre_2+4 or choix_chiffre == choix_chiffre_2+2 and choix_chiffre == choix_chiffre_1+4 or choix_lettre == choix_lettre_1-2 and choix_lettre == choix_lettre_2-4 or choix_lettre == choix_lettre_2-2 and choix_lettre == choix_lettre_1-4 or choix_lettre == choix_lettre_1+2 and choix_lettre == choix_lettre_2+4 or choix_lettre == choix_lettre_2+2 and choix_lettre == choix_lettre_1+4:
                plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "M" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
                plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
                choix_chiffre_3 = choix_chiffre
                choix_lettre_3 = choix_lettre
            else:
                print("Vous devez placer votre morceau de navire a coter et dans la meme direction que les autres morceaux")
                choix_joueur_J1()
        elif nb_bateau_places == 3:
            if choix_chiffre == choix_chiffre_1-2 and choix_chiffre == choix_chiffre_2-4 and choix_chiffre == choix_chiffre_3-6 or choix_chiffre == choix_chiffre_1-2 and choix_chiffre == choix_chiffre_3-4 and choix_chiffre == choix_chiffre_2-6 or choix_chiffre == choix_chiffre_2-2 and choix_chiffre == choix_chiffre_1-4 and choix_chiffre == choix_chiffre_3-6 or choix_chiffre == choix_chiffre_3-2 and choix_chiffre == choix_chiffre_1-4 and choix_chiffre == choix_chiffre_2-6 or choix_chiffre == choix_chiffre_3-2 and choix_chiffre == choix_chiffre_2-4 and choix_chiffre == choix_chiffre_1-6 or choix_chiffre == choix_chiffre_2-2 and choix_chiffre == choix_chiffre_3-4 and choix_chiffre == choix_chiffre_1-6 or choix_chiffre == choix_chiffre_1+2 and choix_chiffre == choix_chiffre_2+4 and choix_chiffre == choix_chiffre_3+6 or choix_chiffre == choix_chiffre_1+2 and choix_chiffre == choix_chiffre_3+4 and choix_chiffre == choix_chiffre_2+6 or choix_chiffre == choix_chiffre_2+2 and choix_chiffre == choix_chiffre_1+4 and choix_chiffre == choix_chiffre_3+6 or choix_chiffre == choix_chiffre_3+2 and choix_chiffre == choix_chiffre_1+4 and choix_chiffre == choix_chiffre_2+6 or choix_chiffre == choix_chiffre_3+2 and choix_chiffre == choix_chiffre_2+4 and choix_chiffre == choix_chiffre_1+6 or choix_chiffre == choix_chiffre_2+2 and choix_chiffre == choix_chiffre_3+4 and choix_chiffre == choix_chiffre_1+6 or choix_lettre == choix_lettre_1-2 and choix_lettre == choix_lettre_2-4 and choix_lettre == choix_lettre_3-6 or choix_lettre == choix_lettre_1-2 and choix_lettre == choix_lettre_3-4 and choix_lettre == choix_lettre_2-6 or choix_lettre == choix_lettre_2-2 and choix_lettre == choix_lettre_1-4 and choix_lettre == choix_lettre_3-6 or choix_lettre == choix_lettre_3-2 and choix_lettre == choix_lettre_1-4 and choix_lettre == choix_lettre_2-6 or choix_lettre == choix_lettre_3-2 and choix_lettre == choix_lettre_2-4 and choix_lettre == choix_lettre_1-6 or choix_lettre == choix_lettre_2-2 and choix_lettre == choix_lettre_3-4 and choix_lettre == choix_lettre_1-6 or choix_lettre == choix_lettre_1+2 and choix_lettre == choix_lettre_2+4 and choix_lettre == choix_lettre_3+6 or choix_lettre == choix_lettre_1+2 and choix_lettre == choix_lettre_3+4 and choix_lettre == choix_lettre_2+6 or choix_lettre == choix_lettre_2+2 and choix_lettre == choix_lettre_1+4 and choix_lettre == choix_lettre_3+6 or choix_lettre == choix_lettre_3+2 and choix_lettre == choix_lettre_1+4 and choix_lettre == choix_lettre_2+6 or choix_lettre == choix_lettre_3+2 and choix_lettre == choix_lettre_2+4 and choix_lettre == choix_lettre_1+6 or choix_lettre == choix_lettre_2+2 and choix_lettre == choix_lettre_3+4 and choix_lettre == choix_lettre_1+6:
                plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "M" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
                plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
            else:
                print("Vous devez placer votre morceau de navire a coter et dans la meme direction que les autres morceaux")
                choix_joueur_J1()

        # Pour le contre-torpilleur L (3 cases)
        if nb_bateau_places == 4:
            plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "L" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
            plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
            choix_chiffre_4 = choix_chiffre
            choix_lettre_4 = choix_lettre
        elif nb_bateau_places == 5:
            if choix_chiffre == choix_chiffre_4-2 or choix_chiffre == choix_chiffre_4+2 or choix_lettre == choix_lettre_4-2 or choix_lettre == choix_lettre_4+2:
                plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "L" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
                plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
                choix_chiffre_5 = choix_chiffre
                choix_lettre_5 = choix_lettre
            else:
                print("Vous devez placer votre morceau de navire a coter et dans la meme direction que les autres morceaux")
                choix_joueur_J1()
        elif nb_bateau_places == 6:
            if choix_chiffre == choix_chiffre_4-2 and choix_chiffre == choix_chiffre_5-4 or choix_chiffre == choix_chiffre_5-2 and choix_chiffre == choix_chiffre_4-4 or choix_chiffre == choix_chiffre_4+2 and choix_chiffre == choix_chiffre_5+4 or choix_chiffre == choix_chiffre_5+2 and choix_chiffre == choix_chiffre_4+4 or choix_lettre == choix_lettre_4-2 and choix_lettre == choix_lettre_5-4 or choix_lettre == choix_lettre_5-2 and choix_lettre == choix_lettre_4-4 or choix_lettre == choix_lettre_4+2 and choix_lettre == choix_lettre_5+4 or choix_lettre == choix_lettre_5+2 and choix_lettre == choix_lettre_4+4:
                plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "L" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
                plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
            else:
                print("Vous devez placer votre morceau de navire a coter et dans la meme direction que les autres morceaux")
                choix_joueur_J1()

        # Pour le torpilleur K (3 cases)
        if nb_bateau_places == 7:
            plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "K" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
            plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
            choix_chiffre_6 = choix_chiffre
            choix_lettre_6 = choix_lettre
        elif nb_bateau_places == 8:
            if choix_chiffre == choix_chiffre_6-2 or choix_chiffre == choix_chiffre_6+2 or choix_lettre == choix_lettre_6-2 or choix_lettre == choix_lettre_6+2:
                plan_decouvert_J1_ligne = plan_decouvert_J1[choix_chiffre][:choix_lettre] + "K" + plan_decouvert_J1[choix_chiffre][choix_lettre+1:]
                plan_decouvert_J1 = plan_decouvert_J1[:choix_chiffre] + [plan_decouvert_J1_ligne] + plan_decouvert_J1[choix_chiffre+1:]
            else:
                print("Vous devez placer votre morceau de navire a coter et dans la meme direction que les autres morceaux")
                choix_joueur_J1()

    else: # Si un morceau de navire est deja a cet emplacement
        print("Vous avez deja place un morceau de navire a cet emplacement")
        choix_joueur_J1() # On relance la fonction choix_joueur_J1


def verification_torpille_J1(choix_chiffre, choix_lettre):
    """
    Permet de verifier si l'on touche ou non un navire
    torpille: nombre de torpille lance
    plan_cache_J2: plan d'eau adverse cache
    plan_decouvert_J2: plan d'eau adverse decouvert
    M, L, K: morceau de navire
    #: tir effectue et cible atteinte
    X: tir effectue mais aucune cible atteinte
    """
    global torpille, score, plan_cache_J2, plan_decouvert_J2

    if plan_decouvert_J2[choix_chiffre][choix_lettre] == "M" or plan_decouvert_J2[choix_chiffre][choix_lettre] == "L" or plan_decouvert_J2[choix_chiffre][choix_lettre] == "K": # Si a la case choisi il y'a un morceau de navire sur le plan d'eau adverse
        # On modifie les plans d'eau adverse en ajoutant le tir effectue
        plan_cache_J2_ligne = plan_cache_J2[choix_chiffre][:choix_lettre] + "#" + plan_cache_J2[choix_chiffre][choix_lettre+1:]
        plan_cache_J2 = plan_cache_J2[:choix_chiffre] + [plan_cache_J2_ligne] + plan_cache_J2[choix_chiffre+1:]

        plan_decouvert_J2_ligne = plan_decouvert_J2[choix_chiffre][:choix_lettre] + "#" + plan_decouvert_J2[choix_chiffre][choix_lettre+1:]
        plan_decouvert_J2 = plan_decouvert_J2[:choix_chiffre] + [plan_decouvert_J2_ligne] + plan_decouvert_J2[choix_chiffre+1:]

        # On modifie les scores et le nombre de torpille lance
        torpille = torpille + 1
        score = score + 1

    elif plan_decouvert_J2[choix_chiffre][choix_lettre] == ' ':
        plan_cache_J2_ligne = plan_cache_J2[choix_chiffre][:choix_lettre] + "X" + plan_cache_J2[choix_chiffre][choix_lettre+1:]
        plan_cache_J2 = plan_cache_J2[:choix_chiffre] + [plan_cache_J2_ligne] + plan_cache_J2[choix_chiffre+1:]

        plan_decouvert_J2_ligne = plan_decouvert_J2[choix_chiffre][:choix_lettre] + "X" + plan_decouvert_J2[choix_chiffre][choix_lettre+1:]
        plan_decouvert_J2 = plan_decouvert_J2[:choix_chiffre] + [plan_decouvert_J2_ligne] + plan_decouvert_J2[choix_chiffre+1:]

        torpille = torpille + 1

    elif plan_decouvert_J2[choix_chiffre][choix_lettre] == 'X': # Si la case choisie a deja ete torpillee
        print("Vous avez deja torpiller cette case, veuillez recommencer")
        choix_joueur_J1() # On relance la fonction choix_joueur_J1



#--------------
# fonction Hugo
#--------------

def affiche_eau_J1():
    global plan_cache_J2, plan_decouvert_J1

    for i in range(len(plan_cache_J2)):
      print(plan_cache_J2[i])
    for i in range(len(plan_decouvert_J1)):
      print(plan_decouvert_J1[i])

def charge_eau():
    try:
        fichier1 = open("plan_eau_1_cache.txt","r")
        fichier2 = open("plan_eau_1_vide.txt","r")
        plan_cache = fichier1.readlines()
        plan_decouvert = fichier2.readlines()
        plan_cache_J1 = [i.replace('\n','') for i in plan_cache]
        plan_cache_J2 = [i.replace('\n','') for i in plan_cache]
        plan_decouvert_J1 = [i.replace('\n','') for i in plan_decouvert]
        plan_decouvert_J2 = [i.replace('\n','') for i in plan_decouvert]
        return plan_cache_J1, plan_cache_J2, plan_decouvert_J1, plan_decouvert_J2
    except FileNotFoundError:
        print("Impossible d'ouvrir les fichiers !")

def ligne_etat() :
    print("Votre score est de :",score)
    print("Vous avez tire :", torpille, "torpille(s)")



#--------------------
# Programme principal
#--------------------

plan_cache_J1, plan_cache_J2, plan_decouvert_J1, plan_decouvert_J2 = charge_eau()
depart = True
torpille = 0
score = 0
nb_bateau_places = 0

choix_chiffre_1 = 0
choix_lettre_1 = 0
choix_chiffre_2 = 0
choix_lettre_2 = 0
choix_chiffre_3 = 0
choix_lettre_3 = 0
choix_chiffre_4 = 0
choix_lettre_4 = 0
choix_chiffre_5 = 0
choix_lettre_5 = 0
choix_chiffre_6 = 0
choix_lettre_6 = 0

choix_chiffre_1_J2 = 0
choix_lettre_1_J2 = 0
choix_chiffre_2_J2 = 0
choix_lettre_2_J2 = 0
choix_chiffre_3_J2 = 0
choix_lettre_3_J2 = 0
choix_chiffre_4_J2 = 0
choix_lettre_4_J2 = 0
choix_chiffre_5_J2 = 0
choix_lettre_5_J2 = 0
choix_chiffre_6_J2 = 0
choix_lettre_6_J2 = 0

i = 0

while True:
    affiche_eau_J1()
    choix_joueur_J1()
    if depart == True:
        nb_bateau_places += 1 # Le morceau de navire est place donc on ajoute 1 au nombre de morceau places
    if nb_bateau_places == 9: # Si l'on a place tout les morceaux de navire
        depart = False # Le lancement est termine
    ligne_etat()