"""Bajar archivo de FTP"""

from ftplib import FTP

servidor = 'ftp.debian.org'
directorio = 'debian'
archivo = 'README'

ftp = FTP(servidor) 
ftp.login()
ftp.cwd(directorio)
ftp.retrbinary('RETR 'archivo, open(archivo, 'wb').write)
ftp.quit