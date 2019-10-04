import socket

header_size = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been establish")
	msg = "Welcome to the server"
	msg = f'{len(msg):<{header_size}}' + msg

	clientsocket.send(bytes(msg, "utf-8"))
	
