#!/usr/bin/env python3

from collections import defaultdict
import sys
view_count = defaultdict(int)
for line in sys.stdin:
    try:
        line = line.strip()
        pagename_date, pageviews = line.split()
        pageviews = int(pageviews)
    except:
        continue
    view_count[pagename_date] += pageviews
    
for pagename_date, pageviews in view_count.items():
    print(pagename_date, pageviews)
