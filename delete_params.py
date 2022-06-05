import json 

# 저장한 data 불러오기 
with open("new.json", "r") as f:
    data = json.load(f)

def url_params(data):  
    for n in range(0, len(data)):
        url = data[n]['url']
        b = url.split('/')
        index = len(b)
        for i in range(len(b)): 
            if '-' in b[i]: 
                index = i
        b = b[:index] 
        if '?' in b[-1]: 
            index = b[-1].find('?')
            b[-1] =  b[-1][:index]
        elif '%' in b[-1]: 
            index = b[-1].find('%')
            b[-1] =  b[-1][:index]
        i ='/'.join(b)
        data[n]['url'] = i
    return data 

data = url_params(data)
print(data)
