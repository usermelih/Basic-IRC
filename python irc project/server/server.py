import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.lock = threading.Lock()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server {self.host}:{self.port} üzerinde dinleniyor...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Yeni bağlantı: {client_address}")
            
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
            self.clients.append(client_socket)

    def broadcast_message(self, message, sender_socket):
        with self.lock:
            for client_socket in self.clients:
                if client_socket != sender_socket:
                    try:
                        client_socket.sendall(message.encode('utf-8'))
                    except:
                        pass

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break

                print(f"Alınan mesaj: {message}")

                # Diğer kullanıcılara dağıt
                self.broadcast_message(message, client_socket)
            except:
                break

        client_socket.close()

if __name__ == "__main__":
    HOST = '0.0.0.0'  #buraya kendi bilgisayarınızın veya isteğe bağlı olarak sunucuyu çalıştırmak istediğiniz v4 ip adresinizi yazınız
    PORT = 44444

    server = ChatServer(HOST, PORT)
    server.start_server()
