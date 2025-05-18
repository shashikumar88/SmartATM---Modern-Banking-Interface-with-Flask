from flask import Flask,render_template,request

app = Flask(__name__)

accounts = {
    "1001" : ["User 1","user1@gmaiul.com","1234",10000],
    "1002" : ["User 2","user2@gmail.com","5678",12000],
    "1003" : ["User 3","user3@gmail.com",None,5000],
    "1004" : ["User 4","user4@gmail.com",None,0]
}
@app.route("/")
def landing():
    return render_template("home.html")

@app.route("/withdraw1")
def withdraw1():
    return render_template("withdraw1.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/withdraw2",methods=["POST","GET"])
def withdraw2():
    accno = request.form["account_number"]
    pin = request.form["pin"]
    print(accno)
    print(pin)
  
    if accno not in accounts:
        return render_template("withdraw1.html",msg="noaccount")
    elif accounts[accno][-2] != pin:
        return render_template("withdraw1.html",msg="wrongpin")
    else:
        return render_template("withdraw2.html",user_name=accounts[accno][0],accno=accno)
@app.route("/withdraw3",methods=["POST","GET"])
def withdraw3():
    accno = request.form["accno"]
    amount = request.form["amount"]
    if int(amount) <= accounts[accno][-1]:
        accounts[accno][-1] = accounts[accno][-1] -  int(amount)
        return render_template("withdraw2.html",msg="balance",accno=accno)

    else:
        return render_template("withdraw2.html",msg="nobalance",accno=accno)
@app.route("/deposit1")
def deposit1():
    return render_template("deposit1.html")

@app.route("/deposit2",methods=["POST","GET"])
def deposit2():
    accno = request.form["accno"]
    amount = int(request.form["amount"])
    if accno not in accounts:
        return render_template("deposit1.html",msg="noaccount")
    else:
        accounts[accno][-1] += amount 
        return render_template("deposit1.html",msg = "account" )
@app.route("/ministatement1")
def ministatement1():
    return render_template("ministatement1.html")
@app.route("/ministatement2",methods=["POST","GET"])
def ministatement2():
    accno = request.form["accno"]
    pin = request.form["pin"]
    if accno not in accounts:
        return render_template("ministatement1.html",msg="noaccount")
    elif accounts[accno][-2] != pin:
        return render_template("ministatement1.html",msg="wrongpin")
    else:
        name = accounts[accno][0]
        email = accounts[accno][1]
        balance = accounts[accno][-1]
        return render_template("ministatement2.html",accno=accno,name=name,email=email,balance=balance)
@app.route("/pingeneration1")
def pingeneration1():
    return render_template("pingeneration1.html")
@app.route("/pingeneration2",methods=["POST","GET"])
def pingeneration2():
    accno = request.form["accno"]
    if accno not in accounts:
        return render_template("pingeneration1.html",msg="noaccount")
    elif accounts[accno][-2] != None:
        return render_template("pingeneration1.html",msg="account")
    else:
        return render_template("pingeneration2.html",accno=accno)
@app.route("/pingeneration3",methods=["POST","GET"])
def pingeneration3():
    accno = request.form["accno"]
    pin = request.form["pin"]
    cpin = request.form["cpin"]
    if pin != cpin:
        return render_template("pingeneration2.html",accno=accno,msg="wrongpin")
    else:
        accounts[accno][-2] = pin
        return render_template("pingeneration2.html",msg="ok")
app.run(port=5011)

