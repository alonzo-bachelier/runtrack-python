# Création des variables représentant un produit
nom_du_produit = 'Monster Gold'
prix_unitaire = 1.99
quantite_en_stock = 50

# Affichage des informations du produit
print(f"Informations du produit :")
print(f"Nom du produit : {nom_du_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock} unités")

# Gestion de l'inflation sur le prix du produit
augmentation_prix = 0.10  # 10% d'augmentation
prix_unitaire *= (1 + augmentation_prix)

# Affichage des informations après l'inflation
print(f"\nInformations du produit après l'inflation :")
print(f"Nom du produit : {nom_du_produit}")
print(f"Nouveau prix unitaire (après inflation) : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock} unités")

# Demande à l'utilisateur de saisir la quantité qu'il souhaite acheter
quantite_demandee = int(input('\nCombien d\'unités souhaitez-vous acheter ? :'))

# Vérification si la quantité demandée est disponible en stock
if quantite_demandee <= quantite_en_stock:
    # Mettre à jour le stock après l'achat
    quantite_en_stock -= quantite_demandee
    montant_total = quantite_demandee * prix_unitaire
    print(f"\nAchat réussi ! Vous avez acheté {quantite_demandee} unités pour un montant de {montant_total} euros.")
    print(f"Quantité restante en stock : {quantite_en_stock} unités")
else:
    print("Achat impossible. La quantité demandée n'est pas disponible en stock.")

#demander a l'utilisateur d'ajouter des produits au stock
ajout_en_stock = int(input('\nCombien de produits souhaitez vous ajouter au stock ? :'))
quantite_en_stock += ajout_en_stock
stock_apres_ajout = ajout_en_stock + quantite_en_stock
stock_apres_ajout = quantite_en_stock
print(f'vous venez d\'ajouter {ajout_en_stock} unités!')
print(f'stock apres ajout {stock_apres_ajout}')


