#!/usr/bin/env python3

import sys

def main(argv):
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
                print(f"{curr_pagename_date}\t{count}")
            curr_pagename_date = pagename_date
            count = pageviews
        else:
            count += pageviews
    if (pagename_date == curr_pagename_date): # print last count
        print(f"{curr_pagename_date}\t{count}")
        pagename_date = None
        curr_pagename_date = None
        count = 0

if __name__ == "__main__":
    main(sys.argv)