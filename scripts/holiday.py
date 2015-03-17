#!/usr/bin/python

class holiday:
    def GET(self,uri):
      request = uri.split('/')
      print request
      if request == ['']:
        web.badrequest()
        return "Incorrect request"
      try:
        format = request[1]
      except:
        format = None
      if request[0] == "now":
        return "pouet"
