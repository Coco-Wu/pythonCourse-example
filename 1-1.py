import  requests
url = 'http://www.sinica.edu.tw/'
res = requests.get(url)
print(res.text)
print("coco")