from flask import Flask,render_template
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



app.run(debug=True)