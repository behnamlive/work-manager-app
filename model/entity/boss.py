from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.entity import *

class Boss(Base):
    __tablename__ = 'boss_tbl'
    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30),unique=True)
    password = Column(String(30))
    profile_image = Column(String(100),default=None)

    work_rel = relationship("Work", back_populates="boss_rel")

    def __init__(self,name,family,username,password,profile_image):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.profile_image = profile_image


a = Boss('behnam','masoumi','behnamlive','behnam123','12345')
print(a)
