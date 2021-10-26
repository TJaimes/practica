from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')#Te manda hasta la raiz del navegador
def index():
    objeto = {"nombre": "Tairi",
              "apellido": "Jaimes"
             }
    nombre = "Tairi"
    lista_nombres = ["Daniela", "Juan", "Raquel"]
    return render_template("index.html", variable = lista_nombres )

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()