import os;
import subprocess

#os.popen("dir").read()
return_good = subprocess.call("echo Hello World", shell=True)
return_false = subprocess.call("eco Hello World", shell=True)
#return_code = subprocess.call("echo Hello World", shell=True)

print ("Good command return : %d" % return_good)
print ("Bad command return : %d" % return_false)

class lolilol :
    def __init__(self):
        self.lst = ["chocho", "enbal", "samere", "oulala", "shi", "alala"]


numbers = lolilol()
numbers.lst.sort()

print (numbers.lst)