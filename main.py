import socket

# Make a phone call
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dial the phone. Dialing it to the domain and the port
my_socket.connect(("pypi.org", 443))

# Now sending the command cmd, a variable which has a UTF-8 string in it
cmd = "GET https://pypi.org/project/sockets/ HTTP/1.0\r\n\r\n".encode()
my_socket.send(cmd)

# We are receiving data until the socket is closed.
while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=" ")

my_socket.close()
