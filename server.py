import socket
import threading
from scapy import *

IP_ADDRESS = '0.0.0.0'  # Bind to all available network interfaces
PORTS = [12345, 23456, 34567]  # List of port numbers to listen on

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f'[+] New connection from {client_address[0]}:{client_address[1]}')

    # Send a welcome message to the client
    client_socket.send(b'Welcome to the server!\n')

    # Close the client socket
    client_socket.close()
    print(f'[-] Connection closed with {client_address[0]}:{client_address[1]}')

# Create a socket for each port and bind it to the IP address
for port in PORTS:
    # Create a new socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP address and port number
    server_socket.bind((IP_ADDRESS, port))

    # Start listening for incoming connections
    server_socket.listen(5)

    print(f'[*] Listening on {IP_ADDRESS}:{port}')

    # Accept incoming connections in a loop
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
def detect_syn_flood(pcap_file):
    
    packets = rdpcap(pcap_file)
    source_ips = {}
    syn_packets = []
    for packet in packets:
        if IP in packet and TCP in packet:
            if packet[TCP].flags == 'S':
                syn_packets.append(packet)
                source_ip = packet[IP].src
                if source_ip in source_ips:
                    source_ips[source_ip] += 1
                else:
                    source_ips[source_ip] = 1