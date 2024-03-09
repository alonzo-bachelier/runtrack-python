nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]  # Liste des nombres à arrondir et trier

def arrondir_et_trier(liste):
    n = 0                                          # Compte le nombre d'éléments dans la liste
    for _ in liste:                                # Boucle pour calculer la longueur de la liste
        n += 1

    index = 0                                      # Index pour la boucle d'arrondissement
    while index < n:                               # Boucle pour arrondir chaque nombre de la liste
        nombre = liste[index]                      # Prend l'élément courant de la liste
        partie_entiere = 0                         # Initialise la partie entière du nombre
        while nombre >= 1:                         # Boucle pour isoler la partie entière du nombre
            nombre -= 1
            partie_entiere += 1
        if nombre >= 0.5:                          # Si la partie décimale est >= 0.5, arrondit à l'entier supérieur
            liste[index] = partie_entiere + 1
        else:                                      # Sinon, garde la partie entière
            liste[index] = partie_entiere
        index += 1

    i = 0                                          # Index pour la boucle de tri
    while i < n - 1:                               # Tri par sélection
        min_index = i                              # Indice du plus petit élément trouvé
        j = i + 1                                  # Comparaison à partir de l'élément suivant
        while j < n:                               # Parcourt le reste de la liste pour trouver le plus petit
            if liste[j] < liste[min_index]:
                min_index = j
            j += 1
        temp = liste[min_index]                    # Échange les éléments pour trier
        liste[min_index] = liste[i]
        liste[i] = temp
        i += 1

    return liste                                   # Retourne la liste triée et arrondie

resultat = arrondir_et_trier(nombres)              # Applique la fonction à la liste des nombres
print("Liste arrondie et triée :", resultat)       # Affiche le résultat
