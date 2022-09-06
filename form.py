import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'usbw'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = ' 192.168.0.8'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('formulario.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    if nome and email and senha:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into cadastro  (name,email,senha) VALUES (%s, %s, %s)', (nome, email, senha))
        conn.commit()
    return render_template('formulario.html')


@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.executar('select name, email,  from cadastro')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
