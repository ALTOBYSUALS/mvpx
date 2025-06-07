#!/usr/bin/env python3
from flask import Flask, send_from_directory, send_file
import os

app = Flask(__name__)

# Directorio raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """Sirve la página principal"""
    return send_file(os.path.join(ROOT_DIR, 'index.html'))

@app.route('/<path:filename>')
def serve_static(filename):
    """Sirve archivos estáticos"""
    return send_from_directory(ROOT_DIR, filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    """Sirve archivos CSS"""
    return send_from_directory(os.path.join(ROOT_DIR, 'css'), filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    """Sirve archivos JavaScript"""
    return send_from_directory(os.path.join(ROOT_DIR, 'js'), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    """Sirve imágenes"""
    return send_from_directory(os.path.join(ROOT_DIR, 'images'), filename)

@app.route('/fonts/<path:filename>')
def serve_fonts(filename):
    """Sirve fuentes"""
    return send_from_directory(os.path.join(ROOT_DIR, 'fonts'), filename)

@app.route('/videos/<path:filename>')
def serve_videos(filename):
    """Sirve videos"""
    return send_from_directory(os.path.join(ROOT_DIR, 'videos'), filename)

@app.errorhandler(404)
def not_found(error):
    """Maneja errores 404"""
    return send_file(os.path.join(ROOT_DIR, '404.html')), 404

if __name__ == '__main__':
    print("🚀 Servidor MVP X iniciado!")
    print("📱 Accede a: http://localhost:5000")
    print("🔧 Modo desarrollo con auto-reload")
    print("❌ Presiona Ctrl+C para detener")
    
    app.run(
        host='0.0.0.0',  # Permite acceso desde otros dispositivos en la red
        port=5000,
        debug=True,      # Auto-reload cuando cambies archivos
        threaded=True    # Soporte para múltiples conexiones
    ) 