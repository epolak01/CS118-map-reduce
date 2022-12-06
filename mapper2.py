#!/usr/bin/env python3

import gzip, re, os, sys, urllib.parse

for line in sys.stdin:
    try:
        line = line.strip()
        pagename_date, pageviews = line.split()
        pagename, date = pagename_date.split('}')
    except:
        continue
    
    print(pagename, '\t', date + '}' + pageviews)