from unittest import result
from flask import Flask,render_template,request,session
import mysql.connector as mysql
db=mysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='db'
)
cur=db.cursor()
app = Flask( __name__ )
app.secret_key='vasu2420'

@app.route("/register")
def indexPage():
    return render_template('registerpage.html')

@app.route("/")
def login_page(): 
    return render_template('loginpage.html')
@app.route('/form')
def result_page(): 
    return render_template('result.html')
@app.route('/collect',methods=['POST'])  
def collectData():
    n = request.form['name']
    r = request.form['rollno']
    p = request.form['password']
    storeData(r,n,p)
    result = "Data collected"
    # session['rollno']=r
    # session['name']=n
    #session['password']=p
    return render_template('registerpage.html',result='Registered')
@app.route('/compare',methods=['POST'])
def logincollect():
    r1 = request.form['name']
    p1 = request.form['password']
    cur.execute('Select name,password from data')
    d=cur.fetchall()
    flag=0
    for i in d:
        if i[0]==r1 and i[1]==p1:
            flag=1
            break
    if flag:
        k = i[0]
        return render_template('result.html',result = k)
    else:
        k='Invalid'
        return render_template('loginpage.html',result=k)
def storeData(rollno,name,password):
    sql='INSERT INTO data (rollno,name,password) VALUES (%s,%s,%s)'
    val=(rollno,name,password)
    cur.execute(sql,val)
    db.commit()
if __name__=="__main__":
    app.run(debug=True)