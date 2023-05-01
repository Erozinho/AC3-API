from flask import Blueprint, render_template, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="dbAlunos",
)

mycursor = db.cursor()

insert = "INSERT INTO Alunos (nome, curso, idade) VALUES (%s,%s,%s)"
select = "SELECT * from Alunos"

registrar = Blueprint('registrar', __name__, template_folder="template")

@registrar.route('/registrar', methods=['GET'])
def pegar_registro():
    return render_template("registrar.html")

@registrar.route('/registrar', methods=['POST'])
def salvar_registro():
    n = request.form.get('nome')
    i = request.form.get('idade')
    c = request.form.get('curso')
    i = int(i)

    val = (n,c,i)

    mycursor.execute(insert, val)
    db.commit()
    mycursor.execute(select)
    tabela = mycursor.fetchall()
    
    for tabela in tabela:
        print("Nome:", tabela[0])
        print("Curso:", tabela[1])
        print("Idade:", tabela[2], "\n")

    return "<h1>Dados criado com sucesso!</h1>"
