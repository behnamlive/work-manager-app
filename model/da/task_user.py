from model.da.database import *
from model.entity import *


class Task_User_Da(DataBaseManager):
    def find_by_id(self, id):
        self.make_engine()
        result = self.session.query(Task_User).filter(Task_User.id == id)
        self.session.close()
        return result


    def find_by_task_id(self, task_id):
        self.make_engine()
        result = self.session.query(Task_User).filter(Task_User.task_id == task_id)
        self.session.close()
        return result


    def find_by_user_id(self,user_id):
        self.make_engine()
        result = self.session.query(Task_User).filter(Task_User.user_id ==user_id)
        self.session.close()
        return result