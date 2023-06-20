import requests
import os
# import ssl
# import urllib2
 
# ssl._create_default_https_context = ssl._create_unverified_context

# https://f100.coget.cn/bbc/1.mp4
base_url = "https://f100.coget.cn/bbc/"  # 替换为实际的文件下载地址
# https://f100.coget.cn/bbcVideo/V3.mp4
base_url1 = "https://f100.coget.cn/bbcVideo/"
for i in range(1, 48):
    filename =  str(i) + ".mp4"
    url = base_url + filename
    filename1 = "V" + str(i) + ".mp4"
    url1 = base_url1 + filename1

    try:
        response = requests.get(url,verify=False)
        response.raise_for_status()
        filepath = os.path.join( os.getcwd()+"\\mp3\\short", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)

        filepath1 = os.path.join( os.getcwd()+"\\mp3\\long", filename)
        response = requests.get(url1,verify=False)
        response.raise_for_status()
        with open(filepath1, "wb") as f:
            f.write(response.content)
        print(f"{filename} downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")