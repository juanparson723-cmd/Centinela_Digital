from flask import Flask #importa flask
from flask import render_template # muestra los HTML
from flask import request #obtiene datos enviados desde formularios
from flask import redirect #redirigir al usuario a otra rut
from flask import url_for #genera rutas 
from flask import session #sesión del usuario
from flask import flash #permite mostrar mensajes temporales al usuario

from config import Config # importa la configuración de la db
from database import get_connection # importa la función para conectarse a la base de datos

import bcrypt # se utiliza para cifrar contraseñas

app = Flask(__name__) # crea la aplicación Flask
app.config.from_object(Config) #carga lo que tenga config


# =registro

@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html") #se cierra la definicion de index


#ejecucion de la app 
if __name__ == "__main__":
    app.run(debug=True)