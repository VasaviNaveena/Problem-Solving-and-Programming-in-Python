from datetime import date
from_date = date(2019, 1, 1)
to_date = date(2019, 4, 20)
x = to_date - from_date
print(x.days, "days")
