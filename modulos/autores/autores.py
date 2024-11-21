from flask import Blueprint, render_template, request, flash, redirect
from database import db
from models import Autor

bp_autores = Blueprint('autores', __name__, template_folder="templates")

@bp_autores.route('/')
def index():
    a = Autor.query.all()
    return render_template('autores.html', autores = a)

@bp_autores.route('/add')
def add():
    return render_template('autores_add.html')

@bp_autores.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    instituicao = request.form.get('instituicao')
    if nome and instituicao:
        bd_autor = Autor(nome, instituicao)
        db.session.add(bd_autor)
        db.session.commit()
        flash('Autor salvo com sucesso!!!')
        return redirect('/autores')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/autores/add')
    
@bp_autores.route("/remove/<int:id>")
def remove(id):
    a = Autor.query.get(id)
    try:
        db.session.delete(a)
        db.session.commit()
        flash("Autor removido!!!")
    except:
        flash("Autor Inválido!!!")
    return redirect("/autores")

@bp_autores.route("/edit/<int:id>")
def edit(id):
    a = Autor.query.get(id)
    return render_template("autores_edit.html", dados=a)

@bp_autores.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    instituicao = request.form.get("instituicao")
    id_autor = request.form.get("id_autor")
    if nome and instituicao and id_autor:
        a = Autor.query.get(id_autor)
        a.nome = nome
        a.instituicao = instituicao
        db.session.commit()
        flash("Autor editado com sucesso!!!")
    else:
        flash("Preencha todos os campos!!!")
    return redirect("/autores")