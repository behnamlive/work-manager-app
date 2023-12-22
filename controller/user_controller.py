from controller import *
from model.da import *
from model.entity import *


class UserController:
    @classmethod
    def save(cls,name,family,username,password,profile_image,roll):
        try:
            da = UserDa()
            if not da.find_by_username(username):
                user = User(name,family,username,password,profile_image,roll)
                da.save(user)
                return True, user
            else:
                raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id,name,family,username,password,profile_image,roll):
        try:
            da = UserDa()
            user = User(name,family,username,password,profile_image,roll)
            User.id = id
            da.edit(user)
            return True, user
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = UserDa()
            user = da.find_by_id(User, id)
            return True, da.remove(user)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = UserDa()
            return True, da.find_all(User)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = UserDa()
            user = da.find_by_id(User, id)
            if user:
                return True,user
            else:
                raise NoContentError("There is no profile!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = UserDa()
            return True, da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, username, password):
        try:
            da = UserDa()
            user = da.find_by_username_password(username, password)
            if (user):
                return True, user
            else:
                raise AccessDeniedError("Wrong username/password")
        except Exception as e:
            return False, str(e)
