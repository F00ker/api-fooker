import os, sys
from datetime import datetime
from datetime import timedelta

#######################################
#
# Content for my displio
#
#######################################

def displiocontent():
    time = datetime.now().strftime("%a %d/%m/%y - %H:%M")

    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
        formated_uptime = uptime_string.split('.')[0]

    raw_average = os.getloadavg()
    load_average = raw_average[0]

    return "--- FOOKER ---\nTime:\n{}\n\nUptime:\n{}\n\nLoad:{}".format(time,formated_uptime,load_average)
