from paprica import app
from flask import render_template, redirect, url_for, flash
from paprica.models import Item,User
from paprica.forms import CadastroForm
from paprica import db
from flask_login import login_user, logout_user, login_required, current_user
from paprica.forms import LoginForm

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens=Item.query.all()

    return render_template("produtos.html",itens=itens) 

@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(usuario=form.usuario.data).first()
        
        if usuario and usuario.check_senha(form.senha.data):
            login_user(usuario)
            flash("Login realizado com sucesso!", category="success")

            # 🔥 AQUI ESTÁ A MÁGICA
            if usuario.is_admin:
                return redirect(url_for("admin.dashboard"))

            return redirect(url_for('page_produto'))
        else:
            flash("Usuário ou senha incorretos", category="danger")

    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout realizado", category="info")
    return redirect(url_for('page_home'))

@app.route('/cadastro', methods=['GET','POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = User(
            usuario=form.usuario.data,
            email=form.email.data
        )
        usuario.set_senha(form.senha1.data)

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produto'))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao cadastrar usuário {err}', category="danger")
    return render_template("cadastro.html", form=form)

@app.route("/perfil")
@login_required
def page_perfil():
    itens_comprados = Item.query.filter_by(dono=current_user.id).all()
    return render_template("perfil.html", itens=itens_comprados)

