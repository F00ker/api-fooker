#!/usr/bin/python

###########################
#
# Extraire les CPU et RAM des instances RDS contenu dans la page http://aws.amazon.com/rds/details/
#
###########################

from bs4 import BeautifulSoup
import urllib2
from lxml import etree


def rdsdetails(rds_type):
    pageContent = urllib2.urlopen('http://aws.amazon.com/rds/details/').read()
    soup = BeautifulSoup(pageContent)
    soup = soup.find_all("table")[-1]

    print "table read"

    rows = soup.find_all('tr')
    for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	if cols[0] == rds_type :
		return cols[0], cols[1], cols[2]
