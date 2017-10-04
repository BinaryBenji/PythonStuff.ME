import bcrypt
import hashlib

class grec:
    contenu = "salade tomate oignons"
    sauce = "mayo"


print(grec.contenu + " sauce " + grec.sauce + " stp chef\n")

def impot_tamer(somme) :
    print("Je taxe que les pauvres comme un batarde")
    somme = somme - 1000
    if (somme < 10000) :
        print("Les impots vous ont mis dans la galere")
        return (0);
    else :
        return (somme)


liste = ["pingouin", "gobelet", "troiscinqsept", "champignon"]
listenb = [45, 5648, 7913]

i = 0;
j = 0;
somme = 0;

liste.remove(liste[2])
while (i < len(liste)) :
    print("Element no %d : %s" % (i, liste[i]))
    i+=1

while (j < len(listenb)) :
    somme = somme + listenb[j]
    j = j.__add__(1)

print("La somme totale : %d" % (somme))
listenb.append(56)

somme = listenb[j] + somme

print("\nSomme de tout maggle : %d" % (somme))

somme = impot_tamer(somme)
print("Apres l'impot : %d" % (somme))

pipi = b"divisionekippp"
caca = b"fumeleshit"

hashed_pipi = hashlib.sha256(pipi).hexdigest()
hashed_caca = bcrypt.hashpw(caca, bcrypt.gensalt(14))

print ("\nHashed pipi : %s" % (hashed_pipi))
print ("Hashed caca : %s" % (hashed_caca))







