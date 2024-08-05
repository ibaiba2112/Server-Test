import http.server
import socketserver

# directory = "for_yixuan"

# handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", port,), handler) as httpd:
#     print("Server started LocalHost at port: " + str(port))
#     httpd.serve_forever()



# class customHTTPHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/":
#             self.path = "test.html"
#             print("Server started LocalHost at port: " + str(port))
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)

# port = 8080
# hanlder_object = customHTTPHandler

# server_trial = socketserver.TCPServer(("", port), hanlder_object)

# server_trial.serve_forever()



import http.server # Import the server classes and functionality from http module, this is all request handling, GET POST etc
import socketserver # This imports things like TCPservers or UDPServers, these are transport protocols

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler): 
    """
    CustomHTTPHandler is a class I made that INHERITS from the SimpleHTTPRequestHandler class
    the parent(SimpleHTTPRequestHandler) class comes from the http.server module
    """

    def do_GET(self): #do_Get() method is used in handling get request, but more so for custom get requests like the one we have here 
        if self.path == "/": # if the path starts with "/"
            self.path = "for_yixuan" # redirect the path to the folder in the project called "for_yixuan"
        return super().do_GET() # this overrides parent class method and calls the custom do_Get() function

port = 8080 # port I'm using
handler_object = CustomHTTPHandler # the class CustomHTTPHanlder created an object instance which the one I will be using


with socketserver.TCPServer(("", port), handler_object) as httpd:
    """
    The socketserver library is using a TCP connection
    the "" is the network spec so it is basically looking out for any netowkr connections, so anybody can join and any device can join
    the port is 8080 so it will only work on port 8080
    assigning all this tcp connection is condensed as httpd
    """
    print("Server started LocalHost at port: " + str(port))
    httpd.serve_forever() # create and run the run server forever until the admin stops it