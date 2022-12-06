#!/usr/bin/env python3
import sys

pagename_date = None
curr_pagename_date = None
count = 0

for line in sys.stdin:
    try:
        line = line.strip()
        pagename_date, pageviews = line.split()
        pageviews = int(pageviews)
    except:
        continue
    
    # print old result, and start accumulating new result
    if (pagename_date != curr_pagename_date):
        if (curr_pagename_date != None): # print old result
            print(curr_pagename_date, count)
        curr_pagename_date = pagename_date
        count = pageviews
    else:
        count += pageviews
if (pagename_date == curr_pagename_date): # print last count
    print(curr_pagename_date, count)
