import os
import winshell

startup = winshell.startup() + '/Windows Security Update.exe'
os.remove(startup)
