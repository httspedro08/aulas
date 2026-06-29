from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'loja.db'

def conectar_banco():
    return sqlite3.connect(DATABASE)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = conectar_banco()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, nome, preco FROM produtos')
    linhas = cursor.fetchall()
    conn.close()
    
    produtos = []
    for linha in linhas:
        produtos.append({
            'id': linha[0],
            'nome': linha[1],
            'preco': linha[2]
        })
        
    return jsonify(produtos), 200

@app.route('/produtos', methods=['POST'])
def inserir_produto():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'preco' not in dados:
        return jsonify({'erro': 'Nome e preço são obrigatórios.'}), 400
        
    nome = dados['nome']
    preco = dados['preco']
    
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
    conn.commit()
    
    novo_id = cursor.lastrowid
    conn.close()
    
    produto_criado = {
        'id': novo_id,
        'nome': nome,
        'preco': preco
    }
    
    return jsonify(produto_criado), 201

if __name__ == '__main__':
    app.run(debug=True)