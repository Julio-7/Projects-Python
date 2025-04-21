from db import db

class Contato(db.Model):
  __tablename__ = 'contatos'
  
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(40), nullable=False)
  telefone = db.Column(db.Integer, nullable=False)