from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html', nome ='Alba', email= 'alba.lopes@gmail.com')

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

@app.route('/usuario', defaults={"nome":"usuário comum"})
@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome = nome)

@app.route('/semestre/<int:x>')
def semestre(x):
    return render_template('semestre.html', x = x)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    modalidade = request.form.getlist('modalidade')
    return render_template('recebedados.html', modalidade=modalidade)

    # formacao = request.form['formacao']
    # return render_template('recebedados.html', formacao=formacao)

    # estados = request.form['estados']
    # return render_template('recebedados.html', estados=estados)

    # nome = request.form['nome']
    # sobrenome = request.form['sobrenome']
    # email = request.form['email']
    # return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email)


if __name__ == '__main__':
    app.run()
    