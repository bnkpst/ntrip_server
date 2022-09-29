
import socket


class TCPServer:
    def __init__(self, host='0.0.0.0', port=2101):
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

        response_line = b'ICY 200 OK\r\n'

        headers = b''.join([
            b'Server: bnkpst ntrip server\r\n', 
            b'Ntrip-Version: Ntrip/2.0\r\n',
            b'Content-Type: text/plain\r\n'
        ])

        blank_line = b'\r\n'

        response_body = b''.join([
            b'STR;Ben1;VRS-ben1;RTCM 3.0;1005(1),1033(1),1074(1),1084(1),1094(1),1124(1);2;GPS+GLONASS+BDS+GALILEO;eGPS;RUS;0.00;0.00;1;1;CPS;none;B;N;0;\r\n',
            b'STR;Ben2;VRS-ben2;RTCM 3.0;1005(1),1033(1),1004(1),1012(1),1104(1);2;GPS+GLONASS;eGPS;RUS;0.00;0.00;1;1;CPS;none;B;N;0;\r\n',
            b'ENDSOURCETABLE'
        ])

        return b''.join([response_line, headers, blank_line, response_body])

class NTRIPServer(HTTPServer):
    # TODO

    def serve_source_table():

        return b'source table'


if __name__ == '__main__':

    server = HTTPServer()

    server.start()