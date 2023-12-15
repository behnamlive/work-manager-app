from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from model.entity.base import Base
from datetime import datetime

class Work(Base):
    __tablename__ = 'work_tbl'
    work_id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("user_tbl.userid"))
    title = Column(String(100))
    description = Column(String(300))
    explain = Column(String(30))
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(DateTime)
    do_time = Column(DateTime, default=datetime.now())

    # relationship

    def __init__(self, user, title,description,explain,start_date,end_date,do_time):
        self.user=user
        self.title=title
        self.description=description
        self.explain=explain
        self.start_date= datetime.now()
        self.end_date=end_date
        self.do_time= datetime.now()
