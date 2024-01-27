import socket
import threading

class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client_socket.connect((self.host, self.port))
        print("Bağlandı.")

        # Sunucudan gelen mesajları dinle
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        # Kullanıcının girdiği mesajları gönder
        self.send_messages()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                print(message)
            except:
                break

    def send_messages(self):
        while True:
            message = input("")
            self.client_socket.sendall(f"{self.username}: {message}".encode('utf-8'))

    def close_connection(self):
        self.client_socket.close()

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Sunucu IP adresi
    PORT = 44444
    USERNAME = input("Kullanıcı adınızı girin: ")

    client = ChatClient(HOST, PORT, USERNAME)
    client.connect_to_server()
