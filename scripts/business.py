#!/usr/bin/python
#################
#
# api-fooker business day API, tells you if today is a working day or not
# Discounts weekends and national holidays
#
#################


import datetime
import string
today = datetime.date.today()

def easterday():
	a=today.year//100
	b=today.year%100
	c=(3*(a+25))//4
	d=(3*(a+25))%4
	e=(8*(a+11))//25
	f=(5*a+b)%19
	g=(19*f+c-e)%30
	h=(f+11*g)//319
	j=(60*(5-d)+b)//4
	k=(60*(5-d)+b)%4
	m=(2*j-k-g+h)%7
	n=(g-h+m+114)//31
	p=(g-h+m+114)%31
	day=p+1
	month=n
	return [day, month]

def adddays(orig,delta):
	orig_day, orig_month = orig
	proper_orig = datetime.datetime(today.year,orig_month,orig_day)
	result = proper_orig + datetime.timedelta(days=delta)
	return [result.day,result.month]

# Return false if weekend or national holiday
def isBusinessDay():
	if (today.weekday() >= 5 ):
		return False
	else:
		if ( isholiday(today) ):
			return False
		else:
			return True


# Array of national holidays for the current year

holidays = []
holidays.append([1,1]) # Jour de l'an
holidays.append([1,5]) # Premier mai
holidays.append([8,5]) # 8 mai
holidays.append([14,7]) # fete national
holidays.append([15,8]) # 15 aout
holidays.append([1,11]) # premier novembre
holidays.append([11,11]) # onze novembre
holidays.append([25,12]) # noel
# I hate easter!
holidays.append(adddays(easterday(),1))
holidays.append(adddays(easterday(),39))
holidays.append(adddays(easterday(),50))

def isholiday(today):
	for i in xrange(0, len(holidays)):
		if (today.day == holidays[i][0] and today.month == holidays[i][1]):
			return True
	return False


