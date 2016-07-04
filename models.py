from database import *
from sqlalchemy.orm import relationship
from slugify import slugify
from wtforms.widgets import * #TextArea
from wtforms import * #TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,validators, ValidationError
import wtforms.widgets.core

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name=  db.Column(db.String(500),nullable=True,unique=True)
    location= db.Column(db.String(500),nullable=True)
    logo=db.Column(db.String(500),nullable=True)
    title=db.Column(db.String(500),nullable=True)
    description=db.Column(db.Text,nullable=True)
    requirement=db.Column(db.Text,nullable=True)
    updated_at=db.Column(db.String(200),nullable=True)
    url = db.Column(db.String(300),nullable=True)

if __name__ == '__main__':
    app.secret_key = "dfd#@C23+"
    app.config['DEBUG'] = True
    app.config['SESSION_TYPE'] = 'filesystem'
   # sess.init_app(app)
    app.debug = True
    manager.run()
    app.run()