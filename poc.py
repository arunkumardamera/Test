from ftplib import FTP
import tarfile
import os, sys, os.path
ftp = FTP('ftp.pfainc.com')                              # connect to host, default port
ftp.login('CoreLogic','#C0r3106!c@m@d0r!')               # user anonymous, passwd anonymous@
ftp.retrlines('LIST')
filenames = ftp.nlst()                                   # get filenames within the directory
filematch ='*public010319.tar'
path = 'C:/CA-Latestfile AMador'
for filename in ftp.nlst(filematch):
    target_file_name = os.path.join(path,os.path.basename(filename))
    with open(target_file_name,'wb') as fhandle:
        ftp.retrbinary('RETR %s' %filename, fhandle.write)
        print("Files Downleded")
tar = tarfile.open('C:/CA-Latestfile AMador/public010319.tar')
tar.extractall(path='C:\CA-Latestfile AMador')
print("Extract All Sucsessfully")
tar.close()
