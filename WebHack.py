from platform import platform
from re import findall
from time import sleep
from os import system
from requests.api import get
from json import dumps,loads
reqs = [0,82,720,232,38,5,2,107,48,39,54,7,8,7,7,6]
countries = ["","RU","US","JP","CA","NZ","UK","DE","AT","ES","TR","HK","GR","PT","SG","CO"]
try:
    config = loads(open("config.json","r").read())
    conf = config[config["lang"]]
except IOError:
    print("You haven't config.json file")
if platform().startswith("Windows"):
    clear = "cls"
else:
    clear = "clear"
def loader(text):
    i=0
    sep = str(text).lower()
    while i < len(sep):
        if(sep[i] != " "):
            do(clear)
            if(sep[i] == "." and i+1 != len(sep)):
                print(sep[:i]+"|"+sep[1+i:])
            else:
                print(sep[:i]+sep[i].upper()+sep[1+i:])
        i += 1

def setLang():
        lang = input("Enter lang(eng, ru, uz):\n").lower()
        if lang in config["langs"]:
            config["lang"] = lang
            open("config.json","w").write(dumps(config))
            conft = config[config["lang"]]
        else:
            return conf
        conf["dontChangeLang"] = True
        return conft
def do(action,time=0.1):
    sleep(float(time))
    if action.startswith("ping"):
        a = system("ping -c 2 -W 3 google.com")
    else:
        a = system(str(action))
    if a == 0:
        return True
    else:
        return False

do(clear,0.5)


if do("ping",0.5):
    do(clear,0.5)
    loader(conf["loading"])
else:
    print("You aren't connected to network")
    exit()

do(clear,1)
print(conf["version"])
do(clear,3)
print(conf["subscribe"])
do(clear,4)
def enter():
    print(conf["hack"])
    print(conf["countries"])
    print(conf["num"])
    try:
        integ = int(input())
    except ValueError:
        integ = enter()
    return integ

def log():
    num = enter()
    if num < 16 and num > 0:
            print("\n")		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                url = ("https://www.insecam.org/en/bycountry/"+countries[num]+"/?page=1")
                res = get(url, headers=headers)
                found = findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0                            
                for _ in found:
                    ans = found[count]
                    print ("\033[1;31m",ans)
                    count += 1 
                f = open('IPs.Web_Hack.txt' , 'a')
                f.write(str(found) + '\n')
                f.close()
                return ans
            except:
                print (" ") 
    else:
        do("clear",1)
        do("echo Enter valid number",1)
        do("clear",3)
        return log()
def search():
    while True:
        do("clear",2)
        try:
           IP = input(conf["search"])
        except ValueError:
            print("Error: Enter valid IP like 192.169.1.255")
            continue
        gotIPs = []
        for num in range(1,len(countries)+1):
            try:
                    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                    url = ("https://www.insecam.org/en/bycountry/"+countries[num]+"/?page=1")
                    res = get(url, headers=headers)
                    found = findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0                            
                    for _ in found:
                        ans = found[count]
                        
                        if(findall(IP,ans) != []):
                            gotIPs.insert(-1,ans)
                        count += 1
                    if(gotIPs != []):
                        print("We have got this IP's:")
                        for i in gotIPs:
                            print(i)
                    else:
                        print("We haven't this IP")
            except ValueError:
                    print ("Error") 
        break
    return True
def getAnswer():
    while True:
        do("clear",1)
        gotAns = input(conf["getAns"])
        if(gotAns == "1"):
            log()
            break
        elif(gotAns == "2"):
            search()
            break
        elif gotAns == "999":
            setLang()
            continue
        else:
            continue
    return True
if not config["dontChangeLang"]:
    conf = setLang()
getAnswer()