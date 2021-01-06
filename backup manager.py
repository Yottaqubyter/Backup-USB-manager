from os import system, path
from time import sleep
# Incluir el instalador en el menu de inicio
def cmd(c):
	_ = system(c)
alphabet = [chr(ord('A')+i) for i in range(26)]
backed = []
while True:
	try:
		cmd("cls")
		print("Scanning: ")
		for USB in alphabet:
			print('	'+USB+': [',end='')
			try:
				file = open(USB+":/USBack.txt")
				_ = open(USB+":/.USBignore")
				_.close()
				bname = file.read()
				file.close()
				if not USB in backed:
					if ('"'  not in bname and
						'\\' not in bname and
						'\n' not in bname and
						'/'  not in bname and
						':'  not in bname and
						'*'  not in bname and
						'>'  not in bname and
						'<'  not in bname and
						'|'  not in bname and
						'?'  not in bname and
						len( bname ) != 0 ):
						backed += USB
						print('SAVING...',end='')
						sleep(0.1)
						cmd('rmdir /S /Q "%HOMEDRIVE%%HOMEPATH%/USB-backup/'+bname+'" >> %HOMEDRIVE%%HOMEPATH%/USB-backup/log.txt')
						cmd('xcopy "'+USB+':/" "%HOMEDRIVE%%HOMEPATH%/USB-backup/'+bname+'" /S /E /I /EXCLUDE:'+USB+':\\.USBignore >> %HOMEDRIVE%%HOMEPATH%/USB-backup/log.txt')
					else:
						print('INVALID BACKUP NAME',end='')
					else:
						print('BACKED UP',end='')
						# cmd("start copyscript.bat "+USB+" "+bname)
					except OSError:
						bname=""
						if USB in backed:
							backed.remove(USB)
							print('EXTRACTED',end='')
						else:
							print('NOT FOUND',end='')
						finally:
							print(']'+'\t'+('Name: ')*(len(bname)>0)+bname)
		sleep(5)
	except KeyboardInterrupt:
		cmd("pause")
