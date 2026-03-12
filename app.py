from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Aqui você pode pegar os dados: nome = request.form['nome']
        return "Mensagem enviada com sucesso!"
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
