import datetime
import math

expired_time = '2022-03-31 15:10:58'
pay_type = '月'

et = datetime.datetime.strptime(expired_time, '%Y-%m-%d %H:%M:%S')
et_day = et.date()
now = datetime.datetime.now()
et_stamp = et.timestamp()
now_stamp = now.timestamp()
day = (et_stamp - now_stamp) / 86400
remain_day = math.ceil(day)  # 剩余天数

ct = None
if '年' in pay_type:
      ct = datetime.date(et.year - 1, et.month, et.day)

if '月' in pay_type:
      if et.month == 1:
            ct = datetime.date(et.year - 1, 12, et.day)
      else:
            ct = datetime.date(et.year, et.month - 1, et.day)

all_day = (et_day - ct).days  # 支付周期总天数

print(all_day, remain_day)