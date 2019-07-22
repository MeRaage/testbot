import time, threading
import requests
from bs4 import BeautifulSoup
import time, threading
import BotPy as BP


FileFirstList = "FirstList.txt"
ListFirstInfo = list()
ListFirstTitle = list()
ListTitle=list()
AnimeTitle=''

ListInfo=list()
AnimeInfo=''

ListHrefs=list()
AnimeHrefs=''


listname=list()
listinfo = list()
'''

        try :
            page = requests.get('https://yummyanime.club/anime-updates')
            #with open('E:/PythonLessons/Telegram bot/site.html', 'rb') as html:
            soup = BeautifulSoup(page.text,features="html.parser")
            div = soup.find("ul",class_="update-list")
            AnimeInfo = div.find_all("span",class_="update-info")
            print(len(AnimeInfo))
            for item in AnimeInfo:
                ListFirstInfo.append(item.getText())
            AnimeTitle = div.find_all("span",class_="update-title")
            for item in AnimeTitle:
                ListFirstTitle.append(item.getText())
        except Exception as e:
            print("Error",e)
'''
'''
updatelist = div.find("ul",class_="update-list")
li = div.find_all("li")
for item in li:
    span = item.find("span",class_="update-list-block")
    name = span.find("span",class_="update-title")
    info = span.find("span",class_="update-info")
    listname.append(name)
    listinfo.append(info)
    '''


def FirstRun():
    ReadFirstList()
    if len(ListFirstInfo) == 12:
        pass
    else:
        try :
            print("FirstRun")
            page = requests.get('https://yummyanime.club')
            #with open('E:/PythonLessons/Telegram bot/site.html', 'rb') as html:
            soup = BeautifulSoup(page.text,features="html.parser")
            div = soup.find("div",class_="col col-50 update-block")
            AnimeInfo = div.find_all("span",class_="update-info")
            for item in AnimeInfo:
                ListFirstInfo.append(item.getText())
            AnimeTitle = div.find_all("span",class_="update-title")
            for item in AnimeTitle:
                ListFirstTitle.append(item.getText())
            SaveFirstList(ListFirstInfo)
        except AttributeError as e:
            print("Error=",e)


def CheckSite():
    #html=open('site.html').read()
    page = requests.get('https://yummyanime.club')
#    with open('E:/PythonLessons/Telegram bot/site.html', 'rb') as html:
    soup = BeautifulSoup(page.text,features="html.parser")
    #div = soup.find("div",class_="col col-50 update-block")
    div = soup.find("ul",class_="update-list")


    FunAnimeTitle(div)# Название аниме
    FunAnimeInfo(div)  # Добавлена новая серия
    FunAnimeHrefs(div)# Ссылка на эту серию
####
def FunAnimeHrefs(div):#Получаем все ссылки на сериал
    try:
        ListHrefs.clear()
        AnimeHrefs = div.find_all("a")
        for item in AnimeHrefs:
            if 'catalog' in str(item.get('href')):
                hrefs = item.get('href')
                ListHrefs.append("https://yummyanime.club/"+hrefs)
    except Exception as e:
        print(e)
        ListHrefs.reverse()
####
def FunAnimeTitle(div):#Получаем список названия каждого сериала
    try:
        ListTitle.clear()
        AnimeTitle = div.find_all("span",class_="update-title")
        for item in AnimeTitle:
            #print(item)
            ListTitle.append(item.getText())
    except Exception as e:
        print(e)
    #ListTitle.reverse()
####
def FunAnimeInfo(div):#Получаем информацию о серии(Озвучка)
    try:
        ListInfo.clear()
        AnimeInfo = div.find_all("span",class_="update-info")
        for item in AnimeInfo:
            ListInfo.append(item.getText())
    except Exception as e:
        print(e)
    #ListInfo.reverse()
