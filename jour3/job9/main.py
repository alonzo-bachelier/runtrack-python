def moyenne(note1, note2, note3):
    moyenne = (note1 + note2 + note3)/3
    return moyenne

note1 = float(input("Entrez la premiere note : "))
note2 = float(input("Entrez la seconde note : "))
note3 = float(input("Entrez la troisieme note : "))

resultat = moyenne(note1, note2, note3)
print("La moyenne est :", resultat)

if resultat >= 15 and resultat <=20:
    print('aaliyah la plus forte')
elif resultat >= 11 and resultat <= 14:
    print("aaliyah n'est plus la plus forte")
elif resultat >= 8 and resultat <= 10:
    print("Aaliyah n'est pas tres studieuse")
elif resultat >=0 and resultat <= 7:
    print("Aaliyah farquaad")
    

