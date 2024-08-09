from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Lista pré-definida de formas de pagamento
formas_pagamento = ['Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix']

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            # Coletando os dados enviados pelo formulário
            valor = request.form.get('valor', '')
            forma_pagamento = request.form.get('forma_pagamento', '')
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            if not valor or not forma_pagamento:
                print("Valor ou forma de pagamento não fornecidos!")
                return redirect(url_for('index'))

            # Caminho do arquivo onde os dados serão armazenados
            caminho_arquivo = os.path.join(os.getcwd(), 'vendas.txt')

            # Salva os dados em um arquivo de texto
            with open(caminho_arquivo, 'a') as f:
                f.write(f'{data_hora}, {valor}, {forma_pagamento}\n')
            
            print(f"Dados salvos: {data_hora}, {valor}, {forma_pagamento}")
            return redirect(url_for('index'))

        return render_template('index.html', formas_pagamento=formas_pagamento)
    except Exception as e:
        print(f"Erro: {e}")
        return "Ocorreu um erro durante a execução. Verifique o console para mais detalhes."

if __name__ == '__main__':
    app.run(debug=True)
