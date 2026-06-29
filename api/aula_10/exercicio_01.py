from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.00}
]

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    
    novo_id = len(produtos) + 1
    
    novo_produto = {
        "id": novo_id,
        "nome": dados.get("nome"),
        "preco": dados.get("preco")
    }
    
    produtos.append(novo_produto)
    return jsonify(novo_produto), 21 

if __name__ == '__main__':
    app.run(debug=True)