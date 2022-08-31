from flask import Flask, render_template, url_for, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Pages %r>' % self.id


@app.route('/hello/<user>')
def home(user):
    return 'hello: ' + user


@app.route('/create-text', methods=['POST', 'GET'])
def create_text():
    if request.method=='POST':
        title=request.form['name']
        text=request.form['text']
        page=Pages(name=title, text=text)
        try:
            db.session.add(page)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'Its some trouble'
    else:
        return render_template('create.html')


@app.route('/posts')
def posts():
    texts = Pages.query.order_by(Pages.date.desc()).all()
    return render_template('posts.html', pages=texts)


@app.route('/posts/<int:id>')
def posts_id(id):
    text = Pages.query.get(id)
    return render_template('posts_text.html', page=text)


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