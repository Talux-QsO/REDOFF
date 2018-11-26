import time
from datetime import datetime as dt

#windos c:\\windows\system32\drivers\etc
#unix \etc\host
hosts_path_windows =r"C:\Windows\System32\drivers\etc\hosts"
hosts_path_unix="/etc/hosts"
hosts_pr="hosts"

redirect  ="127.0.0.1"
website_list =[
       " www.facebook.com",
       " facebook.com",
       " www.youtube.com",
        ]

print("Bloquiador de wed\n")

from_hour=16
to_hour=24

while True:
    if from_hour<dt.now().hour<=to_hour:
        print("trabajo")
        with open(hosts_path_unix, 'r+') as file:
            conten= file.read()
            for website in website_list:
                if website in conten:
                    pass
                else:
                    file.write( redirect + "" + website + "\n")
    else:
        print("descanso")
        with open(hosts_path_unix, 'r+' ) as file:
            conten= file.readlines()
            file.seek(0)
            for line in conten:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(60)







