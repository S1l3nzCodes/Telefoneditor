from distutils.core import setup
import py2exe, os, sys

sys.argv.append('py2exe')

ICON='E:/UKSH/Telefonedit/Telefon.ico'
setup(
    name='Telefonlisteneditor',
    version='0.01',
    author='Florian Becker',
    
    options={'py2exe':{'bundle_files':3, 'compressed':True}},
    windows=[{'script':'E:/UKSH/Telefonedit/TelefonEditor.py','icon_resources':[(1,ICON)]}],
    zipfile=None
    )

