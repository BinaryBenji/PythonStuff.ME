import os
import time

i = 0

#Hosts List
hostname = ["youtube.fr", "riot.de"]

print("##################\n")
print("### Ping Check ###\n")
print("##################\n\n")

#Ping requests
while i < len(hostname) :
    print("-- " + hostname[i] + " --\n")
    response = os.system("ping " + hostname[i] + " -n 5 | findstr -i Minimum")
    if response == 0:
        print ('    Ping is OK ! :D\n\n')
    else:
        print ('    Ping is K.O. :(\n\n')
    i+=1
os.system('pause')
