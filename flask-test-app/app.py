from flask import render_template, redirect, url_for, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('user_index', username='Lou428'))


@app.route('/user/<username>')
def user_index(username):
    return render_template('user.html', username=username)


