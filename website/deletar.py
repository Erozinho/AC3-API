from flask import Blueprint, render_template, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@",
    database="dbAlunos"
)

mycursor = db.cursor()
dele = "DELETE FROM Alunos WHERE RA=%s"

apagar = Blueprint('apagar', __name__, template_folder="template")

@apagar.route('/apagar', methods=['GET'])
def pegar_RA():
    return render_template("delete.html")

@apagar.route('/apagar', methods=['POST','DELETE'])
def apagar_registros():
    RA = request.form.get('RA')
    R = [int(RA)]
    mycursor.execute(dele, R)
    db.commit()
    return "<h1>Dado apagado com sucesso.</h1>"

