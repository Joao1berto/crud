from database import db
class Autor(db.Model):
    __tablename__ = 'autores'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    instituicao = db.Column(db.String(100))
    
    def __init__(self, nome, instituicao):
        self.nome = nome
        self.instituicao = instituicao

    def __repr__(self):
        return "<Autor {}>".format(self.nome)
    
class Capitulos(db.Model):
    __tablename__ = 'capitulos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    pagina_inicial= db.Column(db.Integer)
    id_autor = db.Column(db.Integer, db.ForeignKey('autores.id_autor'))

    autor = db.relationship('Autor', foreign_keys = id_autor)
    
    def __init__(self, titulo, pagina_inicial, id_autor):
        self.titulo = titulo
        self.pagina_inicial = pagina_inicial
        self.id_autor = id_autor

    def __repr__(self):
        return "<Capitulo {}>".format(self.titulo)