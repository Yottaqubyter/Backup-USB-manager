@echo off
rmdir /S /Q "%HOMEDRIVE%%HOMEPATH%\USB-backup\program-data"
mkdir "%HOMEDRIVE%%HOMEPATH%\USB-backup\program-data\"
echo "%HOMEDRIVE%%HOMEPATH%\USB-backup\program-data\PortablePython\python-3.9.0.amd64\python.exe" "%HOMEDRIVE%%HOMEPATH%\USB-backup\program-data\backup manager.py" >> "%HOMEDRIVE%%HOMEPATH%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\backup.cmd"
copy /Y "backup manager.py" "%HOMEDRIVE%%HOMEPATH%\USB-backup\program-data\"
xcopy "PortablePython" "%HOMEDRIVE%%HOMEPATH%\USB-backup\program-data\PortablePython" /S /E /I
"%HOMEDRIVE%%HOMEPATH%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\backup.cmd"
