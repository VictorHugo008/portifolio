from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página de projetos
@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

# Página de contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Executa o servidor
if __name__ == '__main__':
    app.run(debug=True)
