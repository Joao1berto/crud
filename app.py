from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = "QualquerCoisa"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/projetocrud"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Autor, Capitulos
from modulos.autores.autores import bp_autores
from modulos.capitulos.capitulos import bp_capitulos
app.register_blueprint(bp_autores, url_prefix='/autores')
app.register_blueprint(bp_capitulos, url_prefix='/capitulos')

@app.route('/')
def index():
    return render_template("ola.html")