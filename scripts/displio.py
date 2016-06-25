import os, sys
from datetime import datetime
from datetime import timedelta
from collections import namedtuple

#######################################
#
# Content for my displio
#
#######################################

_ntuple_diskusage = namedtuple('usage', 'total used free')

def displiocontent():
    time = datetime.now().strftime("%a %d/%m/%y - %H:%M")

    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
        formated_uptime = uptime_string.split('.')[0]

    raw_average = os.getloadavg()
    load_average = raw_average[0]

    return "--- FOOKER ---\nTime:\n{}\n\nUptime:\n{}\n\nLoad:{}\n\nFree Space: {}GB".format(time,formated_uptime,load_average,disk_usage())


def disk_usage():
    """Return disk usage statistics about the given path.

    Returned valus is a named tuple with attributes 'total', 'used' and
    'free', which are the amount of total, used and free space, in bytes.
    """
    st = os.statvfs("/home")
    free = st.f_bavail * st.f_frsize
    return free / 1024 / 1024 / 1024
