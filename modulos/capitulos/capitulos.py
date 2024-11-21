from flask import Blueprint, render_template, request, flash, redirect
from database import db
from models import Capitulos, Autor

bp_capitulos = Blueprint('capitulos', __name__, template_folder="templates")

@bp_capitulos.route('/')
def index():
    c = Capitulos.query.all()
    return render_template('capitulo.html', capitulo = c)

@bp_capitulos.route('/add')
def add():
    a = Autor.query.all()
    return render_template('capitulo_add.html', autores=a)

@bp_capitulos.route('/save', methods=['POST'])
def save():
    titulo = request.form.get('titulo')
    pagina_inicial = request.form.get('pagina_inicial')
    id_autor = request.form.get('id_autor')
    if titulo and pagina_inicial and id_autor:
        bd_capitulo = Capitulos(titulo, pagina_inicial, id_autor)
        db.session.add(bd_capitulo)
        db.session.commit()
        flash('Capitulo salvo com sucesso!!!')
        return redirect('/capitulos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/capitulos/add')

@bp_capitulos.route("/remove/<int:id>")
def remove(id):
    c = Capitulos.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("Capitulo removido!!!")
    except:
        flash("Capitulo Inválido!!!")
    return redirect("/capitulos")

@bp_capitulos.route("/edit/<int:id>")
def edit(id):
    c = Capitulos.query.get(id)
    a = Autor.query.all()
    return render_template("capitulo_edit.html", dados=c, autores=a)

@bp_capitulos.route("/edit-save", methods=['POST'])
def edit_save():
    titulo = request.form.get("titulo")
    pagina_inicial = request.form.get("pagina_inicial")
    id_autor = request.form.get("id_autor")
    id = request.form.get("id")
    if titulo and pagina_inicial and id_autor and id:
        c = Capitulos.query.get(id)
        c.titulo = titulo
        c.pagina_inicial = pagina_inicial
        c.id_autor = id_autor
        db.session.commit()
        flash("Dados atualizados!!!")
    else:
        flash("Preencha todos os campos!!!")
    return redirect("/capitulos")  