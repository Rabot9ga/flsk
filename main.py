from flask import Flask, render_template, url_for
import os

app=Flask(__name__)

@app.route('/hello/<user>')
def home(user):
    return 'hello: ' + user

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

@app.route('/add/<int:x>/<int:y>')
def adding(x, y):
    return str(x+y)

@app.route('/long/<x>/<y>/<z>')
def longest(x, y, z):
    a=sorted([x, y, z], key=len)
    return a[-1]

@app.route('/path/<file>')
def path(file):
    if file in os.listdir(path=os.getcwd()):
        return 'yes'
    return 'no'

if __name__=='__main__':
    app.run(debug=True)