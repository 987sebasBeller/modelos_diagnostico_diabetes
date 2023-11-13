
from pymongo.mongo_client import MongoClient
from flask import Flask , render_template ,request ,redirect ,url_for,session,flash
import pickle
import pandas as pd
with open("modelo.pkl", "rb") as file:
    modelo = pickle.load(file)


client = MongoClient("mongodb://localhost:27017/")
mydb = client["ProyectoDiabetes"]
print(mydb)
db_usuarios=mydb.usuarios
app = Flask(__name__)
app.secret_key = "_C@A&T*o{"
# @app.route('/signUp',methods=['POST'])
# def signUp():
#     email=request.form.get("email")
#     password=request.form.get("password")
#     try:
#         client.admin.command('ping')
#         db['usuarios'].insert_one({'email':email,'password':password})
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#         print(db['usuarios'].find())
#     except Exception as e:
#         print(e)
#     return render_template('index.html')

def limpiarMemoria():
    if 'pacientes' in session:
        session.pop('pacientes')
    if 'username' in session:
        session.pop('username')
    if 'password' in session:
        session.pop('password')
@app.route('/')
def home():
    limpiarMemoria()
    return render_template('login.html')
def init_dic_pacientes():
        datos_prediccion =   {
            'NOMBRE':[],
        'AGE': [],
        'HbA1c': [],
        'Chol': [],
        'TG': [],
        'VLDL': [],
        'BMI': [],
        'Gender': [],
        'CLASS':[]
            }
        return datos_prediccion

@app.route('/get_tabla',methods=["POST"])
def get_tabla():
    session["pacientes"]=init_dic_pacientes().copy()
    user_name=request.values.get("user_name")
    password=request.values.get("password")
    cliente=db_usuarios.find_one({'username':user_name,'password':password})
    if cliente==None:
        flash('No se encontro el registro, ingrese nuevamente sus datos!!')
        return redirect(url_for('home'))
    session["username"]=user_name
    session["password"]=password
    return render_template('tabla.html')
@app.route('/predecir')
def predecir():
    vec=['AGE',
        'HbA1c',
        'Chol',
        'TG',
        'VLDL',
        'BMI',
        'Gender',
        'CLASS',
        'NOMBRE'
       ]
    data=pd.DataFrame(session["pacientes"],columns=vec)
    data["CLASS"]=modelo.predict(data.iloc[:,:-1])
    print(data)

    return render_template('reporte.html',resultados=data)
@app.route('/aniadirPaciente',methods=["POST"])
def aniadirPaciente():
    dictionary=session["pacientes"].copy()
    for key,value in dictionary.items():
        data=request.values.get(key)
        if not data.isalpha():
            data=float(data)
        value.append(data)
    session["pacientes"]=dictionary
    print(session["pacientes"])

    return render_template('tabla.html')
@app.route('/salir')
def salir():
    print("holA")
    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True) 
    del session