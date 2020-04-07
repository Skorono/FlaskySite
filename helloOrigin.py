import config
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, session
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Required,Email
from acceptcode.EmailSend import SendYandexEmail


app = Flask(__name__)

app.config['SECRET_KEY'] = 'EQV4z38I1E2n9t4g1Sz1'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class LinePasswordField(FlaskForm):
	password = PasswordField('Input your password here:', validators=[Required()])
	sumbit = SubmitField('Sumbit')

class LineRegisterField(FlaskForm):
	email = StringField('Enter your Email addres:', validators=[Email()])	
	submit = SubmitField('Submit')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



@app.route('/home')
def welcome():
	return render_template('welcome.html')



@app.route('/stranger')
def warning():
	return render_template('youarenotregisteredmiserablehuman.html')	



@app.route('/register', methods=['GET','POST'])
def reg():
	line = LineRegisterField()
	email = SendYandexEmail(config.email, config.password, line.email.data)	
	session['email_password'] = email.message
	if line.validate_on_submit():
		email.send()
		return redirect(url_for('index'))
	return render_template('register.html', register_line=line)



@app.route('/', methods=['GET','POST'])
def index():
	line = LinePasswordField()
	if session.get('email_password') is None:
		return redirect(url_for('warning'))		
	else:	
		if line.password.data == session.get('email_password'):
			return redirect(url_for('welcome'))
		else:	
			return render_template('keycheck.html', line=line)



@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



@app.route('/photo')
def galery():
	return render_template('illustration.html')

if __name__ == '__main__':
    manager.run()
