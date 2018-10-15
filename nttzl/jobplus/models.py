from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.Datetime,default=datetime.utcnow)
    updated_at = db.Column(db.Datetime,default=datetime.utcnow,onupdate=datetime.utcnow)

user_job = db.Table(
        'user_job',
        db.Column('user_id',db.Integer,db.ForeignKey(user.id,ondelete='CASCADE')),
        db.Column('job_id',db.Integer,db.ForeignKey(job.id,ondelete='CASCADE'))
        )

class User(Base):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),nullable=False,unique=True,index=True)
    email = db.Column(db.String(64),nullable=False,unique=True,index=True)
    _password = db.Column('password',db.String(256),nullable=False)
    role = db.Column(db.SmallInteger,default=ROLE_USER)
    company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='SET NULL'))
    company = db.relationship('Company')
    resume_url = db.Column(db.String(64))
    jobs = db.relationship('Job',secondary='user_job')

class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),nullable=False,unique=True,index=True)
    site = db.Column(db.String(64))
    description = db.Column(db.Text)
    logo_url = db.Column(db.String(64))
    tags = db.Column(db.String(64))
    stack = db.Column(db.String(64))
    finance = db.Column(db.String(8))
    location = db.Column(db.String(64))
    job = db.ralation('Job')


class Job(Base):
    __tablename__ = 'position'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),nullable=False)
    salary = db.Column(db.String(32))
    experience = db.Column(db.String(8),default='0')
    location = db.Column(db.String(16))
    is_fulltime = db.Column(db.Boolean,default=True)
    is_open = db.Column(db.Boolean,default=True)
    description = db.Column(db.text)
    requirement = db.Column(db.text)

    company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='SET NULL'))
    company = db.relationship('Company',userlist=False)
    
class Delivery(Base):
    __tablename__ = 'delivery'
    
    STATUS_WAITING = 10
    STATUS_REJECT = 20
    STATUS_ACCEPT = 30

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
    status = db.Column(db.SmallInteger,default=STATUS_WAITING)
    
    response = db.Column(db.Text)



