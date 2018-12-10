from flask import Flask, render_template, request
from wtf.form.user import UserForm

from functions import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def user():
    form = UserForm()


    allUsers = getUsers()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user.html', myform=form, users=allUsers)
        else:
            add_user(
                u_nickname=request.form["username"],
                u_login=request.form["login"],
                u_pass=request.form["password"],
                u_name=request.form["name"],
                u_surname=request.form["surname"],
                u_faculty=request.form["faculty"],
                u_course=request.form["course"]
            )

            return render_template('user.html', myform=form, users=allUsers)

    return render_template('user.html', myform=form, users=allUsers)

# @app.route('/delete', methods=['GET', 'POST'])
# def delete():


if __name__ == '__main__':
    app.run(debug=True)
