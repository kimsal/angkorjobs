from database import *
from sqlalchemy.orm import relationship
from slugify import slugify
#from wtforms.widgets import * #TextArea
from wtforms import * #TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,validators, ValidationError
#import wtforms.widgets.core
import sys
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
if sys.version_info >= (3, 0):
    enable_search = False
else:
    enable_search = True
    import flask.ext.whooshalchemy as whooshalchemy
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name=  db.Column(db.String(500),nullable=True)
    location= db.Column(db.String(500),nullable=True)
    logo=db.Column(db.String(500),nullable=True)
    title=db.Column(db.String(500),nullable=True) #,unique=True
    category=db.Column(db.String(120),nullable=True) #,unique=True
    description=db.Column(db.Text,nullable=True)
    requirement=db.Column(db.Text,nullable=True)
    updated_at=db.Column(db.String(200),nullable=True)
    contract_type = db.Column(db.String(200),nullable=True)
    url = db.Column(db.String(300),nullable=True)
    def to_Json(self):
        return dict(
            id=self.id,
            company_name=self.company_name,
            location=self.location,
            logo=self.logo,
            title=self.title,
            category=self.category,
            description=self.description,
            requirement=self.requirement,
            updated_at=self.updated_at,
            contract_type=self.contract_type,
            url=self.url
            )
if __name__ == '__main__':
    app.secret_key = "dfd#@C23+"
    app.config['DEBUG'] = True
    app.config['SESSION_TYPE'] = 'filesystem'
   # sess.init_app(app)
    app.debug = True
    manager.run()
    app.run()