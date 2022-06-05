def make_table(data): # tableAndColumns 에 있는 내용들을 간단하게 정리하기 위해 게임 아이디 별로 내용을 분류하기 위한 함수
  table ={}
  for i in data:
    if i['game_id'] not in table.keys():#게임아이디로 이루어진 key값이 있나 확인
      z = i['game_id']
      table[z] = {}#게임아이디와 짝지어질 dict만들기
      if i['tableAndColumn'] not in table[z].values():#tableAndColumn 내용이 게임아이디의 값에 있나 확인.
        ind= len(table[z])#dict에 있는 거 갯수
        table[z][ind]=i['tableAndColumn'] #위의 갯수를 키로 이용해서 dict에 넣는다.
    elif i['game_id'] in table.keys():#이미 게임 아이디로 만들어진 값이 있다면 새로운 딕셔너리를 만들지 않고 위의 반복
      z = i['game_id'] 
      if i['tableAndColumn'] not in table[z].values():
        ind= len(table[z])
        table[z][ind]=i['tableAndColumn']
  return table
"""
위에서 만들어진 table은 
{게임아이디: {0: tableAndColumn 내용,
            1: tableAndColumn 내용2 
            ...}.
}
이런 식으로 만들어 진다.
"""


def table_enc(data,table):# 넣을때 json 파일 전체를 넣어야함. 그래야 game id로 구별 가능, 무조건 위에 make table을 먼저 거칠것!
  result = []

  for i in data:
    z = format(i['game_id'], '04')# 인코딩할때 숫자에서 게임아이디와 키값을 찾기 편하기 위해서 게임아이디를 4자리로 만든다.
    for key,value in table[i['game_id']].items():
      if i['tableAndColumn'] == value:
        a = format(key, '02')# 인코딩할때 숫자를 찾기 쉽기 위해 키값을 두자리로 만든다.
    b = z+a
    result.append(b)
  return result

def table_dec(data, table): 여기서에 데이터는 위에 table_enc를 거친 데이터이다.
  result1= []
  for i in data:
    a= int(i[:4]) # 6글자중 앞에 4글자는 game_id
    b= int(i[4:]) #6글자 중 뒤에 2글자는 원래 데이터가 저장되어 잇는 table 키
    c = table[a][b] #원래 데이터
    result1.append(c) 
  return result1
