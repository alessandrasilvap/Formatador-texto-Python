from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    texto = ""

    if request.method == "POST":
        texto = request.form["texto"]
        opcao = request.form["opcao"]

        if opcao == "maiusculo":
            resultado = texto.upper()

        elif opcao == "minusculo":
            resultado = texto.lower()

        elif opcao == "capitalizar":
            frases = texto.lower().split(".")
            frases = [f.strip().capitalize() for f in frases]
            resultado = ". ".join(frases)

        elif opcao == "espacos":
            resultado = " ".join(texto.split())

    return render_template("index.html", resultado=resultado, texto=texto)

if __name__ == "__main__":
    app.run(debug=True)
