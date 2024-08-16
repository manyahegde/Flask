from flask import Flask, request

app=Flask(__name__)

@app.route('/') 
def welcome():
    return 'This is my first Flask app'

@app.route('/potato') 
def potato():
    return 'This is potato page'

@app.route('/yay') 
def yay():
    return 'This yay page'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method=='POST':
        return "you have used a POST request!"
    else:
        return "I guess a GET request?"
app.run()