import os
import sys
import socket
import socketserver
import time
import datetime
import requests
import pyautogui
import getpass




class blok:
    def get_hostname():
        return socket.gethostname() 

    def get_username():
        return getpass.getuser()

    
    def get_ip():
        socket_start = socket.gethostname()
        local_ip = socket.gethostbyname(socket_start)
        print(local_ip)

        return local_ip




    def screen_shot():
        user_screenshot = pyautogui.screenshot()
        timezone = time.time()
        rtime = time.localtime(timezone)
        file_name = "{0}&{1}&{2}&{3}&{4}".format(rtime.tm_hour,rtime.tm_min,rtime.tm_mday,rtime.tm_mon,rtime.tm_year)
        h = getpass.getuser()
        os.system("mkdir {0}-screen".format(h))
        
        user_screenshot.save(r"C:\Users\{0}\Desktop\pc-controller-go\{1}-screen\{2}.png".format(h,h,file_name))




    def req(host,username,ip):
        request_api = requests.get(f"http://127.0.0.1:5000/pcdata?hostname={host}&username={username}&ip={ip}")
        print(request_api)












cl = blok()
host = blok.get_hostname()
ip = blok.get_ip()
username = blok.get_username()
blok.screen_shot()
blok.req(host,username,ip)

















