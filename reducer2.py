#!/usr/bin/env python3

import sys

def main(argv):
    pagename = None
    curr_pagename = None
    dates = []
    pageviews_per_date = []
    count = 0
    pop_trend = 0

    for line in sys.stdin:
        try:
            line = line.strip()
            pagename, date_pageviews = line.split()
            date, pageviews = date_pageviews.split('}')
            pageviews = int(pageviews)
            date = int(date)
        except:
            continue
        # print old result, and start accumulating new result
        if (pagename != curr_pagename):
            if (curr_pagename != None): # print old result            
                print(f"{curr_pagename}\t{dates}\t{pageviews_per_date}\t{count}\t{pop_trend}")
            
            # reset variables from previous key
            dates.clear()
            pageviews_per_date.clear()
            
            # set variables for next key
            curr_pagename = pagename
            dates.append(date)
            pageviews_per_date.append(pageviews)
            count = pageviews
            
            if (date % 100 > 2):
                pop_trend = pageviews
            else:
                pop_trend = -pageviews
        else:
            count += pageviews
            dates.append(date)
            pageviews_per_date.append(pageviews)
            if (date % 100 > 2):
                pop_trend += pageviews
            else:
                pop_trend -= pageviews
    if (pagename == curr_pagename): # print last count
        print(f"{curr_pagename}\t{dates}\t{pageviews_per_date}\t{count}\t{pop_trend}")
    
if __name__ == "__main__":
    main(sys.argv)
