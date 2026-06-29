from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    
    titulo = dados.get("titulo")
    
    if not titulo or str(titulo).strip() == "":
        return jsonify({"erro": "O titulo nao pode ser vazio"}), 400
        
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "feita": dados.get("feita", False) 
    }
    
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

if __name__ == '__main__':
    app.run(debug=True)