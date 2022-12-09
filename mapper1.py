#!/usr/bin/env python3

import re, sys, urllib.parse, os

def main(argv):
    for line in sys.stdin:
        try:
            line = line.strip()
            projectcode, pagename, pageviews, bytes = line.split()
        except:
            continue
        
        filename = os.path.split(os.getenv('map_input_file'))[1] # get filename
        name, date, hour = filename.split('-')
        
        pagename_decoded = urllib.parse.unquote_plus(pagename)  ## for lines that have this part only
        
        if re.search(r'^en$', projectcode): # TODO: is it just beginning with en or just en??????
            if not re.search(r'^(Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk)', pagename_decoded):  ## ^ = begins with
                if not re.search(r'^\"*[\[:upper:\]]', pagename_decoded):
                    if not re.search(r'(.jpg|.gif|.png|.ico|.txt)\"*$', pagename_decoded, re.I):  ## re.I = case-insensitive
                        if not re.search(r'(404_error|Main_Page|Hypertext_Transfer_Protocol|Favicon.ico|Search)', pagename_decoded):
                            print(f"{pagename_decoded}}}{date}\t{pageviews}")

        """ we now take into account url decoding has quotations at the beginning and end; \"* means optional quotation mark
        if re.search(r'^en', projectcode): # TODO: is it just beginning with en or just en??????
            if not re.match(r'^(Media|Special|Talk|User|User_talk|Project|Project_talk|File|File_talk|MediaWiki_talk|Template|Template_talk|Help|Help_talk|Category|Category_talk|Portal|Wikipedia|Wikipedia_talk)', pagename_decoded):  ## ^ = begins with
                if not re.search(r'^[\[:upper:\]]', pagename_decoded):
                    if not re.search(r'(.jpg|.gif|.png|.ico|.txt)$', pagename_decoded, re.I):  ## re.I = case-insensitive
                        if not re.search(r'(404_error|Main_Page|Hypertext_Transfer_Protocol|Favicon.ico|Search)', pagename_decoded):
                            print(f"{pagename_decoded}}}{date}\t{pageviews}")
        """


if __name__ == "__main__":
    main(sys.argv)



