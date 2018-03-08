import requests
from lxml import etree


URL = 'http://tieba.baidu.com/mo/q-0--9D6BAD6941DE18EB4AEE76BFE8CC1466%3AFG%3D1-sz%401320_2001%2C-1-3-0--2--wapp_1509554041766_868/m?kw={}&lp=5011&lm=&pn=0'
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

# r = requests.get(url=URL.format('fate'),headers=headers)
# print(r.content.decode())

session = requests.Session()
session.trust_env = False

response = requests.get(url=URL.format('fate'), headers=headers)
temp_html = etree.HTML(response.content)
temp_html.xpath('')





with open('fate','w',encoding='utf-8') as f:
    f.write(etree.tostring(temp_html).decode())
