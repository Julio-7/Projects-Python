from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/restaurantes', methods=['GET', 'POST'])
def listar_restaurantes():
    url_api = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    dados_filtrados = {}

    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status()
        dados = resposta.json()

        termo_busca = request.form.get('nome') if request.method == 'POST' else ''

        for item in dados:
            nome = item['Company']
            if termo_busca.lower() in nome.lower():
                if nome not in dados_filtrados:
                    dados_filtrados[nome] = []
                dados_filtrados[nome].append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })

        return render_template('restaurantes.html', restaurantes=dados_filtrados, busca=termo_busca)

    except requests.RequestException as erro:
        return f"Erro ao acessar a API: {erro}", 500

if __name__ == '__main__':
    app.run(debug=True)
