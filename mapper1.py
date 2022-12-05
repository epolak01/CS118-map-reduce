#!/usr/bin/env python3

import gzip, re, os, sys, urllib.parse

for line in sys.stdin:
    try:
        line = line.strip()
        projectcode, pagename, pageviews, bytes = line.split()
    except:
        continue
    
    date = "0-0-0000" # temporary, get date from filename 
    pagename_decoded = urllib.parse.unquote_plus(pagename)  ## for lines that have this part only
    
    if re.search(r'^en', projectcode):
        if not re.match(r'^(Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk)', pagename_decoded):  ## ^ = begins with
            if not re.search(r'^[[:upper:]]', pagename_decoded):
                if not re.search(r'(.jpg|.gif|.png|.ico|.txt)$', pagename_decoded, re.I):  ## re.I = case-insensitive
                    if not re.search(r'(404_error|Main_Page|Hypertext_Transfer_Protocol|Favicon.ico|Search)', pagename_decoded):
                        print('[' + pagename_decoded + ']', '\t', pageviews)
                        print(projectcode + "," + pagename_decoded + "," + pageviews + "," + bytes);
    


# import gzip, re, os, sys, urllib

# with gzip.open(filename, ‘rt’) as fi:  # rt = read text mode
#     for line in fi:
#         pagename_decoded = urllib.unquote_plus(pagename)  ## for lines that have this part only
#         # fields = line.split()
#         projectcode, pagename, pageviews, bytes = line.split()




