from flask import Flask, render_template,request,redirect,flash,url_for
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Iselva1290'
app.config['MYSQL_DB']='e'
app.secret_key = "mysecretkey"
mysql=MySQL(app)


## ------------------- funciones para el fixture -----------------------------


def  ordenarFecha( a) :

    aux = [None] * (len(a))
    aux[0] = a[0]
    aux[1] = a[len(a) - 1]
    i = 2
    while (i < len(a)) :
        aux[i] = a[i - 1]
        i += 1
    return aux

def mostrarFecha( a) :

    datos=[]
    numero = int(len(a) / 2)
    con = 0
    i = 0
    while (i < len(a)) :
        if (con != numero) :
            ariel=str(a[i] + " vs " + a[(len(a) - con) - 1])
            con += 1
            datos.append(ariel)
        i += 1
    return datos

#pagina de inicio de sesion en el sistema web
@app.route('/')
def Index():
    return  render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/ingresar',methods=['POST'])
def ingresar():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE username = %s and password= %s', (username,password))
        data = cur.fetchall()
        cur.close()
        if data:
            return render_template('home.html')
        else:
            flash('El usuario no existe')
            return redirect(url_for('login'))


## ----------------- seccion para adicionar equipo ----------------------
@app.route('/equipos')
def equipos():
    return render_template('equipo.html')

@app.route('/fixture')
def fixture():
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre FROM equipos')
    equipos_disponibles = cur.fetchall()
    cur.close()
    data=[]
    a=[]
    for l in equipos_disponibles:
        a.append(l[0])
    if len(a)%2 !=0:
        a.append(" Equipo descansa ")
    if (len(a) % 2 == 0) :

        i = 0
        while (i < len(a) - 1) :

            leira=str("fecha " + str((i + 1)))
            
            if (i == 0) :

                data.append(mostrarFecha(a))
            else :

                aux = ordenarFecha(a)
                data.append(mostrarFecha(aux))
                a = aux
            i += 1

    return render_template('fixture.html',datos=data)

@app.route('/adicionar_usuario',methods=['POST'])
def adicionar_usuario():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        paterno=request.form['paterno']
        materno=request.form['materno']
        nombre=request.form['nombre']
        role=request.form['role']
        fecha_creacion=request.form['fecha_creacion']
        cur = mysql.connection.cursor()
        cur.execute(
                "INSERT INTO usuarios (username, password, paterno,materno,nombre,role,fecha_creacion) VALUES (%s,%s,%s,%s,%s,%s,%s)", (username, password, paterno,materno,nombre,role,fecha_creacion))
        mysql.connection.commit()
            
        #return redirect(url_for('Index.html'))
        return 'registrado'

@app.route('/editar_usuario')
def editar_usuario():
    return 'pantalla para editar usuario'

@app.route('/eliminar_usuario')
def eliminar_usuario():
    return 'eliminar usuario'

if __name__== '__main__':
    app.run(port=3000,debug=True)