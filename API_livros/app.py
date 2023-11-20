from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulos': 'O senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J. K. Rowling'
    }, 
    
    {
        'id': 3,
        'titulo': 'Hábitos Clear',
        'autor': 'James Clear'
    }
]

# Consultor(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultar(id)
@app.route('/livros/<int:id>') #Espera um número inteiro com palavra chave id
def obter_livro_por_id(id):
    for livro in livro:
        if livro.get('id') == id:
            return jsonify(livro)
#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros', methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)