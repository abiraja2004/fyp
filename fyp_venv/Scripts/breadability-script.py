#!d:\fyp\fyp_venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'breadability==0.1.20','console_scripts','breadability'
__requires__ = 'breadability==0.1.20'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('breadability==0.1.20', 'console_scripts', 'breadability')()
    )
