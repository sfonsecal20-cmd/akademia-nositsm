from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

base_conhecimento = {
    "gpm": "A Gestão de Processos de Mudança (GPM) gere e acompanha mudanças organizacionais.",
    "nosi": "A NOSi lidera a transformação digital em Cabo Verde.",
    "formacao": "A formação prepara utilizadores para novos sistemas.",
    "validacao": "A validação garante que o sistema funciona antes da produção.",
    "stage": "O ambiente de stage é usado para testes.",
    "producao": "O ambiente de produção é onde o sistema é usado pelos utilizadores finais."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "").lower()

    resposta = "Não encontrei essa informação no manual."

    for k in base_conhecimento:
        if k in msg:
            resposta = base_conhecimento[k]

    return jsonify({"response": resposta})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
