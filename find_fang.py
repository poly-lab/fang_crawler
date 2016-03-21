
import requests
from bs4 import BeautifulSoup
__author__ = 'admin'
urllist=['http://esf.nanjing.fang.com/house/g23-j2134-k2138-h31-j3100-l3010-kw%cb%ae%d4%c2%c7%d8%bb%b4/']




def get_info():
    r=requests.Session()
    s=r.get(urllist[0])
    a=open("soufang.html",'w')
    m=s.text.encode('gb2312', 'ignore')
    a.write(m)
    a.close()
    soup=BeautifulSoup(m,"html.parser")
    contens=soup.find_all(class_="list rel")
    print len(contens)
    print contens
    '''for price in contens:
        print price.get_text()
        pass
        #print price.get_text()'''
def check_db():
    pass


if __name__=="__main__":
    get_info()
    check_db()