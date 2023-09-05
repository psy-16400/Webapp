from flask import *
from cdbDBM import *

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("Logpage.html")

@app.route("/login1", methods=["POST"])
def log_in():
    username=request.form["uname"]
    password=request.form["passw"]
    t=(username,password)
    t1=Log_check(t)
    print(t,t1)
    if t in t1:
        return redirect("home")
    else:
        return render_template("Logpage.html", status='Invalid Credentials')        

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/Admissions")
def admit():
    return render_template("Admissions.html")

@app.route("/Ad_complete")
def admissioncomplete():
    return render_template("Ad_complete.html")

@app.route("/addPerson", methods=["POST"])
def Add_Person():
    Id=request.form["ID"]
    fname=request.form["fname"]
    gender=request.form["gender"]
    age=request.form["age"]
    t=(Id, fname, gender, age)
    addPerson(t)
    return redirect("/Ad_complete")

@app.route("/Personlist")
def Personlist():
    data=selectAllPerson()
    return render_template("All_Person.html",vlist=data)

@app.route("/deletePerson", methods=["GET"])
def delete_Person():
    ids=request.args.get("id")
    deletePerson(ids)
    return redirect("Personlist")

@app.route("/editPerson/<int:myid>")
def edit_Person(myid):
    ids=myid
    data=selectPersonById(ids)
    return render_template("Update.html",row=data)

@app.route("/updatePerson", methods=["POST"])
def update_Person():
    Id=request.form["ID"]
    fname=request.form["fname"]
    gender=request.form["gender"]
    age=request.form["age"]
    t=(Id, fname, gender, age)
    updatePerson(t)
    return redirect("Personlist")

     
if (__name__=="__main__"):
    app.run(debug=True)
