#!"C:\Users\New user\Desktop\RealPython\flasktaskr-03\env\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'nose==1.3.3','console_scripts','nosetests'
__requires__ = 'nose==1.3.3'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('nose==1.3.3', 'console_scripts', 'nosetests')()
    )
