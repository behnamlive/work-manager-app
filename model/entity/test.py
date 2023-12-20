from model.entity import *
from model.da.database import *

da = DataBaseManager()

a = Boss('behnam2','masoumi2','behnamlive3','behnam123','12345')
b = Work(a,'salam khubi','injure doroste',None,None)
d= User('behnam','masoumi','behnamlive126','behnam126',None,1)
c = Task(b,d,'hamali','bayad hamali bokoni',None,None)
da.save(d)