from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)

class Usuario(db.Model):
  __tablename__ = 'usuarios'
  
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(40), nullable=False, unique=True) 

  def __repr__(self):
    return f"<{self.nome}>"
  
@app.route('/')
def index():
  return 'ola,mundo'

if __name__ == '__main__':
  with app.app_context():
    # ADICIONANDO NO BANCO
    # user = Usuario(nome = 'Pixelar')
    # db.session.add(user)
    # db.session.commit()
    # db.create_all()
    
    # LISTANDO TODOS OS NOMES DO BANCO
    # usuario = db.session.query(Usuario).all()
    # for us in usuario:
    #   print(f"Usuario: {us.nome}")
    
    user = db.session.query(Usuario).filter_by(id = 2).first()
    # user.nome = "Rodrigo" # editando
    db.session.delete(user) # deletando
    db.session.commit() # nao se esqueça do commit
  app.run(debug=True)
