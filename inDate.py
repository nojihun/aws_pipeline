import json 
from datetime import datetime

# 저장한 data 불러오기 
with open("data.json", "r") as f:
    raw = json.load(f)


"""inDate 인코딩"""
# 방법 1 
## raw데이터에서 inDate 데이터만 추출 
date = [a['inDate'] for a in raw]
## str -> datetime 변환 
date_time = [datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ') for x in date]
## datetime -> timestamp 변환 
timestamp = [z.timestamp() for z in date_time]

# 방법 2 
## str -> datetime -> timestamp 변환 (for문)
times = []
for i in raw :
    times.append(datetime.strptime(i['inDate'], '%Y-%m-%dT%H:%M:%S.%fZ').timestamp())

# 방법 3 
## str -> datetime -> timestamp 변환 (컴프리헨션)
timess = [datetime.strptime(i['inDate'], '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() for i in raw]

"""inDate 디코딩"""
# 방법 1
## timestamp -> datetime 변환 
con_time = [datetime.fromtimestamp(b) for b in timestamp] 
## datetime -> str 변환 
con_date = [datetime.strftime(c, '%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z' for c in con_time]

# 방법 2 
## timestamp -> datetime -> str 변환 (for 문)
con_d = []
for d in timestamp : 
    con_d.append(datetime.strftime(datetime.fromtimestamp(d), '%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z')

# 방법 3 
## timestamp -> datetime -> str 변환 (컴프리헨션)
conv = [datetime.strftime(datetime.fromtimestamp(v), '%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z' for v in timestamp]

print(conv[0])


