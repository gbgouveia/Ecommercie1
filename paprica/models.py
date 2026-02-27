from paprica import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=345), nullable=False, unique=True)
    senha = db.Column(db.String(length=255), nullable=False)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref="dono_user", lazy=True)

    is_admin = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(20), default="cliente")
    data_criacao = db.Column(db.DateTime, default=db.func.now())

    def set_senha(self, senha_texto):
        self.senha = generate_password_hash(senha_texto)

    def check_senha(self, senha_digitada):
        return check_password_hash(self.senha, senha_digitada)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False)
    estoque = db.Column(db.Integer, default=0)
    imagem = db.Column(db.String(200))
    ativo = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=db.func.now())
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item {self.nome}"

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total = db.Column(db.Integer)
    status = db.Column(db.String(50), default="Pendente")
    data = db.Column(db.DateTime, default=db.func.now())

    usuario = db.relationship('User', backref='pedidos')

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    quantidade = db.Column(db.Integer)
    preco_unitario = db.Column(db.Integer)

    pedido = db.relationship('Pedido', backref='itens')
    produto = db.relationship('Item')

<<<<<<< HEAD
class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)

    item = db.relationship('Item')
    usuario = db.relationship('User')
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
