import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=["POST"])
def chat():
    try:
        data = request.json  # Pega os dados JSON da requisição
        pergunta = data.get("pergunta", "")

        # Resposta gerada pela Aurora
        resposta = f"Aurora: Você disse '{pergunta}', mas ainda estou aprendendo!"
        
        # Retorna a resposta como JSON
        return jsonify({"resposta": resposta}), 200  

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Retorna erro 400 se algo der errado

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))