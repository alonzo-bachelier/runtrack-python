#Initialiser deux variables, une pour le montant initial de l’investissement et une pour le taux de rendement annuel en pourcentage.
montant_initial_de_l_investissement = 50000
taux_de_rendement_annuel = 7

gain_annuel = (montant_initial_de_l_investissement * taux_de_rendement_annuel)/100
#Affichez en console le gain annuel en fonction du taux de rendement.
print(f'le gain annuel est de {gain_annuel}euros')

#L’investisseur augmente son capital de 5 000 euros, le taux augmente alors de 2%.
montant_initial_de_l_investissement += 5000
taux_de_rendement_annuel += 2

#Calculez à nouveau le gain de l’investisseur et affichez en console le résultat.
nouveau_gain_annuel = (montant_initial_de_l_investissement * taux_de_rendement_annuel)/100
print(f'le nouveau gain annuel est de {nouveau_gain_annuel}euros')

#L’investisseur retire 10% du montant total, suite à ce retrait, 
#le rendement diminue de 1%. Calculez le montant final de l’investissement et affichez le nouveau gain.
retrait_montant = 10 
montant_final_de_l_investissement = montant_initial_de_l_investissement - (montant_initial_de_l_investissement*retrait_montant/100)

retrait_rendement = 1
rendement_final_annuel = taux_de_rendement_annuel - (taux_de_rendement_annuel*retrait_rendement/100)

gain_annuel_final = (montant_final_de_l_investissement * rendement_final_annuel)/100
print(f'gain annuel final {gain_annuel_final}')



