import socket

header_size = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))


while True:


	full_msg = ''
	new_msg = True
	while True:
		msg = s.recv(16)
		if new_msg:
			print(f"new message length: {msg[:header_size]}")
			msglen = int(msg[:header_size])
			new_msg = False

		full_msg += msg.decode("utf-8")

		if len(full_msg) - header_size == msglen:
			print("full msg recvd")
			print(full_msg[header_size:])
			new_msg = True;
			full_msg = ''

	print(full_msg)