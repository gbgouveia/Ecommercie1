from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
from paprica.models import Item,User
from paprica import db
from functools import wraps
from paprica.forms import ProdutoForm

admin = Blueprint("admin", __name__, url_prefix="/admin")

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

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

@admin.route("/produtos")
@login_required
@admin_required
def produtos():
    itens = Item.query.all()
    return render_template("admin/produtos.html", itens=itens)

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

    return render_template("admin/novo_produto.html", form=form)



@admin.route("/produto/editar/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def editar_produto(id):
    produto = Item.query.get_or_404(id)

    if request.method == "POST":
        produto.nome = request.form.get("nome")
        produto.preco = request.form.get("preco")
        db.session.commit()

        flash("Produto atualizado!", "success")
        return redirect(url_for("admin.produtos"))

    return render_template("admin/editar_produto.html", produto=produto)

@admin.route("/produto/excluir/<int:id>")
@login_required
@admin_required
def excluir_produto(id):
    produto = Item.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()

    flash("Produto excluído!", "info")
    return redirect(url_for("admin.produtos"))

@admin.route("/usuarios")
@login_required
@admin_required
def usuarios():
    usuarios = User.query.all()
    return render_template("admin/usuarios.html", usuarios=usuarios)

@admin.route("/pedidos")
@login_required
@admin_required
def pedidos():
    return render_template("admin/pedidos.html")

@admin.route("/relatorios")
@login_required
@admin_required
def relatorios():
    return render_template("admin/relatorios.html")
