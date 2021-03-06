#!/usr/bin/python

######################################
#
# Fooker API, for bits and bobs
# V0.1, 17/03/2015
#
######################################

import web
import sys
import datetime

sys.path.insert(0, 'scripts')

from Daemon import Daemon
from business import *
from store import *
from aws_ec2 import *
from aws_rds import *
from displio import *

############
# Setup
############

listenip = "0.0.0.0"
listenport = "9090"
web.config.debug = False

urls = (
  '/business/*', 'businessday',
  '/myip/*', 'myip',
  '/epoc/(.*)', 'epoc',
  '/store/(.*)', 'store',
  '/showall/*', 'showAll',
  '/ec2/(.*)', 'ec2',
  '/rds/(.*)', 'rds',
  '/displio/*', 'displio',
  '/', 'index'
)

###########
# Call the functions
##########
class index:
    def GET(self):
        raise web.seeother('http://www.google.com/ncr')

class businessday:
    def GET(self):
	return isBusinessDay()

class myip:
    def GET(self):
	return web.ctx.env.get('HTTP_X_FORWARDED_FOR', web.ctx.get('ip', ''))

class epoc:
    def GET(self,uri):
	return datetime.datetime.fromtimestamp(int(uri)).strftime('%Y-%m-%d %H:%M:%S')

class store:
    def GET(self,uri):
	return storeThis(uri)

class showAll:
    def GET(self):
	return showStored()

class ec2:
    def GET(self,uri):
	print uri
	return ec2details(uri)

class rds:
    def GET(self,uri):
	print uri
	return rdsdetails(uri)

class displio:
    def GET(self):
	return displiocontent()

app = web.application(urls,globals())

###########
# Start up!
###########

class MyDaemon(Daemon):
	def run(self):
		app.run()

if __name__ == "__main__":
	service = MyDaemon('/tmp/apifooker.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			sys.argv[1] = listenip+':'+listenport
			service.start()
		elif 'stop' == sys.argv[1]:
			service.stop()
		elif 'restart' == sys.argv[1]:
			service.restart()
		elif 'console' == sys.argv[1]:
			sys.argv[1] = listenip+':'+listenport
			service.console()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart|console" % sys.argv[0]
		sys.exit(2)
