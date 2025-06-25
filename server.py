#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import sys

# Port configuration
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def start_server():
    """Start a simple HTTP server to serve the static files"""
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 Servidor iniciado en: http://localhost:{PORT}")
            print(f"📁 Sirviendo archivos desde: {os.getcwd()}")
            print("💡 Presiona Ctrl+C para detener el servidor")
            
            # Abrir el navegador automáticamente
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Mantener el servidor corriendo
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Error: El puerto {PORT} ya está en uso")
            print("💡 Intenta cambiar el puerto o cerrar otros servidores")
        else:
            print(f"❌ Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server() 