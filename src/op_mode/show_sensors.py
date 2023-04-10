#!/usr/bin/env python3

import re
import sys
from ngnos.util import popen
from ngnos.util import DEVNULL
output,retcode = popen("sensors --no-adapter",  stderr=DEVNULL)
if retcode == 0:
    print (output)
    sys.exit(0)
else:
    output,retcode = popen("sensors-detect --auto",stderr=DEVNULL)
    match = re.search(r'#----cut here----(.*)#----cut here----',output, re.DOTALL)
    if match:
        for module in match.group(0).split('\n'):
            if not module.startswith("#"):
                popen("modprobe {}".format(module.strip()))
                output,retcode = popen("sensors --no-adapter",  stderr=DEVNULL)
                if retcode == 0:
                    print (output)
                    sys.exit(0)


print ("No sensors found")
sys.exit(1)


