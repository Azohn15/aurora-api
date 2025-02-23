from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    pergunta = data.get("pergunta", "")

    resposta = f"Aurora: Você disse '{pergunta}', mas ainda estou aprendendo!"
    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
