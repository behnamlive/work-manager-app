from model.da import *
from model.entity import *

class TaskController:
    @classmethod
    def save(cls, work, title,description,start_date,end_date):
        try:
            da = TaskDa()
            task = Task(work,title,description,start_date,end_date)
            da.save(task)
            return task
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, work_id, title,description,start_date,end_date):
        try:
            da = TaskDa()
            task = Task(title,description,start_date,end_date)
            task.id = id
            task.work_id = work_id
            da.edit(task)
            return task
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = TaskDa()
            task = da.find_by_id(Task, id)
            if task:
                da.remove(task)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_time(cls, datetime1, datetime2):
        try:
            da = TaskDa()
            post_list = da.find_by_time(datetime1, datetime2)
            return post_list
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_work_id(cls, work_id):
        try:
            da = TaskDa()
            task_list = da.find_by_work_id(work_id)
            return task_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_task_id(cls, task_id):
        try:
            da = TaskDa()
            task_list = da.find_by_task_id(task_id)
            return task_list
        except Exception as e:
            return False, str(e)


