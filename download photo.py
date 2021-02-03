from urllib import request
import json

def get(n):

    yu = n % 98
    zhen = int(n / 98)
    if 0==0:
        for ii in range(0,zhen+1):
            start=ii*100
            url = "https://www.duitang.com/napi/blog/list/by_tag/?tag=%E5%92%92%E6%9C%AF%E5%9B%9E%E6%88%98&include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,sender,album&limit=" + str(
                100) + "&start=" + str(start) + "&_=1612274425285"
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
            req = request.Request(url, headers=header)
            response = request.urlopen(req)
            if response.getcode() == 200:
                data = response.read()
                da = json.loads(data)
                information = da["data"]["object_list"]
                if ii!=zhen :
                    for i in range(0, 98):
                        img = information[i]["photo"]["path"]

                        img = request.Request(img, headers=header)
                        img = request.urlopen(img)
                        img = img.read()
                        with open("photo/"+str(ii)+"-"+str(i)+".jpg",mode='wb') as f:
                            f.write(img)
                else:
                    for i in range(0, yu):
                        img = information[i]["photo"]["path"]
                        print(img)
                        img = request.Request(img, headers=header)
                        img = request.urlopen(img)
                        img = img.read()
                        with open("photo/"+str(ii)+"-"+str(i)+".jpg",mode='wb') as f:
                            f.write(img)




get(100)
