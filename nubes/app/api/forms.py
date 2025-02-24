from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Length

class LoginServidorForm(FlaskForm):
    matricula = StringField('Matrícula', validators=[DataRequired()])
    submit = SubmitField('Verificar Dados')

class EmitirGuiaForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    submit = SubmitField('Emitir Guia')

class LoginCredenciadaForm(FlaskForm):
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class VerificarGuiaForm(FlaskForm):
    codigo_guia = StringField('Código da Guia', validators=[DataRequired()])
    submit = SubmitField('Verificar')