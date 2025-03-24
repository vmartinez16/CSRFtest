# CSRFtest
Test con Flask
Aplicación web que simula un ataque CSRF y su protección con tokens.

 ************************Requisitos previos ************************
Python 3.8+ instalado
pip (gestor de paquetes de Python)
pip install flask flask-wtf (flask-wtf para instalar la solución)

 ************************Estructura del proyecto ************************
/proyecto-csrf/
├── app.py                # Backend Flask (servidor)
├── templates/
│   └── index.html        # Landing page (página vulnerable)
└── static/
    ├── style.css         # Estilos CSS
    ├── jordan1.jpg       # Imagen de los tenis
    ├── nike.png          # Logo de Nike
    └── favicon.ico       # Icono de la pestaña (opcional)

 ************************ Ejecución ************************
1. Inicia el servidor Flask: python app.py
2. Abre tu navegador en:

http://localhost:5000/login (simula inicio de sesión).

http://localhost:5000/landing (página con el botón de "oferta").

 ************************¿Qué hace este proyecto? ************************
Simula un ataque CSRF:

La landing page tiene un botón que envía una petición oculta a /comprar.

Sin protección, este endpoint procesaría la acción sin validación.

Protección con tokens CSRF:

El archivo app.py usa Flask-WTF para generar tokens únicos.

El formulario en index.html incluye {{ csrf_token() }} para validar peticiones.




 ************************Modo seguro (con CSRF habilitado) ************************
El endpoint /comprar solo acepta peticiones POST con token válido.

Si se desactiva CSRF en app.py, el ataque sería exitoso.
