import socket
import threading


# Connect to server through 'HandShake'
def get_connect():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            # If 'HandShake' in message send to server nickname
            if message == 'HandShake':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


# Send to server
def get_send():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


if __name__ == '__main__':
    nickname = input("Choose your nickname: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))

    receive_thread = threading.Thread(target=get_connect)
    receive_thread.start()

    write_thread = threading.Thread(target=get_send)
    write_thread.start()
