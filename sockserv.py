import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 50500))


while True:
	server.listen(5)
	client, address = server.accept()
	print("{} connected".format(address))

	response = client.recv(255)
	if len(response) :
		print(response)
	server.send(b"WB")

print("Closed.")

client.close()
stock.close()

