
from model.da.database import *

da = DataBaseManager()

a = Boss("aaa111", "bbbb", "ahmad", "ahmad123",'adss')
b = User('reza','ahmadi','reza@ahmadi',123,'asd',1)
c = Work(a,'salam','man hastam',None,None)
d= Task(c,'zaraban','zaraban ghalb',None,None)


da.save(d)