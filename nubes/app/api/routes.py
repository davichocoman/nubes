from flask import render_template, redirect, url_for, flash
from app.api.models import Servidor, Guia, Clinica  # Importe do módulo models
from app.api.forms import LoginServidorForm, EmitirGuiaForm, LoginCredenciadaForm, VerificarGuiaForm  # Importe do módulo forms
from app import db, create_app  # Importe do módulo principal

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/servidor', methods=['GET', 'POST'])
def servidor():
    form = LoginServidorForm()
    if form.validate_on_submit():
        servidor = Servidor.query.filter_by(matricula=form.matricula.data).first()
        if servidor:
            return render_template('servidor.html', form=EmitirGuiaForm(), dados_servidor=servidor)
        else:
            flash('Matrícula não encontrada. Entre em contato com o NUBES.', 'danger')
    return render_template('servidor.html', form=form)

@app.route('/emitir_guia', methods=['POST'])
def emitir_guia():
    form = EmitirGuiaForm()
    if form.validate_on_submit():
        # Lógica para emitir a guia
        flash('Guia emitida com sucesso!', 'success')
    return redirect(url_for('servidor'))

@app.route('/credenciada', methods=['GET', 'POST'])
def credenciada():
    form = LoginCredenciadaForm()
    if form.validate_on_submit():
        clinica = Clinica.query.filter_by(cnpj=form.cnpj.data, senha=form.senha.data).first()
        if clinica:
            return render_template('credenciada.html', form=VerificarGuiaForm(), autenticado=True)
        else:
            flash('CNPJ ou senha incorretos.', 'danger')
    return render_template('credenciada.html', form=form)

@app.route('/verificar_guia', methods=['POST'])
def verificar_guia():
    form = VerificarGuiaForm()
    if form.validate_on_submit():
        guia = Guia.query.filter_by(codigo=form.codigo_guia.data).first()
        if guia:
            return render_template('credenciada.html', form=form, autenticado=True, guia_valida=guia)
        else:
            flash('Guia não encontrada.', 'danger')
    return redirect(url_for('credenciada'))

@app.route('/admin')
def admin():
    return render_template('admin.html')