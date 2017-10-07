import socket


host = sys.argv[1]
port = 50500


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print ("Connected on  {}".format(port))

client.send(b"Hello")


print("Closed.")
client.close()