import socket
from main import DNS, root_server

IP = "0.0.0.0"
PORT = 5000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)


print(f"[+] DNS listening on {IP}:{PORT}")
sock.bind((IP, PORT))


dns_server = DNS(root_server)

while True:
    data, addr = sock.recvfrom(1024)
    print(f"[+] New connection from {addr}")

    domain_name = data.decode(encoding="utf-8")

    domain = dns_server.search(domain_name)

    msg = ""

    if domain:
        msg = domain.ipv4

    sock.sendto(
        msg.encode(),
        addr
    )
