from app.api import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'credenciada'

class Servidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

class Guia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servidor_id = db.Column(db.Integer, db.ForeignKey('servidor.id'), nullable=False)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    data_emissao = db.Column(db.DateTime, nullable=False)
    exames = db.Column(db.JSON, nullable=False)  # Lista de exames

class Clinica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(60), nullable=False)