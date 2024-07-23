from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
            <html>
            <body>
                <h1>Enviar Datos</h1>
                <form action="/" method="post">
                    <label for="name">Nombre:</label>
                    <input type="text" id="name" name="name"><br><br>
                    <label for="email">Email:</label>
                    <input type="text" id="email" name="email"><br><br>
                    <input type="submit" value="Enviar">
                </form>
            </body>
            </html>
        """)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

        name = post_data.get('name')[0]
        email = post_data.get('email')[0]

        print(f'Nombre: {name}')
        print(f'Email: {email}')

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
            <html>
            <body>
                <h1>Datos recibidos</h1>
            </body>
            </html>
        """)

def run(server_class=HTTPServer, handler_class=MyServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
