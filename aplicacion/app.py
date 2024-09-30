import config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/')
def inicio():
	return render_template("inicio.html")


@app.route('/Clientes')
def clientes():
	return render_template("clientes.html")

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html", error="Página no encontrada..."), 404



if __name__ == '__main__':
    app.run(host="127.0.0.1")
