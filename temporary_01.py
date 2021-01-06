import datetime
import calendar

expired_time = '2021-01-04'
pay_type = '月'

et = datetime.datetime.strptime(expired_time, '%Y-%m-%d').date()
today = datetime.date.today()
print(et, today)

if pay_type == '年':
    ct = datetime.date(et.year - 1, et.month, et.day)

if pay_type == '月':
    if et.month == 1:
        ct = datetime.date(et.year - 1, 12, et.day)
    else:
        ct = datetime.date(et.year, et.month - 1, et.day)

print(ct)