import random;


class server:
    def __init__(self):
        self.ip = "undefined"
        self.netmask = "255.255.255.0"
        self.name = "Default Name"
        self.typ = ["super serveur", "mini serveur", "serveur titan"]

def decider(server):
    randnum = random.randrange(0,10)
    if (randnum < 5):
        server.ip = "192.168.0.3"
    return server

masterchef = server()
masterchef = decider(masterchef)

if masterchef.ip == "":
    print("Pas d'IP.")
else :
    print("IP OK : %s" % masterchef.ip)

print("Le nom de ce serveur est : %s" % (masterchef.name).lower())
print("Il a pour IP : %s" % masterchef.ip)
print("Son masque est : %s" % masterchef.netmask)
print("Le type de ce serveur est %s \n" %
      masterchef.typ[random.randrange(0,3)])

