from datetime import date
def date_submonth(ds,m=1):
    '''
    :param ds: datetime.date
    :param month:  int <12
    :return: datetime.date
    '''
    if m>12:
        print("month should be lq 12")
        return None
    month_ds=ds.month
    year_update = ds.year
    month_update = ds.month
    day_update = ds.day
    if month_ds<=m:
        year_update = year_update-1
        month_update = 12+month_update-m

    else:
        month_update = month_update-m
    return date(year_update,month_update,day_update)