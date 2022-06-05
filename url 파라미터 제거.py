import pandas as pd

data = pd.read_csv('data.csv')

url = data['url']
count = 0

for i in url:
  b = i.split('/') #url을 /로 나누어서 내용대로 나눈다.
  index = len(b)
  for i in range(len(b)):# 나눠진 url을 하나씩 불러온다.
    if '-' in b[i]:# uuid나 시간으로 표시되어 있는 url 내용을 없애기 위해서 uuid랑 시간에만 포함되어있는 -를 검색한다. 
        index = i
    elif b[i].isdigit():
        index = i
        break
  b= b[:index] # -가 검색이 되면 그 뒤로 다 날려버린다.
  if '?' in b[-1]: # 파라미터 값중 ?뒤로 j쿼리 같은게 있으니 날린다.
    index = b[-1].find('?')
    b[-1] =  b[-1][:index]
  elif '%' in b[-1]:# %가 url 인코딩? 이런게 있으니 없앤다.
    index = b[-1].find('%')
    b[-1] =  b[-1][:index]
  i ='/'.join(b) # 파라미터를 다 제거햇으니 다시 합친다. 
  url[count] = i
  count+= 1
  
data.to_csv('data(url-고침)-2차.csv', index=False, encoding='cp949')
