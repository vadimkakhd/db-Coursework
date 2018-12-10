from wtf.form.user_delete import UserDelete
from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def delete():
    form = UserDelete()


    allUsers = getUsers()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user_delete.html', myform=form, users=allUsers)
        else:
            del_user(
                u_nickname=request.form["deleteUser"])

            return render_template('user_delete.html', myform=form, users=allUsers)

    return render_template('user_delete.html', myform=form, users=allUsers)




if __name__ == '__main__':
    app.run(debug=True)
