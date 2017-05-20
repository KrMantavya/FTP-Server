import ftplib
import os

host = '0.0.0.0'
port = 8080

ftp = ftplib.FTP()
ftp.connect(host, port)
user=raw_input("ENTER USERNAME")
passw=raw_input("ENTER PASSWORD")
ftp.login(user, passw)
ftp.retrlines('LIST')
os.chdir("/home/mantavya294/projects/FTPServer/ftpclientDirectory")
choice=raw_input("UPLOAD or DOWNLOAD")
if (choice=="upload"):
	test=raw_input("Enter filename")
	f = open(test, "rb")
	ftp.storbinary('STOR '+ test, f)
	ftp.retrlines('LIST')
if (choice=="download"):
	test=raw_input("Enter filename")
	f = open(test,"wb")
	ftp.retrbinary('RETR %s' % test,f.write)

ftp.quit()
