from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/",methods=["GET","¨POST"])
def inicio():
    return render_template("inicio.html")

@app.route("/mayor")
def mayor():
    return render_template("mayor.html") 

@app.route("/SanMiguel")
def SanMiguel():
    return render_template("SanMiguel.html")

@app.route("/enlaces")
def enlaces():
    return render_template("enlaces.html")

@app.route('/resultado', methods=["GET",'POST'])
def resultado():
    respuesta=""
    if request.method =="POST" and "num1" in request.form and "num2" in request.form:
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        respuesta = num1
        if num1>num2:
                respuesta = num1
        else:
                respuesta = num2
    return render_template("resultado.html",respuesta=respuesta)

app.run(debug=True)