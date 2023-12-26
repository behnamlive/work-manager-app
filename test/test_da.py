from model.da import*
from model.entity import *

a = Boss("Ahmad","Messbah","aaa", "bbb",'hhhh')
a_da = BossDa()
#a_da.save(a)
b =a_da.find_all
c =a_da.find_by_username('aaa')
print(c)