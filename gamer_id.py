from b64uuid import B64UUID 
import uuid
import json 

with open("test.json", "r") as f:
    raw = json.load(f)

# uuid encoding 방법 1 b64uuid
def gamer_enc(raw):
    for d in raw: 
        d['gamer_id'] = str(B64UUID(d['gamer_id']))
    return raw

def gamer_dec(raw):
    for r in raw:
        r['gamer_id'] = str(B64UUID(r['gamer_id']).uuid)
    return raw
    
"""
with open("test_dec.json", "w") as f:
    json.dump(raw, f)
"""
