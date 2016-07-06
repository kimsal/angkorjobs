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
from flask.json import jsonify

#client
limit=30
@app.context_processor
def inject_dict_for_all_templates():
    return dict(categories = Job.query.with_entities(Job.category).distinct('category'),locations = Job.query.with_entities(Job.location).distinct('location'))

@app.errorhandler(404)
def page_not_found(e):
	return "Page not found 404"
	return render_template(template+"/404.html")
@app.route('/jobs/search/<pagination>', methods=['GET'])
@app.route('/jobs/search/', methods=['GET'])
def search(pagination=1):
	search=(str(request.args['q']))#.split()
	search=search.replace(" ",'+')
	#return search
	if search=="":
		return redirect(url_for("index"))
	#return search
	jobs=Job.query.filter((Job.title).match("'%"+search+"%'"),(Job.description).match("%'"+search+"'%")).limit(limit).offset(int(int(int(pagination)-1)*limit))
	#jobs=Job.query.search("manager").all()
	# for job in jobs:
	# 	print job.title
	return render_template("index.html",jobs=jobs,search_str=search,page_type="search")
	return str(jobs)

@app.route('/<pagination>', methods=['GET'])
@app.route('/', methods=['GET'])
def index(pagination=1):
	jobs = Job.query.order_by(Job.id).limit(limit).offset(int(int(int(pagination)-1)*limit))
	#return str(jobs)
	return render_template("index.html",page_name='home',jobs=jobs,page_type="index")
@app.route('/pagin/<pagination>', methods=['GET'])
def get_Job_Index(pagination=1):
	jobs = Job.query.order_by(Job.id).limit(limit).offset(int(int(int(pagination)-1)*limit))
	serialized = json.dumps([job.to_Json() for job in jobs])
	return serialized

@app.route('/jobs/search/<pagination>', methods=['GET'])
@app.route('/jobs/search/<pagination>/', methods=['GET'])
def get_Job_search(pagination=1):
	search=(request.args['q']).replace(" ",'+')
	jobs = Job.query.filter((Job.description).match("'%"+search+"%'"),(Job.title).match("%'"+search+"'%")).limit(limit).offset(int(int(int(pagination)-1)*limit))
	serialized = json.dumps([job.to_Json() for job in jobs])
	return serialized
@app.route('/search/<category>/<location>/<pagination>', methods=['GET'])
@app.route('/search/<category>/<location>/<pagination>', methods=['GET'])
def get_Job_category_location(category='',location='',pagination=1):
	#==1 if not selected
	category=category.replace(" ",'+')
	location=location.replace(" ",'+')
	if category=='1':
		if location=='1':
			return redirect(url_for("index"))
		else:
			jobs = Job.query.filter((Job.location).match("%'"+location+"'%")).limit(limit).offset(int(int(int(pagination)-1)*limit))
	elif location=='1':
		if category=='1':
			return redirect(url_for("index"))
		else:
			jobs = Job.query.filter((Job.category).match("%'"+category+"'%")).limit(limit).offset(int(int(int(pagination)-1)*limit))
	else:
		jobs=''
		#jobs = Job.query.filter((Job.category).match("%'"+category+"'%")).limit(limit).offset(int(int(int(pagination)-1)*limit))
	serialized = json.dumps([job.to_Json() for job in jobs])
	return serialized

if __name__ == '__main__':
	 app.run(debug = True)




#replace white space:
#http://docs.python-requests.org/en/master/user/quickstart/