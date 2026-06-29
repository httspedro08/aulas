from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.00, "disponivel": True},
    {"id": 2, "nome": "Mouse Gamer", "preco": 150.00, "disponivel": False},
    {"id": 3, "nome": "Monitor 24'", "preco": 899.90, "disponivel": True},
    {"id": 4, "nome": "Headset USB", "preco": 180.00, "disponivel": True}
]

@app.route('/produtos/disponiveis', methods=['GET'])
def obter_produtos_disponiveis():
    produtos_filtrados = []
    
    for produto in produtos:
        if produto["disponivel"] == True:
            produtos_filtrados.append(produto)
            
    return jsonify(produtos_filtrados)

if __name__ == '__main__':
    app.run(debug=True)