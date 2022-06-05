"""
Kinesis 전송 스트림에서 받은 데이터를 필터링하여 리턴한다. 
해당 데이터는 S3 "filtered-data-logs"에 저장된다.
Reference: https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html
Written by yongs on 2021.12.14.
"""
import json
import boto3


s3= boto3.client('s3')
result = []

def lambda_handler(event, context):
    resp = s3.select_object_content( Bucket='ai05p2test', # Put your own bucket name here. 
    Key='sample_data.csv.gz', # Put your own key name here. 데이터 명
    Expression="SELECT * FROM s3object s", # sql 표현식. 컬럼명 표현할때 \"컬럼명\" 이런식으로 표현해야 됨
    ExpressionType='SQL', 
    InputSerialization= {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'GZIP'}, OutputSerialization={'JSON': {}}, )

    for event in resp['Payload']: 
        if 'Records' in event: 
            a= event['Records']['Payload'].decode('utf-8')
            result.extend(a)
            
    result1 = "".join(result) #a가 하나하나가 글자 하나씩이라서 합쳐준다.
    result2 =result1.split('{')#한 문자열로 합쳐진것을 '{' 단위로 나눠주어서 데이터 하나씩으로 나눠준다.
    result3 = []
    count = 0
    for i in result2:#데이터가 하필 tablecoulum에 {가 또 있어서 그거를 합쳐야 한다.
        if 'tableName' in i:# tablecoulum에 tableName이라는 index가 있어서 그거를 찾아서 앞에 합쳐준다.
            result3[count-1] = result3[count-1]+'{' + i 
            
        elif 'tabelName' not in i:
            result3.append('{'+i)
            count +=1
            
    del result3[0]
    
    result4 = []
    
    for i in result3: # 합친것들을 json형태로 옮겨준다.
        b = json.loads(i)
        del b['']
        result4.append(b)
        
    result5 = {'data': result4[:100]}#한번에 어떻게 해야할지 몰라서 하나의 딕셔너리로 만들어준다.
    
    return {
    'statusCode': 200,
    'body': json.dumps(result5)
    }

print(lambda_handler(1,1))