from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, TextAreaField, FileField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from paprica.models import User
from flask_wtf.file import FileAllowed
=======
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from paprica.models import User
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a

class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuario já existe! Cadastre outro nome de usuário.")
        
    def validate_email(self, check_email):
        email = User.query.filter_by(email = check_email.data).first()
        if email:
            raise ValidationError("E-mail já existe! Cadastre outro e-mail.")
    

        
    usuario = StringField(label='Username: ', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail: ', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha: ', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação de Senha: ', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')


class LoginForm(FlaskForm):
    usuario = StringField(label='Username: ', validators=[DataRequired()])
    senha = PasswordField(label='Senha: ', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')

<<<<<<< HEAD
class ProdutoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    preco = IntegerField("Preço", validators=[DataRequired()])
    cod_barra = StringField("Código de Barra", validators=[DataRequired()])
    descricao = TextAreaField("Descrição")
    estoque = IntegerField("Estoque")

    imagem = FileField(
        "Imagem",
        validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Apenas imagens!')]
    )

    submit = SubmitField("Salvar")
=======



class ProdutoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    preco = IntegerField("Preço", validators=[DataRequired()])
    cod_barra = StringField("Código de Barras", validators=[DataRequired()])
    descricao = StringField("Descrição", validators=[DataRequired()])
    estoque = IntegerField("Estoque")
    submit = SubmitField("Cadastrar")
>>>>>>> bddf3c62ea14cce2f4f6ed5bb23ac4a5cba79c4a