####
def CheckAnime():
    print("@start-CheckAnime")
    sendlist =list()#ListInfo.append(('Попытайтесь снова, владыка демонов! - Добавлена 3-я серия: Одноголосая озвучка AniRise'))
    '''
    print("START CHECK 0 element")
    print(ListTitle[0])
    print(ListInfo[0])
    print(ListHrefs[0])
    print(ListFirstTitle[0])
    print(ListFirstInfo[0])
    print("END CHECK 0 element")

    ListTitle[0] = "Сага о Винланде"
    ListInfo[0] = "Добавлена 1-я серия: Озвучка JAM club"
    ListHrefs[0] = "https://yummyanime.club/catalog/item/saga-o-vinlande"
    ListTitle[1] = "Сага о Винланде"
    ListInfo[1] = "Добавлена 2-я серия: Озвучка JAM club"
    ListHrefs[1] = "https://yummyanime.club/catalog/item/saga-o-vinlande"
    '''
    #for item,item2 in zip(ListFirstInfo,ListInfo):
    #    print(item)
    #    print(item2)


    if ListFirstInfo !=ListInfo:
        #ListInfo.reverse()
        index = IndexsList(ListFirstInfo,ListInfo)
        print("INDEX =",index)
        while index >0:
            sendlist.append(ListInfo[index-1])
            index-=1
    print("@return-CheckAnime return:",len(sendlist))
    return(sendlist)



####
def IndexsList (list1,list2):
    print("start-IndexsList")
    count=0
    '''
    if list1[0] == list2[0]:
        print(list1[0])
        print(list2[0])
    else:
        print('No')
    '''
    for i in list2:
        if i in list1:
            pass
        else :
            count+=1
            #print("Число",i,"имеет индекс",count)
    if count >0:
        ListFirstInfo =  ListInfo
        SaveFirstList(ListFirstInfo)
        ReadFirstList()

    print("return-IndexsList")
    return count
######################
def SaveFirstList(_oldinfo):
    print("SaveFirstList")
    try:
        with open(FileFirstList,"w",encoding="utf8")as file:
            for item in _oldinfo:
                file.write(item)
                file.write('\n')

    except Exception as e :
        print(e)
###########################
def ReadFirstList():
    print("@start-ReadFirstList")
    try:
        with open(FileFirstList,"r",encoding="utf8")as file:
            line = file.readline()
            while line:
                ListFirstInfo.append(line[:-1])
                line = file.readline()
    except Exception as e :
        print("read error",e)
    print("@end-ReadFirstList")
###########################
def main():
    print("start main")
    FirstRun()
    while True:
        CheckSite()
        newlist = CheckAnime()
        if type(newlist) !=None:
            step =0
            for name,info,href in zip(ListTitle,ListInfo,ListHrefs):
                if len(newlist) > step:
                    print("Send")
                    msg = str(ListTitle[step]+'\n'+ListInfo[step]+'\n'+ListHrefs[step])
                    step+=1
                    BP.SendInfo(str(msg))
        time.sleep(300)
    '''
    ListTitle[0] = 'Маг обманщик'
    for item in ListInfo:
        print(item)
    print("/////////////////////////////////////////////////////////////////////")

    for item in newlist:
        print(item)



    while True:
        CheckSite()
        item = CheckAnime() #3
        if item != None:
            msg = ""
            count = 0
            countitem1=len(item)
            countitem2 =-1
            newlistsend=list()
            step =0
            if len(item)>10:
                print("None")
                pass

            else:
                for name,info,href in zip(ListTitle,ListInfo,ListHrefs):
                    if len(item) > step:
                        print("Send")
                        msg = str(ListTitle[step]+'\n'+ListInfo[step]+'\n'+ListHrefs[step])
                        step+=1
                        BP.SendInfo(str(msg))
            time.sleep(300)

            for i in item:
                countitem1-=1
                countitem2+=1
                if item[countitem1] ==ListFirstInfo[countitem2]:
                    pass
                else:
                    newlistsend

            if  ListFirstInfo == ListInfo:
                pass
            else:
                ListFirstInfo.clear()
                ListFirstInfo = ListInfo
                SaveFirstList(ListFirstInfo)
                print("Send")
                for name,info,href in zip(ListTitle,ListInfo,ListHrefs):
                    msg = str(ListTitle[count]+'\n'+ListInfo[count]+'\n'+ListHrefs[count])
                    count+=1
                    BP.SendInfo(str(msg))
            '''


    #for item,item2 in zip(ListFirstTitle,ListFirstInfo):
    #    print("item:",item,item2)
    #timer=0
    #while True:
    #    time.sleep(1)
    #    timer+=1
    #    if timer == 5:
    #        timer=0
    #        CheckAnime()













#if __name__ == '_main_':
main()
