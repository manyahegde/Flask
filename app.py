from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def rootpage():
    name=''
    age=''
    if request.method=='POST' and 'username' in request.form and 'age' in request.form:
        name=request.form.get('username')
        age=request.form.get('age')
    return render_template("index.html", name=name, age=age)
app.run()