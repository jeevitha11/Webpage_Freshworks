from flask import Flask,render_template,request
import mysql.connector
import os

app=Flask(__name__,static_url_path='/static')
@app.route('/')
def home():
    return render_template('reg.html')


@app.route('/login',methods=['POST','GET'])
def login():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="storagebase"
    )
    mycursor=db.cursor()
    if request.method=='POST':
        result=request.form
        username=result['username']
        password=result['password']
        mycursor.execute("select *from `basetable` where username=%s and password=%s",(username,password,))
        r=mycursor.fetchone()

        if r:
           #return "Login successful"
           return render_template("display.html")
        else:
           return "Invalid username/password!"
        db.commit()
        mycursor.close()



@app.route('/reg',methods=['POST','GET'])
def reg():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="storagebase"
    )
    mycursor=db.cursor()
    if request.method=='POST':
        result=request.form
        firstname=result['firstname']
        lastname=result['lastname']
        username=result['username']
        email=result['email']
        password=result['password']
        #print(mycursor.execute("select *from `basetable`"))
        mycursor.execute("insert into `basetable` (First_name,Last_name,username,Email,password) values (%s,%s,%s,%s,%s)",(firstname,lastname,username,email,password))
        db.commit()
        mycursor.close()
        return render_template("displaySUCCESSREG.html")


@app.route('/delete',methods=['POST','GET'])
def delete():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="storagebase"
    )
    mycursor=db.cursor()
    if request.method=='POST':
        result=request.form
        username=result['username']
        password=result['password']
        mycursor.execute("select *from `basetable` where username=%s and password=%s",(username,password,))
        r=mycursor.fetchone()
        if r:
           mycursor.execute("delete from `basetable` where username=%s and password=%s",(username,password,))
           return "DELETED!"
        else:
           return "Invalid username/password!"
        db.commit()
        mycursor.close()


if __name__=="__main__":
    app.secret_key=os.urandom(12)
    app.run(threaded=True,debug=True)  

