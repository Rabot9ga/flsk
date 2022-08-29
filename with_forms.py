from flask import Flask, request

# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from datetime import datetime


class MyForm(Form):
    name = StringField('Name', [InputRequired()])

    def validate_month(form, field):
        if field.data > 50:
            raise ValidationError('Name must be less than 50 characters')



class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email()
    ])
    job = StringField(label='Job', validators=[
        validators.InputRequired(),
        validators.AnyOf(('IT', 'Bank', 'HR'))
    ])
    month = StringField(label='month', validators=[
        validators.validate_month()
    ])
    



app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200

if __name__ == '__main__':
    app.run()
