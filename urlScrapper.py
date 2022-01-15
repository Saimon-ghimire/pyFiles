import urllib.request, urllib.error, urllib.parse
import ssl
import webbrowser
from bs4 import BeautifulSoup

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url='https://en.wikipedia.org/wiki/List_of_representations_of_e#As_an_infinite_product'
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('img')
for tag in tags:
    otag=(tag.get('src',None))
    webbrowser.open(otag)