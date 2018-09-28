import time
from datetime import datetime as dt

hosts_temp = r"/Users/nitinparasa/Desktop/Python_Udemy/app3/hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
websites_lists = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        print("Working Hours...Fuck Off!!")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in websites_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_lists):
                    file.write(line)
            file.truncate()
        print("Relax... Go watch something useful!!")

    time.sleep(10)