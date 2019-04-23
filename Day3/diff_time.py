from datetime import datetime as DT
time1 = '1:00:00'
time2 = '12:00:00' 
Format = '%H:%M:%S'
diff_time = DT.strptime(time2, Format) - DT.strptime(time1, Format)
print(diff_time)
