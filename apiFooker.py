#!/usr/bin/python

######################################
#
# Fooker API, for bits and bobs
# V0.1, 17/03/2015
#
######################################

import web
import sys

sys.path.insert(0, 'scripts')

from business import *

############
# Setup
############

listenip = "0.0.0.0"
listenport = "9090"
web.config.debug = False

urls = (
  '/business/*', 'businessday',
  '/myip/(.*)', 'myip',
  '/', 'index'
)

###########
# Call the functions
##########
class index:
    def GET(self):
        raise web.seeother('/static/index.html')

class businessday:
    def GET(self):
	return isBusinessDay()

class myip:
    def GET(self):
	return web.ctx.env.get('HTTP_X_FORWARDED_FOR', web.ctx.get('ip', ''))

app = web.application(urls,globals())

###########
# Start up!
###########

if __name__ == "__main__":
    sys.argv[1] = listenip+':'+listenport
    app.run()
