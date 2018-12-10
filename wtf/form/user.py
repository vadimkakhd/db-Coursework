from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class UserForm(FlaskForm):
    username = StringField('Username: ', validators=[validators.DataRequired('Required')])
    password = StringField('Password: ', validators=[validators.DataRequired('Required')])
    login = StringField('login: ', validators=[validators.DataRequired('Required')])
    name = StringField('name: ')
    surname = StringField('surname: ')
    faculty = StringField('faculty: ', validators=[validators.DataRequired('Required')])
    course = StringField('course: ', validators=[validators.DataRequired('Required')])


    addbutton = SubmitField('Add')


