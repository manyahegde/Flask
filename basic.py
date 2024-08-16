from flask import Flask

app=Flask(__name__)

@app.route('/') # decorator - provides additional functionality to an existing function
def welcome():
    return 'This is my first Flask app'
# if we dont use decorator, welcome() will just return but where? riute tells where to return. '/' is base directory, if someone opens this url, they will see the return value of the welcome()

@app.route('/potato') # in the url add /potato
def potato():
    return 'This is potato page'

@app.route('/yay') # in the url add /yay
def yay():
    return 'This yay page'

app.run()