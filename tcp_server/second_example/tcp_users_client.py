import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
client_socket.send("Привет, сервер!".encode())

print(f"Ответ от сервера: {client_socket.recv(1024).decode()}")
client_socket.close()
