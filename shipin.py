import requests
import re




mp4list_path = '/Users/mms/Desktop/mp4.txt'

for line in open(mp4list_path):
    url = re.sub(r'[\"\'\,\n]',"",line)
    print('downloading: ',url)
    file_name = url.split('/')[-1]
    headers = {'User-Agent': '',
    'Referer':url}
    video = requests.get(url,headers = headers,stream = True,verify=False)


    #print(video)
    with open('/Volumes/Samsung_T5/video/'+file_name, 'wb') as f:
        for chunk in video.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    f.close
