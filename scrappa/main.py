# import urllib.request, urllib.parse, urllib.error, requests

# fhand=urllib.request.urlopen('')
# for line in fhand:
#     print(line.decode())

# from ast import Continue
import urllib.request, urllib.error, urllib.parse
from urllib.request import Request, urlopen
import ssl
import re
# import webbrowser
from bs4 import BeautifulSoup
import json
from datetime import datetime
# from matplotlib.pyplot import title
# from cv2 import textureFlattening

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
# url='https://fboxtv.com/watch-tv/watch-family-guy-fbox-39549.4841206'
# html=urllib.request.urlopen(url,context=ctx).read()
url='https://en.wikipedia.org/wiki/List_of_Young_Sheldon_episodes#Season_5_(2021%E2%80%9322)'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup=BeautifulSoup(webpage,'html.parser')

#######
# fhand=open('/home/saimon_ghimire010/sAIMON/toBeAdded/Work/1Python/win10/scrappa/datum.json','r+')
now=datetime.now()
dataFile=open('/home/saimon_ghimire010/sAIMON/toBeAdded/Work/1Python/win10/scrappa/datum.json','r+')
jObj=json.loads(dataFile.read())

#########################################################################################
def dumpUpdate(id,value):
    jObj[id] = value # <--- replace value
    dataFile.seek(0)        # <--- should reset file position to the beginning.
    json.dump(jObj, dataFile, indent=4)
    dataFile.truncate()
    
def printStuff():
    
    #print block............................
    print('''
          Title: {}\n
          Date: {}\n
          {}\n
          Last viewed: {}\n
          Remarks: {}
          '''.format(title,date,'*'*20,jObj['lastViewed'],jObj['remarks']))

    rem=input('\nAdd rems. or press enter to skip: ')
    if rem!="":
        dumpUpdate('remarks',rem)
      #  membs['remarks']=rem
    dumpUpdate('lastViewed',now.strftime("%d %B, %Y (%A)"))

# def updates():
#      ##for membs in jObj['status']:
#         membs['ePCount']+=1

###################################################################################################
# local html file 
# with open("/home/saimon_ghimire010/sAIMON/toBeAdded/Work/1Python/win10/scrappa/output.html","w+") as newfile:
#     for itr in soup:
#          newfile.write(str(itr))
#     num_occ = str(soup).count("T12.17216")

ePMark='pcT12.172'
ePNum=(jObj['ePCount'])
tag='td[id="'+ePMark+str(ePNum+1)+'"]'
tagFound=0
# classes--> indivudual tr chunks
# classes.select tag-->search if tag in class chunk iteration
for classes in (soup.select('tr[class="vevent"]')):
    if (classes.select(tag) != []):
        tagFound=1
        print("\n\t\tNew!!!!!!!!\n")
        rem='Prev episode  {} \n{}'.format(jObj['prevep'],jObj['remarks'])
        dumpUpdate('remarks',rem)
        title=(classes.find(class_="summary").get_text())
        dumpUpdate('prevep',title)
        # using regexes
        # ePInfo=(classes.select('td[class="summary"]')) #title line
        # striPart=re.search('.+">',str(ePInfo)) #lstrippables
        # title=str(ePInfo).lstrip(striPart.group()).rstrip('"</td>]') #lstrip lstrippables ++ rstrip leftovers
        # print(title)
        date=(classes.find(class_="bday dtstart published updated").get_text())
        printStuff()
        
        dumpUpdate('ePCount',jObj['ePCount']+1)
    else:
        #if no match
        continue
        

if tagFound==0:
        #if no new episode
        tag='td[id="'+ePMark+str(ePNum-1)+'"]' #-1 episode tag
        title=(classes.find(class_="summary").get_text())
        date=(classes.find(class_="bday dtstart published updated").get_text())

        print('\n\t\tNothing new there :::::::::\n')
        printStuff()

# print (soup.find_all("T12.17216"))
#var1=soup.find_all('table')   









