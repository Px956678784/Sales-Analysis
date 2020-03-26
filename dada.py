import random
import json
shopSum = 10
datas = []
for i in range(1,32):
    date = "2018-01-"+str(i).zfill(2)
    for shop in range(1,shopSum+1):
        shopName = "店"+ str(shop)
        pv = random.randint(1000,10000)
        uv = random.randint(int(pv*0.2),pv)
        cro = random.uniform(0.01,0.30)
        data = {"date":date,"shop":shopName,"pv":pv,"uv":uv,"cro":cro}
        datas.append(data)
jsonData = json.dumps(datas)
fileObject = open('shopData.json', 'w')
fileObject.write(jsonData)
fileObject.close()
