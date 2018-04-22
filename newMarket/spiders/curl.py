# coding=utf-8
from timeParser import  date_submonth
import datetime
import urllib
import urllib2

#================代理设置====================================

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H448WW3T6G0ODEQD"
proxyPass = "8F7F50F6EB37E7F3"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxy_handler = urllib2.ProxyHandler({
    "http": proxyMeta,
    "https": proxyMeta,
})

opener = urllib2.build_opener(proxy_handler)

urllib2.install_opener(opener)

#================代理==============================


values = {}
now = datetime.datetime.now()
this_year = now.strftime("%Y")
last_year = (int(now.strftime("%Y")) -1).__str__()
this_month = now.strftime("%m")
last_month = date_submonth(now,1).strftime("%m")


def curl(region_hidden, region):
    values['device'] = "Mobile"
    values['device_hidden'] = "mobile"
    values['statType_hidden'] = "os_combined"
    values['region_hidden'] = region_hidden  ##国家代码
    values['granularity'] = "monthly"
    values['statType'] = "Operating System"
    values['region'] = region    ###变量list for循环 国家
    values['fromInt'] = last_year + this_month
    values['toInt'] = this_year + last_month
    values['fromMonthYear'] = last_year + "-" + this_month
    values['toMonthYear'] = this_year + "-" + last_month
    values['hideCaption'] = "true"
    values['bottomLegend'] = "true"
    values['siteStyling'] = "true"
    values['siteChartMargins'] = "true"
    values['setChartTitle'] = "Mobile Operating System Market Share "+ region
    data = urllib.urlencode(values)
    url = "http://gs.statcounter.com/os-market-share/mobile/"+region.lower()+"/chart.php"
    geturl = (url + "?" + data).replace(" ","%20")
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    return response.read()

