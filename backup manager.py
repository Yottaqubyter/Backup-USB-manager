from os import system, path
from time import sleep
import console as term
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
				bnameCheck=('"'  not in bname and
						'\\' not in bname and
						'\n' not in bname and
						'/'  not in bname and
						':'  not in bname and
						'*'  not in bname and
						'>'  not in bname and
						'<'  not in bname and
						'|'  not in bname and
						'?'  not in bname and
						len( bname ) != 0 )
				file.close()
				if USB not in backed and bnameCheck:
					backed += USB
					print('SAVING...',end='')
					sleep(0.1)
					cmd('rmdir /S /Q "%HOMEDRIVE%%HOMEPATH%/USB-backup/'+bname+'" >> %HOMEDRIVE%%HOMEPATH%/USB-backup/log.txt')
					cmd('xcopy "'+USB+':/" "%HOMEDRIVE%%HOMEPATH%/USB-backup/'+bname+'" /S /E /I /EXCLUDE:'+USB+':\\.USBignore >> %HOMEDRIVE%%HOMEPATH%/USB-backup/log.txt')
				elif not bnameCheck:
					print('\x1b[101;1m INVALID \x1b[0m',end='')
				else:
					print('\x1b[92;1mBACKED UP\x1b[0m',end='')
					# cmd("start copyscript.bat "+USB+" "+bname)
			except OSError:
				bname=""
				if USB in backed:
					backed.remove(USB)
					print('EXTRACTED',end='')
				else:
					print('NOT FOUND',end='')
			finally:
				print(']'+'\t'+('Name: ')*(len(bname)>0)+bname.replace('\n','<NEWLINE>'))
		sleep(5)
	except KeyboardInterrupt:
		cmd("pause")
		exit()
