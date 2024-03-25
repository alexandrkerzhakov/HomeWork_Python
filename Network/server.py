import socket
import threading


# Sending messages to all connected clients
def get_send(message):
    for client in clients:
        client.send(message)


# Handling messages from clients
def get_handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            get_send(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            get_send('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


# Authorization through 'HandShake'
def get_authorizations_client():
    client, address = server.accept()
    print("Connected with {}".format(str(address)))

    # Request And Store Nickname
    client.send('HandShake'.encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    clients.append(client)

    # Print And Broadcast Nickname
    print("Nickname is {}".format(nickname))
    get_send("{} joined!".format(nickname).encode('ascii'))
    client.send('Connected to server!'.encode('ascii'))
    return client


# Receiving / Listening Function
def get_receive():
    while True:
        client = get_authorizations_client()

        # Start Handling Thread For Client
        thread = threading.Thread(target=get_handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 55555))
    server.listen()

    clients = []
    nicknames = []

    print("Server if listening...")
    get_receive()
