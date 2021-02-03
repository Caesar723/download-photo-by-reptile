from urllib import request
import json
from bs4 import BeautifulSoup
def get(n):
    url="https://www.duitang.com/napi/blog/list/by_tag/?tag=%E5%92%92%E6%9C%AF%E5%9B%9E%E6%88%98&include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,sender,album&limit="+str(n)+"&start=1&_=1612274425285"
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
    req=request.Request(url,headers=header)
    response=request.urlopen(req)
    #print(type(response))
    if response.getcode()==200:
        data = response.read()
        da= json.loads(data)
        information=da["data"]["object_list"]
        for i in range(0,n):

            img=information[i]["photo"]["path"]
            print(img)
            img = request.Request(img, headers=header)
            img = request.urlopen(img)
            img = img.read()


            with open("photo/"+str(i)+".jpg",mode='wb') as f:
                f.write(img)
    #for i in range(0,1):


get(30)