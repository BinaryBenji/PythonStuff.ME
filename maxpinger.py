import os
import subprocess 

ips = ["10.10.10.197", "127.0.0.1"]
res = []

for ip in ips:
	print("Pinging " + ip)
	calls = subprocess.call("ping -c 2 " + ip, shell=True,  stdout=subprocess.PIPE)
	if calls == 1 :
		#print(ip + " is KO")
		res.append(1)
	else :
		#print(ip + " is OK")
		res.append(0)


for i, val in enumerate(res) :
	if res[i] == 1:
		print(ips[i] + " is KO")
	else:
		print(ips[i] + " is OK")

