import sys, os
from cx_Freeze import setup,Executable

includefiles = []
includes = []
excludes = ['Tkinter']
packages = []

base=None
if sys.platform=="win32":
    base="Win32GUI"
else:
    base="Win64GUI"
    
setup(
    name = 'Telefonbuch Editor 2.0',
    version = '2.0',
    description = 'Telefonbuch Editor mit cx_Freeze',
    author = 'S1l3nz',
    author_email = 's1l3nzcodes@googlemail.com.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('TelefoneditorQT.py', base=base)]
)
