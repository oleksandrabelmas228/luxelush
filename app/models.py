import sqlalchemy as sa
import sqlalchemy.orm
from app import db


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    balance = db.Column(db.Float(), default=0)

    def __repr__(self):
        return "User: {}".format(self.username)

    # u = Users(username='sasha', password='1234', email='sdafsadfdsf')