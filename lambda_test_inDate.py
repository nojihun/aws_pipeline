import Pipeline
"""
    lambda 테스트용 py 파일입니다 
    현재 s3에서 변환된 gz파일을 가져와서 압축해제 및 복원 까지 가능합니다
    여기에 쿼리랑 섞으면 될것같습니다
"""

def lambda_handler(event, context):
    time1= event['time1']
    time2= event['time2']
    
    data=Pipeline.download_json_gz('data_trans.json.gz')
    data=Pipeline.key_enc(data,2) # key 복원
    data=Pipeline.indate_trans(data,2) # indate 복원
    data=Pipeline.url_trans(data,2) # url 복원
    data=Pipeline.table_trans(data,2)# db생성 및 복원
    
    result=[]
    if time1:
        for i in data[:]:
            if i['inDate'] <= time1 and i['inDate'] >= time2:
                result.append(i)
        data =result
       
    return data
