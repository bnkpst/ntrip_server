
import socket


class TCPServer:
    def __init__(self, host='0.0.0.0', port=3000):
        self.host = host
        self.port = port

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(5)

        print("Listening at", s.getsockname())

        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            data = conn.recv(1024)

            response = self.handle_request(data)

            conn.sendall(response)
            conn.close()

    def handle_request(self, data):
                
        return data


class HTTPServer(TCPServer):

    def parse_headers(self, data):

        headers, sep, body = data.partition(b'\r\n\r\n')

        headers = headers.decode('latin1')
        print(headers)
        headers = headers.split('\r\n')

        for index, header in enumerate(headers):
            
            if(index == 0):
                print(header.split(' '))

            else:
                print(header.split(':'))






    def handle_request(self, data):

        self.parse_headers(data)

        response_line = b'HTTP/1.1 200 OK\r\n'

        headers = b''.join([
            b'Server: bnkpst ntrip server\r\n', 
            b'Ntrip-Version: Ntrip/2.0\r\n',
            b'Content-Type: text/plain\r\n'
        ])

        blank_line = b'\r\n'

        response_body = b'ENDSOURCETABLE'

        return b''.join([response_line, headers, blank_line, response_body])


if __name__ == '__main__':

    server = HTTPServer()

    server.start()