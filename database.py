from sqlalchemy import create_engine
from flask import Flask,session,json,request
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from  sqlalchemy.sql.expression import func
#from passlib.apps import custom_app_context as pwd_context
from passlib.apps import * 
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from flask_httpauth import HTTPTokenAuth
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://angkorjobs:angkorjobs@localhost:5432/angkorjobs'
auth = HTTPTokenAuth(scheme='Token')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.secret_key = 'Hello@AmokCamSmallworld$Cambodia&*&'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
SECRET_KEY="!Amok123#smallworld_common_toursanak_amok"
def init_db():
    #import BLOG.models
    Base.metadata.create_all(bind=engine)