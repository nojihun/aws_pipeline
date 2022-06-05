import boto3 

#이전에 aws configure를 통해서 s3와 연결해 두어야함
#bash에 aws configure를 입력후 밑에에 미리 받은 accesskey를 입력해야함
# AWS Access Key ID : 
#AWS Secret Access Key : 
#Default region name :  
#Default output format :
#입력

s3 = boto3.client('s3') 

response = s3.list_buckets()
#s3.download_file('de-project-test','game.txt', 'test5.txt' )#'버켓이름','버켓하위 경로를 포함한 s3속 파일이름',"로컬에 저장할때 파일이름")


resp = s3.select_object_content( Bucket='de-project-test', # Put your own bucket name here. 
Key='data.csv.gz', # Put your own key name here. 데이터 명
Expression="SELECT * FROM s3object s", # sql 표현식. 컬럼명 표현할때 \"컬럼명\" 이런식으로 표현해야 됨
ExpressionType='SQL', 
InputSerialization= {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'GZIP'}, OutputSerialization={'CSV': {}}, )

for event in resp['Payload']: 
    if 'Records' in event: 
        print(event['Records']['Payload'].decode('utf-8')) 

