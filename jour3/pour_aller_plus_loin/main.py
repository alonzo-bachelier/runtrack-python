def inverser_chaine(chaine):
    # Cette ligne inverse la chaîne de caractères en utilisant le slicing.
    # [::-1] signifie commencer au début de la chaîne (premier ':'),
    # aller jusqu'à la fin (deuxième ':') et le '-1' indique de le faire en ordre inverse.
    return chaine[::-1]

# Exemple d'utilisation de la fonction
exemple_chaine = "nikana"
chaine_inverse = inverser_chaine(exemple_chaine)
print(chaine_inverse)
