def f(l):                                      # Définit la fonction pour filtrer les doublons dans une liste
    res = []                                   # Initialise la liste des résultats sans doublons
    for i in l:                                # Parcourt chaque élément de la liste d'entrée
        if i not in res:                       # Vérifie si l'élément n'est pas déjà dans 'res'
            res += [i]                         # Ajoute l'élément à 'res' s'il n'est pas déjà présent
    return res                                 # Retourne la liste 'res' sans doublons

li = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40] # Liste d'entrée avec des doublons
resultat = f(li)                                  # Appelle la fonction 'f' avec 'li' et stocke le résultat dans 'resultat'
print(resultat)                                   # Imprime le résultat, qui est la liste sans doublons
