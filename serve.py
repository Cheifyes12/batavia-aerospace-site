#!/usr/bin/env python3
"""
Batavia Aerospace — Local Dev Server
Usage: python3 serve.py
Opens: http://localhost:8080
"""
import http.server, socketserver, os, webbrowser, threading, time

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # Uncomment the line below to see request logs:
        # print(f"  {args[0]} {args[1]}")
        pass

def open_browser():
    time.sleep(0.9)
    webbrowser.open(f"http://localhost:{PORT}")

print(f"\n  🚀  Batavia Aerospace dev server")
print(f"  →   http://localhost:{PORT}")
print(f"  →   Ctrl+C to stop\n")
threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
