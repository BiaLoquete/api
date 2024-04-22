from flask import Flask, jsonify, request
from main import app, db
from models import Livro

@app.route('/livro', methods=['GET'])
def get_livro():
    livros = Livro.query.all()
    livros_dic = []
    for livro in livros:
        livro_dic = {
            'id_livro' : livro.id_livro,
             'titulo' : livro.titulo,
             'autor' : livro.autor,
             'ano_publicacao' : livro.ano_publicacao
        }
        livros_dic.append(livro_dic)

    #retorna dicionario em formato json
    return jsonify(
            mensagem= 'Lista de Livros',
            livros= livros_dic
        )