# MVPX - Página Web Corporativa

## 📋 Análisis del Proyecto

Este es un sitio web corporativo creado con **Webflow** que presenta una plataforma de servicios financieros y musicales llamada "MVPX". 

### 🎯 Propósito del Sitio
- **Gestión de derechos musicales**
- **Distribución musical** en más de 200 plataformas
- **Contratos digitales** automatizados
- **Reclamación de regalías** y derechos conexos

### 🏗️ Estructura Técnica

#### Tecnologías Utilizadas:
- **HTML5** - Estructura semántica
- **CSS3** - Estilos responsivos con Webflow
- **JavaScript** - Interactividad y animaciones
- **GSAP** - Animaciones avanzadas
- **Swiper.js** - Carousels de testimonios
- **jQuery** - Manipulación DOM y efectos

#### Características Destacadas:
1. **Diseño Responsivo** - Adaptable a móviles y tablets
2. **Animaciones Suaves** - Usando GSAP y ScrollTrigger
3. **Interfaz Moderna** - Design system consistente
4. **Optimización de Imágenes** - Múltiples resoluciones para performance

### 📊 Secciones Principales

1. **Hero Section** - Presentación principal con call-to-action
2. **Servicios** - Cards explicativas de los servicios ofrecidos
3. **Características** - Beneficios del ecosistema MVPX
4. **Sobre Nosotros** - Estadísticas y propuesta de valor
5. **Testimonios** - Carrusel de opiniones de usuarios
6. **Contacto** - Call-to-action final con botones de descarga

### 🎨 Paleta de Colores
- **Principal**: `#111111` (Negro)
- **Secundario**: `#696969` (Gris)
- **Fondo**: `#F3F5F5` (Gris claro)
- **Acentos**: Gradientes radiales y colores de cards

## 🚀 Despliegue Local

### Opción 1: Servidor Python (Recomendado)
```bash
# Ejecutar el servidor incluido
python3 server.py
```
El navegador se abrirá automáticamente en `http://localhost:8080`

### Opción 2: Servidor HTTP Simple
```bash
# Python 3
python3 -m http.server 8080

# Python 2
python -m SimpleHTTPServer 8080

# Node.js (si tienes npx)
npx serve . -p 8080
```

### Opción 3: Live Server (VS Code)
1. Instala la extensión "Live Server"
2. Click derecho en `index.html` → "Open with Live Server"

## 📁 Estructura de Archivos

```
mvpx-viti.webflow/
├── index.html              # Página principal
├── server.py              # Servidor local incluido
├── README.md              # Este archivo
├── css/
│   ├── mvpx-viti.webflow.css    # Estilos principales
│   ├── normalize.css            # Reset CSS
│   └── webflow.css             # Framework Webflow
├── js/
│   └── webflow.js              # Scripts de Webflow
└── images/                     # Todas las imágenes del sitio
    ├── favicon.ico
    ├── webclip.png
    └── [múltiples imágenes optimizadas]
```

## 🔧 Personalización

### Modificar Contenido
- **Textos**: Editar directamente en `index.html`
- **Estilos**: Modificar `css/mvpx-viti.webflow.css`
- **Imágenes**: Reemplazar archivos en la carpeta `images/`

### Configuraciones Importantes
- **Puerto del servidor**: Modificar `PORT = 8080` en `server.py`
- **Fuentes**: Inter font cargada desde Google Fonts
- **Animaciones**: Configuradas con GSAP en el script inline

## 🌐 Despliegue en Producción

### Opciones Recomendadas:
1. **Netlify** - Drag & drop la carpeta completa
2. **Vercel** - Conectar con el repositorio de GitHub
3. **GitHub Pages** - Activar en configuración del repo
4. **Firebase Hosting** - `firebase deploy`

### Para GitHub Pages:
1. Subir todos los archivos al repositorio
2. Ir a Settings → Pages
3. Seleccionar "Deploy from a branch" → main branch
4. El sitio estará disponible en `https://username.github.io/repository-name`

## 📱 Responsive Design

El sitio está optimizado para:
- **Desktop**: 1360px+ (diseño completo)
- **Tablet**: 768px - 1359px (layout adaptado)
- **Mobile**: < 768px (stack vertical, elementos simplificados)

## ⚡ Performance

### Optimizaciones Implementadas:
- Imágenes en múltiples resoluciones (srcset)
- CSS minificado
- JavaScript externo cacheado (CDN)
- Lazy loading para imágenes

### Métricas Esperadas:
- **Tiempo de carga**: < 3 segundos
- **First Contentful Paint**: < 1.5 segundos
- **Largest Contentful Paint**: < 2.5 segundos

## 🐛 Solución de Problemas

### Problemas Comunes:
1. **Puerto ocupado**: Cambiar el puerto en `server.py`
2. **Imágenes no cargan**: Verificar rutas relativas
3. **Animaciones no funcionan**: Verificar conexión a CDN de GSAP

### Debugging:
- Abrir DevTools (F12) para ver errores de consola
- Verificar Network tab para recursos no cargados
- Comprobar responsive design con device toolbar

## 📞 Soporte

Si encuentras algún problema o necesitas personalización adicional, puedes:
1. Revisar la consola del navegador para errores
2. Verificar que todos los archivos estén en su lugar
3. Asegurar que las rutas de archivos sean correctas

---

**© 2025 MVPX - Todos los derechos reservados** 