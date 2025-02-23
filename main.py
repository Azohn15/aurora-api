import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=["POST"])
def chat():
    #código para requisição
    if __name__ == "__main__": 
    data = request.json
    pergunta = data.get("pergunta", "")

    resposta = f"Aurora: Você disse '{pergunta}', mas ainda estou aprendendo!"
    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
