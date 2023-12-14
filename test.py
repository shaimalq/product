from produit import*

# Création de produits élémentaires
p1 = ProduitElementaire("Produit 1", "P1", 10.0)
p2 = ProduitElementaire("Produit 2", "P2", 15.0)

print(p1)
print(p2)


p3 = ProduitCompose("Produit 3", "P3", 5.0)
p4 = ProduitCompose("Produit 4", "P4", 8.0)


p3.ajouterConstituant(Composition(p1, 2))
p3.ajouterConstituant(Composition(p2, 4))

p4.ajouterConstituant(Composition(p2, 3))
p4.ajouterConstituant(Composition(p1, 2))


print(p3)
print(p4)

print(f"Le prix HT de {p3.nom} est: {p3.getPrixHT()}")
print(f"Le prix HT de {p4.nom} est: {p4.getPrixHT()}")