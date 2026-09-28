import os, hashlib, requests, socket

# Rangi
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def banner():
    print(f"{GREEN}")
    print("  ██████╗  █████╗ ██████╗ ██████╗ ███████╗███╗   ██╗")
    print("  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║")
    print("  ██║  ██║███████║██████╔╝██████╔╝█████╗  ██╔██╗ ██║")
    print("  ██║  ██║██╔══██║██╔══██╗██╔══██╗██╔══╝  ██║╚██╗██║")
    print("  ██████╔╝██║  ██║██║  ██║██║  ██║███████╗██║ ╚████║")
    print("  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝")
    print(f"{CYAN}              DARREN TOOLKIT v2.0 - By Muhidin{RESET}")
    print(f"{YELLOW}              Kibaha, Tanzania | Ethical Hacking{RESET}\n")

def wifi_scan():
    print(f"\n{CYAN}=== 1. WiFi SCANNER ==={RESET}")
    os.system("nmap -sn 192.168.1.0/24 | grep report")
    print(f"{GREEN}Imeisha! Vifaa hapo juu viko kwenye WiFi yako.{RESET}")

def pesa_check():
    print(f"\n{CYAN}=== 2. PASSWORD CHECKER ==={RESET}")
    pwd = input("Andika password: ")
    score = 0
    if len(pwd) >= 8: score+=1
    if any(c.isupper() for c in pwd): score+=1
    if any(c.isdigit() for c in pwd): score+=1
    if any(c in "!@#$%^&*" for c in pwd): score+=1
    print(f"Nguvu: {score}/4")
    if score==4: print(f"{GREEN}✅ KALI SANA!{RESET}")
    else: print(f"{RED}❌ Dhaifu, ongeza alama!{RESET}")

def breach_check():
    print(f"\n{CYAN}=== 3. BREACH CHECKER ==={RESET}")
    pwd = input("Andika password: ")
    sha1 = hashlib.sha1(pwd.encode()).hexdigest().upper()
    first5, rest = sha1[:5], sha1[5:]
    res = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    if rest in res.text:
        print(f"{RED}🚨 HATARI! Imevuja kwenye internet!{RESET}")
    else:
        print(f"{GREEN}✅ SALAMA! Haijavuja!{RESET}")

def port_scan():
    print(f"\n{CYAN}=== 4. PORT SCANNER (Mpya!) ==={RESET}")
    target = input("Andika IP au website (mf: scanme.nmap.org): ")
    print(f"Ina-scan {target}...")
    for port in [21,22,23,25,53,80,110,443,3306,8080]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN} [+] Port {port} - WAZI{RESET}")
        s.close()
    print(f"{GREEN}Imeisha!{RESET}")

banner()
while True:
    print(f"\n{YELLOW}==========================")
    print("  MENU KUU")
    print("=========================={RESET}")
    print("1. Scan WiFi")
    print("2. Pima Password")
    print("3. Angalia kama Imevuja")
    print("4. Port Scanner (Mpya!)")
    print("5. Toka")
    ch = input("Chagua 1-5: ")
    if ch=="1": wifi_scan()
    elif ch=="2": pesa_check()
    elif ch=="3": breach_check()
    elif ch=="4": port_scan()
    elif ch=="5": print("Bye Mkuu!"); break
    else: print("Chagua 1-5 tu!")
