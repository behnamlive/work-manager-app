from model.da.database import *
from model.entity import *


class WorkDa(DataBaseManager):
    def find_by_task_id(self,wrok_id):
        self.make_engine()
        result = self.session.query(Work).filter(Work.id == wrok_id)
        self.session.close()
        return result

    def find_by_time(self, start_time, end_time):
        self.make_engine()
        result = self.session.query(Work).filter(
            and_(Work.date_time >= start_time, Work.date_time <= end_time))
        self.session.close()
        return result

    def find_by_Boss_id(self, boss_id):
        self.make_engine()
        result = self.session.query(Work).filter(Task.Boss.id == boss_id)
        self.session.close()
        return result