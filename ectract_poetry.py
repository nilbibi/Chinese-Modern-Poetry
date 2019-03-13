import requests
import pickle
from bs4 import BeautifulSoup
import re
import Poet
import json

with open('url_list.pk', 'rb') as url_list_file:
    poet_url_list = pickle.load(url_list_file)

with open('poet_list.pk','rb') as poet_list_file:
    poet_list = pickle.load(poet_list_file )

headers = {
    'Host':'shigeku.org',
    'User-Agent' : 'Chrome/67.0.3396.87'
}

print('data prepare...')

all_data = list()

for index,url in enumerate(poet_url_list):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    html = response.text.replace('<br />', '')
    html_blocks = html.split('<hr />')
    bodies = list()
    titles = list()
    for i in range(1,len(html_blocks)-1):
        block = html_blocks[i]
        soup = BeautifulSoup(block, 'lxml')
        poem = re.sub('[！，。？、…… . , 【 】( )（）— ———— ]+', '', soup.text)
        sentences = poem.split()
        title = sentences[0]
        body = list()
        for sentence in sentences[1:]:
            if sentence != '':
                body.append(sentence)
        titles.append(title)
        bodies.append(body)
    poet = Poet.Poet(name=poet_list[index], titles=titles, bodies=bodies)
    all_data.append(poet)
    print('extract ' + str(index + 1) + ' poet')

with open('modern_poetry.pk','wb') as save_data:
    pickle.dump(all_data,save_data)











