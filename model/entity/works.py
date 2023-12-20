from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.entity import *
from datetime import datetime

class Work(Base):
    __tablename__ = 'work_tbl'
    id = Column(Integer, primary_key=True)
    boss_id = Column(Integer, ForeignKey("boss_tbl.id"))
    title = Column(String(100))
    description = Column(String(300))
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(DateTime,default= None)

    boss_rel = relationship("Boss", back_populates="work_rel")
    task_rel = relationship("Task", back_populates= "work_rel2")

    def __init__(self, boss, title,description,start_date,end_date):
        self.boss=boss
        self.title=title
        self.description=description
        self.start_date= start_date
        self.end_date=end_date

