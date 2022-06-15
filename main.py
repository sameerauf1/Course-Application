import markdown
from http.server import HTTPServer,BaseHTTPRequestHandler



class Serv(BaseHTTPRequestHandler): # class that hold server

    def do_GET(self):  # check path of get requeset

        # Rewrite some paths
        if self.path == '/':   #
            self.path = '/helloworld.html'  # path to index page

        if self.path.endswith(".md"):
            # Plain Markdown, translate to HTML and send
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            markdown.markdownFromFile(input=self.path[1:], output=self.wfile)

        elif self.path.endswith(".quiz"):
            # Quiz Markdown, translate to HTML form and send
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            markdown.markdownFromFile(input=self.path[1:], output=self.wfile)

        elif self.path.endswith(".html") or self.path.startswith("/res/"):
            # Plain HTML, send as is
            try:
                file_to_open = open(self.path[1:]).read()  
                self.send_response(200)  
            except:
                file_to_open = "File not found"  
                self.send_response(404)  
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))  

        else:
            self.send_response(404)
            self.end_headers()                         
        



httpd = HTTPServer(('localhost', 8080), Serv)   # httpd a program that runs in the background, local host
httpd.serve_forever()
