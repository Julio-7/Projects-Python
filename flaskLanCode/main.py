from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  frutas = ['banana', 'abacate', 'morango']
  return render_template('index.html', frutas = frutas)

@app.route('/formulario', methods = ['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nomeForm']
        email = request.form['emailForm']
        print(f"nome: {nome} email: {email}")
        return render_template('formulario.html', nome = nome, email = email)
    return render_template('formulario.html')
if __name__ == '__main__':
  app.run(debug=True)