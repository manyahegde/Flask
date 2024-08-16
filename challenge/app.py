from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def rootpage():
    weight=None
    height=None
    bmi=None
    if request.method=='POST' and 'weight' in request.form and 'height' in request.form:
        weight=float(request.form.get('weight'))
        height=float(request.form.get('height'))/100
        bmi=round(weight/(height**2),2)
    return render_template('index.html', weight=weight, height=height, bmi=bmi)
if __name__ == '__main__':
    app.run(debug=True)



