import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class CustomBrowser(QWidget):
    _PORT_LIST = {
        'google.com' : 8000,
        'facebook.com' : 8001,
        'python.org' : 8002,
    }

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Custom Browser')
        self.setGeometry(300, 300, 800, 600)

        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter domain (e.g. python.org)...")
        self.url_input.returnPressed.connect(self.query_dns) 
        top_layout.addWidget(self.url_input)

        self.search_btn = QPushButton('Search', self)
        self.search_btn.clicked.connect(self.query_dns)
        top_layout.addWidget(self.search_btn)

        layout.addLayout(top_layout)

        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)

        self.web_view.setHtml("<h3>Welcome to your Custom Browser! Enter a domain above.</h3>")

        self.setLayout(layout)

        
    def query_dns(self): 
        domain_name = self.url_input.text().strip()

        if '/' in domain_name:
            domain_name, path = domain_name.split('/', maxsplit=1)
            path = "/" + path
        else:
            path = "/"

        if not domain_name:
            return 

        ipv4 = self.get_ip_by_domain_name(domain_name)

        if ipv4:
            self.web_view.setHtml(f"<h1>IP for domain {domain_name} is {ipv4}</h1>")
            self.start_tcp_connection(
                ipv4,
                port= self._PORT_LIST[domain_name] ,
                path=path
            )
        else:
            self.web_view.setHtml(f"<h1>IP not exists</h1>")



    def start_tcp_connection(self, ipv4 : str, port : int, path : str ) : 
        print(f"[=] Create tcp connection with {ipv4}:{port}{path}")

        soc = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        soc.connect((ipv4, port))

        http_request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {ipv4}\r\n"
            "Connection: close\r\n\r\n"
        )

        
        print(http_request)
        print(f"[=] Sending HTTP Request to {ipv4}:{port}")
        soc.sendall(http_request.encode(encoding="utf-8"))

        http_response = soc.recv(1024).decode()

        http_response = http_response.split('\r\n\r\n')[1]
        self.web_view.setHtml(http_response)
        soc.close()


    def get_ip_by_domain_name(self, domain_name : str) -> str : 


        DNS_IP = "127.0.0.1"
        DNS_PORT = 5000

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )


        sock.sendto(
            domain_name.encode(),
            (DNS_IP, DNS_PORT)
        )

        msg, addr = sock.recvfrom(1024)
        domain_ip = msg.decode()

        sock.close()

        return domain_ip


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = CustomBrowser()
    browser.show()
    sys.exit(app.exec_())