#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        pagename_date, pageviews = line.split()
        pagename, date = pagename_date.split('}')
    except:
        continue
    
    print(f"{pagename}\t{date}}}{pageviews}")