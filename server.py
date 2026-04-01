#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    print(f"Abra http://localhost:{PORT} no seu navegador")
    print("Pressione Ctrl+C para parar")
    httpd.serve_forever()
