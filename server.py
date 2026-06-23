import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    print(f"Starting server in directory: {DIRECTORY}")
    
    # Enable socket reuse to avoid "address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"Server successfully started at: {url}")
        print("Press Ctrl+C to terminate.")
        
        # Automatically launch the default web browser to the application page
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Could not automatically open browser: {e}")
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
