import requests
from bs4 import BeautifulSoup
import pickle

url = 'http://www.shigeku.org/xlib/xd/sgdq/index.htm'
headers = {
    'Host':'shigeku.org',
    'User-Agent' : 'Chrome/67.0.3396.87'
}
response = requests.get(url=url, headers=headers)
response.encoding ='gbk'
html = response.text
soup = BeautifulSoup(html,'lxml')

html = soup.prettify()
html_file = open('index.html','w',encoding='utf-8')
html_file.write(html)

tags = soup.find_all(name='td',attrs={'align':'left','width':'10%'})

poet_url_list = list()
poet_list = list()
for tag in tags:
    if len(str(tag))>36:
        sub_url = tag.a.attrs['href']
        url = 'http://www.shigeku.org/xlib/xd/sgdq/'+str(sub_url)
        poet_name = tag.text
        poet_url_list.append(url)
        poet_list.append(poet_name)

with open('url_list.pk', 'wb') as url_list_file:
    pickle.dump(poet_url_list, url_list_file)

with open('poet_list.pk','wb') as poet_list_file:
    pickle.dump(poet_list,u )





















