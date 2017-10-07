lst = [7,6,4]
find = []
i = 0;
s = 8


def findme(i, s, lst):    
    while (i < len(lst)):
        if (s - lst[i] in find) :
            return True;
        else :
            find.append(lst[i])
        i = i + 1
    return False;

if (findme(i, s, lst)):
    print ("OK")
else :
    print("KO")

