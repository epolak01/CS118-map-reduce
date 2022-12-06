#!/usr/bin/env python3

from collections import defaultdict
import sys
view_count = defaultdict(int)

pagename = None
curr_pagename = None
dates = []
pageviews_per_date = []
count = 0


for line in sys.stdin:
    try:
        line = line.strip()
        pagename, date_pageviews = line.split()
        date, pageviews = date_pageviews.split('}')
        pageviews = int(pageviews)
    except:
        continue
    # print old result, and start accumulating new result
    if (pagename != curr_pagename):
        if (curr_pagename != None): # print old result
            # TODO add popularity
            print(curr_pagename, '\t', dates, '\t', pageviews_per_date, '\t', count)
        
        curr_pagename = pagename
        dates.clear()
        pageviews_per_date.clear()
        
        count = pageviews
        dates.append(date)
        pageviews_per_date.append(pageviews)
        
    else:
        dates.append(date)
        pageviews_per_date.append(pageviews)
        count += pageviews
if (pagename == curr_pagename): # print last count
    print(curr_pagename, '\t', dates, '\t', pageviews_per_date, '\t', count)
    
#     # print old result, and start accumulating new result
#     if (pagename_date != curr_pagename_date):
#         if (curr_pagename_date != None): # print old result
#             print(curr_pagename_date, count)
#         curr_pagename_date = pagename_date
#         count = pageviews
#     else:
#         count += pageviews
# if (pagename_date == curr_pagename_date): # print last count
#     print(curr_pagename_date, count)

