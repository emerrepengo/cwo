"""Cosas para tratar archivos"""

import os
import shutil
import datetime

def tool_jerarquiza(directorio):
    """Crea una jerarquía de directorios en base a la fecha de modificación de los archivos """
    for filename in os.listdir(directorio):
        filename = os.path.join(directorio, filename)
        if os.path.isfile(filename):
            try:
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
            except OSError:
                mtime = -2211753600
            mtime_format = mtime.strftime('%Y%m%d')
            mtime_dir = os.path.join(directorio, mtime_format)
            try:
                os.makedirs(mtime_dir)
            except OSError:
                pass
            shutil.move(filename, mtime_dir)
            print(filename)

#tool_jerarquiza('/home/mrpengo/Documentos/git/pruebas/')
