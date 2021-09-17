from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = SQLAlchemy()


class BaseModelMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    

class Usert(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    key = db.Column(db.String)
    def __init__(self, id,usuario, key):
        self.id = id
        self.usuario = usuario
        self.key = key
    def __str__(self):
        return f'{self.key}'

engine = create_engine('sqlite:///films.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

