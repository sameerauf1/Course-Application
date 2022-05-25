
from http.server import HTTPServer,BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler): # class that hold server

    def do_GET(self):  # check path of get requeset
        if self.path == '/':   #
            self.path = '/helloworld.html'  # path to index page

        if self.path == '/potato':
            self.send_response(200)
            self.end_headers()
            resp.wfile.write(b'potato potato')
        else:
            try:
                file_to_open = open(self.path[1:]).read()   # .read to load text and read it
                self.send_response(200)   # 200 response if opening the webpage is sucessful
            except:
                file_to_open = "File not found"   # display file no tfound
                self.send_response(404)   # sent a 404 response that it was unsucessful
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))   # write contents of file to screen by converting to bytes


httpd = HTTPServer(('localhost', 8080), Serv)   # httpd a program that runs in the background, local host
httpd.serve_forever()