import threading
from urllib import request
import os
import requests
import getpass



def downloaderFiles(num,name,url):
    username = getpass.getuser()
    nom=[]
    
    for i in range(num):
        nom.append(str(i))
        desktop_path = os.path.join('C:\\Users', username, 'downloads')

        dir = os.path.join(desktop_path, "TEST")
        if not os.path.exists(dir):
            os.mkdir(dir)
        file_name = os.path.join(desktop_path, "TEST", name+nom[i] + ".jpg")
        r = requests.get(url, allow_redirects=True)
        open(file_name, 'wb').write(r.content)





if __name__ =="__main__":

    much=int(input("How much photo u want to clone: "))
    for i in range (much):
        name1=input(str(f"Insert the name for the {i+1} file: "))
        url1 = input(str(f"Insert the url for the {i+1} file: "))
        time1 = int(input(f"How much times for {i+1} file: "))
        t1 = threading.Thread(target=downloaderFiles,args=(time1,name1,url1))
        t1.start()
        t1.join()











