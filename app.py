from flask import Flask, render_template, request, session
#from flask_wtf.csrf import CSRFProtect
#csrf = CSRFProtect(app)

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # Necesario para sesiones

# Simulamos que el usuario está logueado (cookie de sesión activa)
@app.route("/login")
def login():
    session["autenticado"] = True
    return "Sesión iniciada. Ahora visita http://localhost:5000/landing."

# Landing page falsa (Nike)
@app.route("/landing")
def landing():
    return render_template("index.html")

# Endpoint vulnerable a CSRF (no verifica token)
@app.route("/comprar")
def comprar():
    if not session.get("autenticado"):
        return "Error: No autorizado", 403
    
    producto = request.args.get("producto")
    cantidad = request.args.get("cantidad")
    
    # ¡Aquí se procesaría la compra en un sistema real!
    print(f"[+] Compra fraudulenta: {cantidad} unidades de {producto}")
    
    return f"Compra realizada: {cantidad} x {producto}"

if __name__ == "__main__":
    app.run(port=5000, debug=True)