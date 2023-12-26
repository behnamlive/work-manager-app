from controller import *
from model.da import *
from model.entity import *


class BossController:
    @classmethod
    def save(cls, name,family,username,password,profile_image):
        try:
            da = BossDa()
            if not da.find_by_username(username):
                boss = Boss(name,family,username,password,profile_image)
                da.save(boss)
                return True, boss
            else:
                raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name,family,username,password,profile_image):
        try:
            da = BossDa()
            boss = Boss(name,family,username,password,profile_image)
            boss.id = id
            da.edit(boss)
            return True, boss
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = BossDa()
            boss = da.find_by_id(Boss, id)
            return True, da.remove(boss)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = BossDa()
            return True, da.find_all(Boss)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = BossDa()
            boss = da.find_by_id(Boss, id)
            if boss:
                return True,boss
            else:
                raise NoContentError("There is no profile!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = BossDa()
            return True, da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, username, password):
        try:
            da = BossDa()
            boss = da.find_by_username_password(username, password)
            if (boss):
                return True, boss
            else:
                raise AccessDeniedError("Wrong username/password")
        except Exception as e:
            return False, str(e)
