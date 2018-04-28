import time
from time import mktime
from datetime import datetime


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)
    t = time.localtime(ptime)
    dt = datetime.fromtimestamp(mktime(t))
    return dt #time.strftime(format, time.localtime(ptime))


def random_time(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y %I:%M %p', prop)
