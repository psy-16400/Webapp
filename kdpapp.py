from flask import *
from KDPDBM import *

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

@app.route("/addVadak", methods=["POST"])
def Add_vadak():
    Id=request.form["ID"]
    fname=request.form["fname"]
    gender=request.form["gender"]
    age=request.form["age"]
    Eid=request.form["Eid"]
    numb=request.form["numb"]
    enumb=request.form["enumb"]
    adrs=request.form["adrs"]
    loc=request.form["loc"]
    expn=request.form["expn"]
    pref=request.form["pref"]
    t=(Id, fname, gender, age, Eid, numb, enumb, adrs, loc, expn, pref)
    addVadak(t)
    return redirect("/Ad_complete")

@app.route("/Vadaklist")
def vadaklist():
    data=selectAllVadak()
    return render_template("All_Vadak.html",vlist=data)

@app.route("/deleteVadak", methods=["GET"])
def delete_vadak():
    ids=request.args.get("id")
    deleteVadak(ids)
    return redirect("Vadaklist")

@app.route("/editVadak/<int:myid>")
def edit_vadak(myid):
    ids=myid
    data=selectVadakById(ids)
    return render_template("Update.html",row=data)

@app.route("/updateVadak", methods=["POST"])
def update_vadak():
    Id=request.form["ID"]
    fname=request.form["fname"]
    gender=request.form["gender"]
    age=request.form["age"]
    Eid=request.form["Eid"]
    numb=request.form["numb"]
    enumb=request.form["enumb"]
    adrs=request.form["adrs"]
    loc=request.form["loc"]
    expn=request.form["expn"]
    pref=request.form["pref"]
    t=(fname, gender, age, Eid, numb, enumb, adrs, loc, expn, pref, Id)
    updateVadak(t)
    return redirect("Vadaklist")

     
if (__name__=="__main__"):
    app.run(debug=True)
