#
#
#  This script will create the golfer database by scraping the url below from A to Z.
#  Golfers are formatted Last name, First name and stored as unicode
#
#


#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Chad Capooth on 2016-06-16.
Copyright (c) 2016 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse


def main():
	pass


if __name__ == '__main__':
	main()
	

# URL page IDs 
page_id = ['A_players.html', 'B_players.html', 'C_players.html', 'D_players.html', 'E_players.html', 'F_players.html', 'G_players.html', 'H_players.html', 'I_players.html', 'J_players.html', 'K_players.html', 'L_players.html', 'M_players.html', 'N_players.html', 'O_players.html', 'P_players.html', 'Q_players.html', 'R_players.html', 'S_players.html', 'T_players.html', 'U_players.html', 'V_players.html', 'W_players.html', 'X_players.html', 'Y_players.html', 'Z_players.html']

#Start golfer list
golfers = []

#start scraping the multiple pages by adding the page_id to the url and pulling the data
for i in page_id:
    
    url = "http://newsok.sportsdirectinc.com/golf/pga-players.aspx?page=/data/pga/players/" # change to whatever your url is
    
    page = urllib2.urlopen(url + i).read()
    soup = BeautifulSoup(page, "lxml")
    

# pull golfers name from the table and td and append it to the golfers list    
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
	#    print "Nome: %s" % (tds[0].text)
        a = tds[0].text
        golfers.append(a)

# remove any duplicate name and return the list
def remove_duplicates(golfers):
    return list(set(golfers))

# cleaning up the list
golfers = [i.replace('\n','') for i in golfers]
print golfers

# golfer count check - not needed
count = 0
for i in golfers:
    count = count + 1




