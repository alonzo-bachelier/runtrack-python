def tri_croissant(liste):
    n = 0                               # Initialisation du compteur pour la longueur de la liste
    for element in liste:
        n += 1                          # Calcule la longueur de la liste manuellement

    i = 0                               # Initialisation de l'index pour la boucle externe
    while i < n:                        # Boucle externe pour parcourir la liste
        j = 0                           # Initialisation de l'index pour la boucle interne
        while j < n - i - 1:            # Boucle interne pour comparer les éléments adjacents
            if liste[j] > liste[j + 1]: # Si l'élément courant est plus grand que le suivant
                temp = liste[j]         # Sauvegarde de l'élément courant
                liste[j] = liste[j + 1] # Échange des éléments
                liste[j + 1] = temp     # Réaffectation de l'élément sauvegardé
            j += 1                      # Incrémentation de l'index de la boucle interne
        i += 1                          # Incrémentation de l'index de la boucle externe

ma_liste = [99, 77, 88, 66, 55, 11, 33, 44, 22]          # Liste d'entiers non triée
tri_croissant(ma_liste)                                  # Appel de la fonction pour trier la liste
print("Liste triée dans l'ordre croissant :", ma_liste)  # Affichage de la liste triée
