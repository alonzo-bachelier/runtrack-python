def my_long_word(n, phrase):
    mots = ['']                                # Initialise une liste avec un élément vide pour stocker les mots
    index_mot = 0                              # Index pour le mot actuel dans 'mots'
    phrase += ' '                              # Ajoute un espace à la fin pour capturer le dernier mot

    for caractere in phrase:                   # Parcourt chaque caractère de la phrase
        if caractere == ' ':                   # Si le caractère est un espace
            if mots[index_mot] != '':          # Vérifie si le mot actuel n'est pas vide
                mots += ['']                   # Ajoute un nouvel élément vide pour le prochain mot
                index_mot += 1                 # Incrémente l'index pour passer au prochain mot
        else:
            mots[index_mot] += caractere       # Ajoute le caractère au mot actuel

    mots_filtres = ''                          # Initialise une chaîne vide pour les mots filtrés
    premier_mot = True                         # Indicateur pour le premier mot ajouté à 'mots_filtres'

    for mot in mots:                           # Parcourt chaque mot dans 'mots'
        longueur_mot = 0                       # Initialise le compteur de longueur pour le mot
        for caractere in mot:                  # Calcule la longueur du mot
            longueur_mot += 1
        if longueur_mot > n:                   # Si la longueur du mot est plus grande que 'n'
            if not premier_mot:                # Si ce n'est pas le premier mot, ajoute un espace avant
                mots_filtres += ' '
            mots_filtres += mot                # Ajoute le mot à 'mots_filtres'
            premier_mot = False                # Met à jour 'premier_mot' pour les prochains mots
    
    return mots_filtres                        # Retourne la chaîne des mots filtrés

phrase_exemple = "La peur est le chemin vers le côté obscur , la peur mène à la colère , la colère mène à la haine , la haine mène à la souffrance"
resultat = my_long_word(3, phrase_exemple)     # Appelle la fonction avec une phrase exemple et 'n' = 3
print("Output :", resultat)                    # Imprime les mots de la phrase dont la longueur est > à 'n'
