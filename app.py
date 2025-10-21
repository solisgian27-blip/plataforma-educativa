from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def about():
    return render_template('about.html')

@app.route('/contacto')
def contact():
    return render_template('contact.html')

# --- Punto de entrada principal ---
if __name__ == "__main__":
    # Render asigna automáticamente un puerto disponible en la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
