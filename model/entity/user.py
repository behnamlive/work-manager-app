from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.entity import *
class User(Base):
    __tablename__ = 'user_tbl'
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30),unique=True)
    password = Column(String(30))
    profile_image = Column(String(100))
    roll = Column(Integer)

    tu_rel = relationship("Task_User", back_populates="tu_rel_user")
    #task_rel2 = relationship("Task", back_populates="user_rel")

    def __init__(self,name,family,username,password,profile_image,roll):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.profile_image = profile_image
        self.roll = roll

