from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
<<<<<<< HEAD
from paprica.models import Item, User
from paprica import db
from functools import wraps
from paprica.forms import ProdutoForm
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
import os

admin = Blueprint("admin", __name__, url_prefix="/admin")


# 🔐 Decorador para exigir admin
=======
from paprica.models import Item,User
from paprica import db
from functools import wraps
from paprica.forms import ProdutoForm

admin = Blueprint("admin", __name__, url_prefix="/admin")

>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

<<<<<<< HEAD

# 📊 Dashboard
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/")
@login_required
@admin_required
def dashboard():
    total_produtos = Item.query.count()
    total_usuarios = User.query.count()

    return render_template(
        "admin/dashboard.html",
        total_produtos=total_produtos,
        total_usuarios=total_usuarios
    )

<<<<<<< HEAD

# 📦 Listar Produtos
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/produtos")
@login_required
@admin_required
def produtos():
    itens = Item.query.all()
    return render_template("admin/produtos.html", itens=itens)

<<<<<<< HEAD

# ➕ Criar Produto
@admin.route("/criar-produto", methods=["GET", "POST"])
@login_required
@admin_required
def criar_produto():
    form = ProdutoForm()

    if form.validate_on_submit():

        # 🔎 Verifica código duplicado
        produto_existente = Item.query.filter_by(
            cod_barra=form.cod_barra.data
        ).first()

        if produto_existente:
            flash("Já existe produto com esse código!", "danger")
            return redirect(url_for("admin.criar_produto"))
        
        produto_existente = Item.query.filter_by(nome=form.nome.data).first()

        if produto_existente:
            flash("Já existe um produto com esse nome.", "danger")
            return redirect(url_for("admin.criar_produto"))

        nome_arquivo = None  # <- importante

        # ✅ AQUI FICA O CÓDIGO DO UPLOAD
        if form.imagem.data:
            arquivo = form.imagem.data
            nome_arquivo = secure_filename(arquivo.filename)

            caminho = os.path.join(
                "paprica/static/produtos",
                nome_arquivo
            )

            arquivo.save(caminho)

        # ✅ Depois cria o produto
        novo_produto = Item(
            nome=form.nome.data,
            preco=form.preco.data,
            cod_barra=form.cod_barra.data,
            descricao=form.descricao.data,
            estoque=form.estoque.data,
            imagem=nome_arquivo,  # <- salva só o nome
            ativo=True,
            dono=current_user.id
        )

        db.session.add(novo_produto)
        db.session.commit()

        flash("Produto criado com sucesso!", "success")
        return redirect(url_for("admin.produtos"))
=======
@admin.route('/produto/novo', methods=['GET', 'POST'])
@login_required
@admin_required
def novo_produto():
    form = ProdutoForm()

    if form.validate_on_submit():
        produto = Item(
            nome=form.nome.data,
            preco=form.preco.data,
            cod_barra=form.cod_barra.data,  # ← ESSA LINHA É OBRIGATÓRIA
            descricao=form.descricao.data,
            estoque=form.estoque.data,
            dono=current_user.id
        )

        db.session.add(produto)
        db.session.commit()

        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for('admin.produtos'))
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a

    return render_template("admin/novo_produto.html", form=form)


<<<<<<< HEAD
# ✏️ Editar Produto
=======

>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/produto/editar/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def editar_produto(id):
    produto = Item.query.get_or_404(id)

    if request.method == "POST":
        produto.nome = request.form.get("nome")
        produto.preco = request.form.get("preco")
<<<<<<< HEAD
        produto.estoque = request.form.get("estoque")
        produto.descricao = request.form.get("descricao")

        db.session.commit()
=======
        db.session.commit()

>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
        flash("Produto atualizado!", "success")
        return redirect(url_for("admin.produtos"))

    return render_template("admin/editar_produto.html", produto=produto)

<<<<<<< HEAD

# 🗑️ Excluir Produto
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/produto/excluir/<int:id>")
@login_required
@admin_required
def excluir_produto(id):
    produto = Item.query.get_or_404(id)
<<<<<<< HEAD

=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
    db.session.delete(produto)
    db.session.commit()

    flash("Produto excluído!", "info")
    return redirect(url_for("admin.produtos"))

<<<<<<< HEAD

# 👤 Listar Usuários
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/usuarios")
@login_required
@admin_required
def usuarios():
    usuarios = User.query.all()
    return render_template("admin/usuarios.html", usuarios=usuarios)

<<<<<<< HEAD

# 🛒 Pedidos
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/pedidos")
@login_required
@admin_required
def pedidos():
    return render_template("admin/pedidos.html")

<<<<<<< HEAD

# 📈 Relatórios
=======
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
@admin.route("/relatorios")
@login_required
@admin_required
def relatorios():
<<<<<<< HEAD
    return render_template("admin/relatorios.html")
=======
    return render_template("admin/relatorios.html")
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
