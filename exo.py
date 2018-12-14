from flask import Flask,render_template,request
import math
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index1.html')

@app.route("/about.html")
def about():
    return render_template('about.html')
@app.route("/position.html")
def position():
    return render_template('position.html')

@app.route("/orbital.html")
def orbital():
    return render_template('orbital.jinja2')
@app.route("/possibility.html")
def possibility():
    return render_template('possibility.html')


@app.route("/divide")
def divide():
    return render_template("divide.jinja2")
@app.route('/divide_result', methods=['POST'])
def divide_result():
    number = float(request.form['number'])
    divide_by = float(request.form['divide_by'])
    mass2=float(request.form['mass2'])
    return render_template('divide_result.jinja2', result=2*3.14*(math.sqrt((number*number*number)/(6.67e-11*(divide_by+mass2)))))


app.run(debug=True)