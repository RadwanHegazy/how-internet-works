import socket


DNS_IP = "127.0.0.1"
DNS_PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

domain_name = "google.org"


sock.sendto(
    domain_name.encode(),
    (DNS_IP, DNS_PORT)
)

msg, addr = sock.recvfrom(1024)
domain_ip = msg.decode()

if domain_ip:
    print(f"[+] IP FOR {domain_name} is : {domain_ip}")
else:
    print(f"[-] IP NOT EXISTS")
