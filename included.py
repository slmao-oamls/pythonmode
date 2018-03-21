from datetime import datetime,timedelta

# now=datetime.now()
# print(now)

# dt=datetime(2015,6,2,18,20)
# print(dt,dt.timestamp())
# st=dt.timestamp()

# print(datetime.fromtimestamp(st))

# cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
# print(cday)

now=datetime.now()
print(now)

print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=14))