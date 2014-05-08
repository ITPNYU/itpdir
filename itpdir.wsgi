import sys

activate_this = '/var/www/dev/itpdir/venv/itpdir-v1/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
sys.path.insert(0, '/var/www/dev/itpdir/itpdir')

from itpdir import app as application
