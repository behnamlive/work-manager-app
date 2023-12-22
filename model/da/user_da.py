from model.da.database import DataBaseManager,and_,or_,between
from model.entity import *


class UserDa(DataBaseManager):
    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(User).filter(
            and_(User.username == username, User.password == password)).all()
        if result:
            return result[0]

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(User).filter(User.username == username).all()
        if result:
            return result[0]
