# coding=utf-8
from Result import *
import urllib
import urllib2
from collections import OrderedDict

record1 = Record()
record2 = Record()
record3 = Record()
record4 = Record()
record5 = Record()
record6 = Record()
record7 = Record()

records=[
record1,
record2,
record3,
record4,
record5,
record6,
record7
]

region_hidden = ['SA','IE','MA','KZ','LB','ES','IT']
region_dict_english = {'SA':'Saudi Arabia', 'IE':'Ireland','MA':'Morocco','KZ':'Kazakhstan','LB':'Lebanon','ES':'Spain','IT':'Italy'}
region_dict_chinese={'SA':'沙特', 'IE':'爱尔兰','MA':'摩洛哥','KZ':'哈萨克斯坦','LB':'黎巴嫩','ES':'西班牙','IT':'意大利'}
print region_dict_english[region_hidden[0]]
print region_dict_chinese[region_hidden[0]]