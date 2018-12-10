from flask import Flask, render_template, request, make_response, session, url_for, redirect
from wtf.form.login import LoginForm
from datetime import datetime, timedelta
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
# csrf = CSRFProtect(app)
app.secret_key = 'My_key'


# form = LoginForm()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    # global form
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
            return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
        else:
            username = request.cookies.get('cookie_name_1')
            if username is None:
                return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"
            return "Logged in as " + username + "<br>" + "<b><a href = '/logout'>click here to log out</a></b>"
    if request.method == 'POST':
        if 'username' in session:
            username = session['username']
            return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
        else:
            username = request.cookies.get('cookie_name_1')
            session['username'] = request.form['username']
            if username is None:
                if form.validate() == False:
                    return render_template('login.html', myform=form)
                else:
                    response = make_response('You log in!')
                    expires = datetime.now()
                    expires += timedelta(days=60)
                    response.set_cookie('cookie_name_1', request.form['username'], expires=expires)

                    return response
            return "Logged in as " + username + "<br>" + "<b><a href = '/logout'>click here to log out</a></b>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # global form
    if request.method == 'GET':
        return render_template('login.html', myform=form)


@app.route('/logout')
def logout():
    session.pop('username', None)

    response = make_response('You log out!')
    response.set_cookie('cookie_name_1', '', expires=0)
    return response

if __name__ == '__main__':
    app.run()
