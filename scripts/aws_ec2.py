#!/usr/bin/python

###########################
#
# Extraire les CPU et RAM des instances AWS contenu dans la page http://aws.amazon.com/ec2/instance-types/
#
###########################

from bs4 import BeautifulSoup
import urllib2
from lxml import etree


def ec2details(ec2_type):
    pageContent = urllib2.urlopen('http://aws.amazon.com/ec2/instance-types/').read()
    soup = BeautifulSoup(pageContent)
    soup = soup.find_all("table")[-1]

    rows = soup.find_all('tr')
    for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	if cols[0] == ec2_type :
		return cols[0], cols[1], cols[2]
