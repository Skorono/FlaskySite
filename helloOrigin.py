from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import Required
from acceptcode.main import email 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'EQV4z38I1E2n9t4g1Sz1'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class LinePasswordField(FlaskForm):
	password = PasswordField('Input your password here:', validators=[Required()])
	sumbit = SubmitField('Sumbit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/home')
def welcome():
	return render_template('welcome.html')

@app.route('/', methods=['GET','POST'])
def index():
	line = LinePasswordField()
	email.send()
	if line.password.data == email.message:
		return redirect(url_for('welcome'))
	return render_template('keycheck.html', line=line)	


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/photo')
def galery():
	return render_template('illustration.html')

if __name__ == '__main__':
    manager.run()