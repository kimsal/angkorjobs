#from api import *
from database import *
import os.path as op
import os
import flask
#from views import *
from flask import abort,Flask,g, render_template,request,session,redirect,url_for,flash
from werkzeug import secure_filename
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,validators, ValidationError
import math
from models import *
#client
@app.errorhandler(404)
def page_not_found(e):
	return "Page not found 404"
	return render_template(template+"/404.html")
@app.route('/')
@app.route('/<pagination>')
def index(pagination=1):
	limit=30
	jobs = Job.query.order_by(Job.id).limit(limit).offset(int(int(int(pagination)-1)*limit))
	#return str(jobs)
	return render_template("index.html",page_name='home',jobs=jobs)

if __name__ == '__main__':
	 app.run(debug = True)




#replace white space:
#http://docs.python-requests.org/en/master/user/quickstart/