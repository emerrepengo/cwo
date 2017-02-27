"""Cosas para tratar archivos"""

import os
import datetime
import argparse
#Funciones
def crea_path(path):
    """Crear directorio si no existe"""
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        pass

def mueve_file(file, dest_dir):
    """Mueve o renombra archivo"""
    basename = os.path.basename(file)
    f_name, f_ext = os.path.splitext(basename)
    dst_file = os.path.join(dest_dir, basename)
    count = 0
    while os.path.exists(dst_file):
        count += 1
        dst_file = os.path.join(dest_dir, '%s-%d%s' % (f_name, count, f_ext))
    os.rename(file, dst_file)
    print('Moviendo %s a %s' % (file, dst_file))

def tool_jerarquiza(directorio):
    """Crea una jerarquía de directorios en base a la fecha de modificación de los archivos"""
    for file in os.listdir(directorio):
        file = os.path.join(directorio, file)
        if os.path.isfile(file):
            try:
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file))
            except OSError:
                mtime = -2211753600
            mtime_format = mtime.strftime('%Y%m%d')
            mtime_dir = os.path.join(directorio, mtime_format)
            crea_path(mtime_dir)
            mueve_file(file, mtime_dir)
        else:
            pass

#Variables
_PARSER = argparse.ArgumentParser(description='Jerarquiza en directorios.')
_PARSER.add_argument('--ruta', metavar='RUTA', type=str, help="Directorio a jerarquizar")
_ARGS = _PARSER.parse_args()

if _ARGS.ruta:
    _DIRECTORIO = str(_ARGS.ruta)
else:
    print('Introduzca directorio. Ej. C:\\temp\\aaa o /tmp/aaa')
    _DIRECTORIO = str(input())
if os.path.isdir(_DIRECTORIO):
    tool_jerarquiza(_DIRECTORIO)
else:
    print(_DIRECTORIO + 'no es un directorio.')
