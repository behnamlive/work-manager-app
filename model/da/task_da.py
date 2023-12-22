from model.da.database import *
from model.entity import *


class TaskDa(DataBaseManager):
    def find_by_task_id(self, task_id):
        self.make_engine()
        result = self.session.query(Task).filter(Task_User.id == task_id)
        self.session.close()
        return result

    def find_by_time(self, start_time, end_time):
        self.make_engine()
        result = self.session.query(Task_User).filter(
            and_(Task.start_time >= start_time, Task.end_time <= end_time))
        self.session.close()
        return result

    def find_by_work_id(self,work_id):
        self.make_engine()
        result = self.session.query(Task).filter(Task.Work.id ==work_id)
        self.session.close()
        return result