from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.entity import *
from datetime import datetime

class Task(Base):
    __tablename__ = 'task_tbl'
    id = Column(Integer, primary_key=True)
    work_id = Column(Integer, ForeignKey("work_tbl.id"))
    user_id = Column(Integer, ForeignKey("user_tbl.id"))
    title = Column(String(100))
    description = Column(String(300))
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(DateTime, default= None)


    work_rel2 = relationship("Work", back_populates= "task_rel")
    #tu_rel2 = relationship("Task_User", back_populates="tu_rel_task")
    user_rel = relationship("User", secondary="Task_User", back_populates="task_rel2")

    def __init__(self, work,user, title,description,start_date,end_date):
        self.work=work
        self.user= user
        self.title=title
        self.description=description
        self.start_date= start_date
        self.end_date=end_date