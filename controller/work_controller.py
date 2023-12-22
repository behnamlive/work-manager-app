from model.da import *
from model.entity import *

class WorkController:
    @classmethod
    def save(cls,title,description,start_date,end_date):
        try:
            da = WorkDa()
            work = Work(title,description,start_date,end_date)
            da.save(work)
            return work
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, boss_id, title,description,start_date,end_date):
        try:
            da = WorkDa()
            work = Work(title,description,start_date,end_date)
            work.id = id
            work.boss_id = boss_id
            da.edit(work)
            return work
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = WorkDa()
            work = da.find_by_id(Work, id)
            if work:
                da.remove(work)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_time(cls, datetime1, datetime2):
        try:
            da = WorkDa()
            work_list = da.find_by_time(datetime1, datetime2)
            return work_list
        except Exception as e:
            return False, str(e)


    @classmethod
    def find_by_Boss_id(cls, boss_id):
        try:
            da = WorkDa()
            work_list = da.find_by_Boss_id(boss_id)
            return work_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_task_id(cls, task_id):
        try:
            da = WorkDa()
            work_list = da.find_by_task_id(task_id)
            return work_list
        except Exception as e:
            return False, str(e)


