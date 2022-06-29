import boto3
import time
import json

with open('new.json','r') as f:
    json_data=json.load(f)


# key, secret, region_name 은 여러분의 환경에 맞는걸 넣어야 합니다.
client = boto3.client('kinesis')

def put_records(records):

    kinesis_records = []

    for i in records:
        kinesis_records.append(
        {
                    'Data': json.dumps(i).encode('utf-8'),
                    # 'ExplicitHashKey': 'string',
                    'PartitionKey': 'string_for_partition'
        }
        )
    # Data 에는 바이너리 형식으로, ExplicitHashKey은 optional입니다. PartitionKey 를 기준으로 hash값을 얻고 이 값을 가지고
    # 실제 들어갈 shard 번호가 결정됩니다. 같은 PartitionKey를 넣으면 항상 같은 shard에만 들어갑니다.
    # 만약 round robin 방식으로 여러 shard에 골고루 넣고 싶으면 random string을 넣으세요.

    response = client.put_records(
        Records=kinesis_records,
        StreamName='test'
    )

    return response


def main():
    count = 0
    k_record = []
    
    for i in json_data:
        if count == 49:
            print('start to send')
            response = put_records(k_record)
            print('response: {}'.format(response))
            count = 0
            time.sleep(10)
            k_record =[]
        else:
            count+=1
            k_record.append(i)


        

if __name__ == "__main__":
    # execute only if run as a script
    main()
