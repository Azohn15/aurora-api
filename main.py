import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    if request.method == "POST":
        try:
            data = request.json  # Pega os dados JSON da requisição
            # Aqui você pode processar os dados recebidos e gerar a resposta.
            # Exemplo simples de resposta:
            response = {
                "message": "Olá, Aurora está pronta para conversar!",
                "input": data
            }
            return jsonify(response), 200  # Retorna a resposta como JSON
        except Exception as e:
            return jsonify({"error": str(e)}), 400  # Caso ocorra algum erro, retorna um erro 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
