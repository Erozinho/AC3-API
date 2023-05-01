from flask import jsonify, Blueprint
import mysql.connector

registros = Blueprint('registros', __name__, template_folder="template")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="dbAlunos",
)

mycursor = db.cursor()

select = "SELECT * from Alunos"

@registros.route('/registros', methods=['GET'])
def pegar_registros():
    mycursor.execute(select)
    tabela = mycursor.fetchall()
    return jsonify(tabela)
