#This Tool was developed by Kumaraguru (www.github.com/hackyguru)
#Please refrain from changing content and removing credits


# Imports
from googlesearch import search
import time
import requests
import os

# Installing dependency
os.system("apt install toilet -y")

# Functions
def checkvpn():
 c=os.system("ifconfig tun0")
 os.system("clear")
 if(c==0):
  banner()
  print("")
 else:
  banner()
  print("\033[1;31;40mYour VPN is not recommended to be used.")
  print("")
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F gay SQLiScan")
 print("    \033[1;36;40m Developed by: \033[1;32;40m Kumaraguru")
 print("    \033[1;36;40m Instagram   : \033[1;32;40m www.instagram.com/guru.317")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/hackyguru")
 print("    \033[1;36;40m Linked In   : \033[1;34;40m www.linkedin.com/in/kumaraguru7")
banner()
checkvpn()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
q=str(input("\033[1;33;40mEnter a dork: "))
no=int(input("\033[1;33;40mEnter the number of results you wish to search: "))
times=int(input("\033[1;33;40mEnter the timeout :"))
op=str(input("\033[1;33;40mDo you want to save the vulnerable sites as txt file(Y/n) :"))
if(op=="Y" or op=="y"):
 name=str(input("\033[1;33;40mEnter the name of your output txt file :"))
 print("\033[1;32;40mAll vulnerable URLs will be saved in "+name)
 time.sleep(2)
 f=open(name,"a+")
i=1
banner()
checkvpn()
for url in search(q,tld="com",num=no,stop=no,pause=2):
 if("php?" not in url):
  i=i+1
  continue   
 print("\033[1;37;40m"+str(i)+". \033[1;35;40mChecking the URL: ")
 print("\033[1;34;40m"+url)
 try:
  checkurl=url+"%27"
  r=requests.get(url,headers=headers,timeout=times)
  s=requests.get(checkurl,headers=headers,timeout=times)
  if((s.url != checkurl) or ("af.org.pk" in url)):
   print("\033[1;31;40mNot Vulnerable!\n")
   i=i+1
   continue
  if(r.text==s.text):
   print("\033[1;31;40mNot Vulnerable!\n")
  else:
   print("\033[1;32;40mVulnerable.\n")
   if(op=="Y" or op=="y"):
    f.write(url+"\n")   
 except:
  print("\033[1;31;40mThis site can't be reached now.")
  print("")
 i=i+1
try: 
 f.close()
 print("\033[1;32;40mVulnerable URLs are saved in "+name)
except:
 pass

# End