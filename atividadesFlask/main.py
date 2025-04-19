from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('base.html')

@app.route('/imc', methods=['GET', 'POST'])
def imc():
    if request.method == 'POST':
        peso = request.form['pesoForm']
        altura = request.form['alturaForm']
        try:
            floatPeso = float(peso)
            floatAltura = float(altura)
            media = floatPeso / (floatAltura ** 2)
            imc = f"{media:.2f}"
        except (ValueError, ZeroDivisionError):
            imc = "Valor inválido"
        return render_template('imc.html', imc=imc)

    return render_template('imc.html')

@app.route('/pares-impares', methods=['GET','POST'])
def pares_impares():
  todos = []
  pares = []
  impares = []
  if request.method == 'POST':
    numeroForm = request.form['numeroForm']
    if numeroForm.isdigit():
      for numero in numeroForm:
        n = int(numero)
        tipo = 'Par' if n % 2 == 0 else 'Impar'
        todos.append((n,tipo))
        if tipo == 'Par':
          pares.append(n)
        else:
          impares.append(n)
    else:
      todos = [('Entrada Invalida', '')]
  return render_template('pares-impares.html', todos = todos, pares = pares, impares = impares)
      
if __name__ == '__main__':
  app.run(debug=True)