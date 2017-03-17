from datetime import datetime
from datetime import timedelta
now=datetime.now()
print ('%s%s%s' &(now.date,now.month,now.year))

print (now)
tomorrow=now -timedelta(days=1)
print (tomorrow)