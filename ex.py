def check_chaine(chaine) :
    tab = list(chaine)
    i = 0
    while i < len(chaine):
        if tab[i] != 'a' and tab[i] != 't' and tab[i] != 'g' and tab[i] != 'c' :
            error = 1
            print ('error')
            break
        else :
            i+=1

error = 0
adn = input("Enter chain : ")
check_chaine(adn)
if error == 1:
    exit

minichain = input("Enter sequence : ")

rs = 0
save = 0
while rs < len(adn) or rs == 0:
    print ("ok");
    print (rs)
    save = rs
    
    rs = adn.find(minichain, rs)
    if rs <= save :
        exit
    
