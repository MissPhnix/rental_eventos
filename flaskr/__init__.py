import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    @app.route('/teste')
    def teste():
        return 'Testando Flask'

    @app.route('/cadastroUsuario', methods=('GET','POST'))
    def novoUsuario():
        if request.method == 'POST':
            nome = request.form['nome']
            data_nascimento = request.form['data_nascimento']
            email = request.form['email']
            senha = request.form['senha']
            cpf = request.form['cpf']
            db = get_db
            error=None

            if not nome or not data_nascimento or not email or not senha or not cpf:
                error = 'Todos os campos devem ser preenchidos.'

            if error is None:
                try:
                    db.execute(
                        "insert into usuario (nome, data_nascimento, email, senha, cpf) values (?, ?)",
                    (nome, data_nascimento, email, senha, cpf),)
                    db.commit()
                except db.IntegrityError:
                    error: f"Usuario {nome} já registrado." 
    
    @app.route('/cadastro')
    def novoEquipamento():
            if request.method == 'POST':
                marca = request.form['marca']
                modelo = request.form['modelo']
                categoria = request.form['categoria']
                potencia = request.form['potencia']
                material = request.form['material']
                peso = request.form['peso']
                dimensoes = request.form['dimensoes']
                cor = request.form['cor']
                db = get_db
                error=None
    
                if not marca or not modelo or not categoria or not material or not peso or not cor:
                    error = 'Todos os campos devem ser preenchidos.'
    
                if error is None:
                    try:
                        db.execute(
                            "insert into usuario (nome, data_nascimento, email, senha, cpf) values (?, ?)",
                        (nome, data_nascimento, email, senha, cpf),)
                        db.commit()
                    except db.IntegrityError:
                        error: f"Usuario {nome} já registrado." 

    return app
