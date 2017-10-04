print("Calcul du Levier & Elasticité \n\n")

cours = input("Entrez le COURS de l'action: ")
pwarr = input("Entrez le PRIX du Warrant (à l'unité): ")
parit = input("Entrez la PARITE du Warrant (x pour 1): ")
delta = input("Entrez le DELTA: ")


cours = float(cours)
pwarr = float(pwarr)
parit = float(parit)
delta = float(delta)
delta = delta/100

levier = cours / (pwarr*parit)
elast = levier * delta

print ("\nLe levier est de : %.2f" % levier)
print ("L'élasticité est de : %.1f%%" % elast)
print ("Le warrant gagnera %.1f%% lorsque le sous-jacent gagnera %.0f%%." % (elast,1))







