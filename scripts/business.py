#!/usr/bin/python

import datetime

def isBusinessDay():
	today = datetime.date.today()
	if (today.weekday() >= 5 ):
		return False
	else:
		print "weekday"
		if ( isholiday(today) ):
			return False
		else:
			return True
