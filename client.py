import socket
import time

# Function to create a TCP connection to the server
def connect_to_server(port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    
    try:
        client_socket.connect(('IP_address', port))  # Replace with the server's IP address
        print(f'[+] Connected to server on port {port}')
    except ConnectionRefusedError:
        print(f'[-] Failed to connect to server on port {port}')
        return None
    

    return client_socket

#client_socket = connect_to_server(12345)
#time.sleep(5)
#client_socket_2 = connect_to_server(34567)
# Send/receive data through the client_socket 

#client_socket.close()
#time.sleep(5)
#client_socket_2.close()

available_ports = [0, 12345, 23456, 34567]

def main():
    print("Welcome client")
    progress = True
    while(progress):
        print("Choose action")
        print("1. Attempt server connection    2. Exit")
        n = int(input())
        if n == 1:
            print("Choose port number to connect to")
            print("1. 12345    2. 23456.    3.34567")
            port_no = int(input())
            print("Attempting connection to port ", available_ports[port_no])
            client_soc = connect_to_server(available_ports[port_no])
            time.sleep(2)
            #if(type(client_soc == None)):
            #    print("Could not connect to server. DOSd")
            #else:
            client_soc.close()
            print("[-] Connection closed")
        elif n == 2:
            print("Server misses you")
            progress = False
        else: 
            print("Enter valid choice")
main()
