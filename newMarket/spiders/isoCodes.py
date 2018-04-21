# coding=utf-8
import urllib
import urllib2
from timeParser import  date_submonth


from Result import *
import datetime
from datetime import date
import lxml.html as HTML



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




values = {}

now = datetime.datetime.now()
this_year = now.strftime("%Y")
last_year = (int(now.strftime("%Y")) -1).__str__()
this_month = now.strftime("%m")
last_month = date_submonth(now,1).strftime("%Y%m")
print(last_month)


values['fromInt'] =last_year + this_month
values['fromInt'] = "201703"
values['toInt'] = "201802"
values['fromMonthYear'] = "2017-04"
values['toMonthYear'] = "2018-03"


# for index in range(len(records)):

values['device'] = "Mobile"
values['device_hidden'] = "mobile"
values['statType_hidden'] = "os_combined"
values['region_hidden'] = "IQ"
values['granularity'] = "monthly"
values['statType'] = "Operating%20System"
values['region'] = "Iraq"
values['fromInt'] = "201703"
values['toInt'] = "201802"
values['fromMonthYear'] = "2017-04"
values['toMonthYear'] = "2018-03"
values['hideCaption'] = "true"
values['bottomLegend'] = "true"
values['siteStyling'] = "true"
values['siteChartMargins'] = "true"
values['setChartTitle'] = "Mobile%20Operating%20System%20Market%20Share%20Iraq"
data = urllib.urlencode(values)
url = "http://gs.statcounter.com/os-market-share/mobile/iraq/chart.php"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
# print response.read()




now = datetime.datetime.now()
this_year = now.strftime("%Y")
last_year = (int(now.strftime("%Y")) -1).__str__()
this_month = now.strftime("%m")
last_month = (int(now.strftime("%m")) -1).__str__()
values['fromInt'] =last_year + this_month









