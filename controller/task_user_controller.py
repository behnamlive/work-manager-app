from model.da import *
from model.entity import *

class Task_User_Controller:
    @classmethod
    def save(cls,user,task,comment):
        try:
            da = TaskDa()
            task_user = Task(user,task,comment)
            da.save(task_user)
            return task_user
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, task_id, user,task,comment):
        try:
            da = Task_User_Da()
            task_user = Task_User(user,task,comment)
            task_user.id = id
            task_user.profile_id = task_id
            return task_user
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = Task_User_Da()
            post = da.find_by_id(Task_User, id)
            if post:
                da.remove(post)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, task_user_id):
        try:
            da = Task_User_Da()
            task_user_list = da.find_by_id(task_user_id)
            return task_user_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_task_id(cls, task_id):
        try:
            da = Task_User_Da()
            post_list = da.find_by_task_id(task_id)
            return post_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_user_id(cls, user_id):
        try:
            da = Task_User_Da()
            post_list = da.find_by_user_id(user_id)
            return post_list
        except Exception as e:
            return False, str(e)
