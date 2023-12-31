from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.entity import *
class Task_User(Base):
    __tablename__ = 'task_user_tbl'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_tbl.id"))
    task_id = Column(Integer, ForeignKey("task_tbl.id"))
    comment = Column(String(300))


    tu_rel_user = relationship("User", back_populates="tu_rel")
    tu_rel_task = relationship("Task", back_populates="tu_rel2")

    def __init__(self,user,task,comment):
        self.user = user
        self.task = task
        self.comment = comment
