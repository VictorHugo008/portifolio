@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        try:
            # Pegando os dados de forma segura
            nome = request.form.get('nome', 'N/A')
            email = request.form.get('email', 'N/A')
            mensagem = request.form.get('mensagem', 'N/A')
            
            print(f">>> MENSAGEM RECEBIDA: {nome} - {email}")
            
            # Retorna o template com a variável 'sucesso'
            return render_template('contato.html', sucesso=True)
        except Exception as e:
            # Se der erro, ele imprime o motivo real no seu terminal/CMD
            print(f"ERRO NO SERVIDOR: {e}")
            return f"Erro interno: {e}", 500
            
    return render_template('contato.html')
