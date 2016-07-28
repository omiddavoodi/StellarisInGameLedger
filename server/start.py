from ledger import makeLedgerForSave
import sys, os

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 12852

basePath = sys.argv[0][:sys.argv[0].rfind('start.py')]

f = open(basePath + 'base.html', 'r')
basehtml = f.read()
f.close()

path = 'C:/Python33/stellarisscorechecker/ver2/2204.01.07.sav'

class LedgerServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
##        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
##        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
##        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
##        self.wfile.write(bytes("</body></html>", "utf-8"))
        
        try:
            games = [i for i in os.listdir(path)]
            saves = []
            for i in games:
                
                svs = [path + '/' + i + '/' + j for j in os.listdir(path + '/' + i)]
                
                saves.extend(svs)
            if (len(saves)):
                least = saves[0]

                for i in range(1, len(saves)):
                    if (os.path.getmtime(saves[i]) > os.path.getmtime(least)):
                        least = saves[i]
                
                led = makeLedgerForSave(least, basePath)
                
                result = basehtml.replace('{{HERE}}', led)
                self.wfile.write(bytes(result, "utf-8"))
            else:
                self.wfile.write(bytes('No save found', "utf-8"))
        except:
            self.wfile.write(bytes('Internal server error', "utf-8"))


if (len(sys.argv) > 1):
    savespath = sys.argv[1]
    f = open(sys.argv[0][:sys.argv[0].rfind('start.py')] + 'path.txt', 'w')
    f.write(savespath)
    f.close()

    input("Path successfully configured.")
else:
    if (os.path.exists('path.txt')):
        f = open('path.txt', 'r')
        path = f.read()
        f.close()

        if (path[-1] == '/' or path[-1] == '\\'):
            path = path[:len(path)-1]
        
        myServer = HTTPServer((hostName, hostPort), LedgerServer)
        print("Server Starts - %s:%s" % (hostName, hostPort))

        try:
            myServer.serve_forever()
        except KeyboardInterrupt:
            pass

        myServer.server_close()
        print("Server Stops - %s:%s" % (hostName, hostPort))
    else:
        input("Error: Save directory path not set")
