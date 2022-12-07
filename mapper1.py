#!/usr/bin/env python3

import re, sys, urllib.parse, os

for line in sys.stdin:
    try:
        line = line.strip()
        projectcode, pagename, pageviews, bytes = line.split()
    except:
        continue
    
    # filename = os.getenv('mapreduce_map_input_file')
    
    # name, date, hours = filename.split('-')
    date = "20160601" # temporary, get date from filename 
    pagename_decoded = urllib.parse.unquote_plus(pagename)  ## for lines that have this part only
    
    if re.search(r'^en', projectcode): # TODO: is it just beginning with en or just en??????
        if not re.match(r'^(Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk)', pagename_decoded):  ## ^ = begins with
            if not re.search(r'^[[:upper:]]', pagename_decoded):
                if not re.search(r'(.jpg|.gif|.png|.ico|.txt)$', pagename_decoded, re.I):  ## re.I = case-insensitive
                    if not re.search(r'(404_error|Main_Page|Hypertext_Transfer_Protocol|Favicon.ico|Search)', pagename_decoded):
                        print(pagename_decoded + '}' + date, '\t', pageviews)



