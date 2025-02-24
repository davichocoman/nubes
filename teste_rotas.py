from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__,
            template_folder='nubes/app/templates',  # Pasta para templates
            static_folder='nubes/app/static',
            )       # Pasta para arquivos estáticos (CSS, JS, imagens)

@app.route('/')
def index():
    return render_template("layout.html")

# Rota para o login
@app.route('/login')
def login():
    if request.method == 'POST':
        # Processar os dados do formulário
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        # Aqui você pode adicionar a lógica de autenticação
        print(f"Usuário: {usuario}, Senha: {senha}")
        
        # Redirecionar para uma página de sucesso (ou outra rota)
        return redirect(url_for('login'))  # Por enquanto, redireciona de volta para o login

    # Se for uma requisição GET, renderize a página de login
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
