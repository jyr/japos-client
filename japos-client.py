#
# JAPOS - Just Another Pos Of Sale
# Osvaldo Jair Gaxiola Mercado - 2009
#
#

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__))+"/")

from views import login
login.main()
