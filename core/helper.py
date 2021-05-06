import time
from datetime import datetime
from dateutil.parser import parse


def calc_secs_duration(st, nd):
    if not isinstance(st, datetime):
        st = parse(st)

    if not isinstance(nd, datetime):
        nd = parse(nd)

    st_time = time.mktime(st.timetuple())
    nd_time = time.mktime(nd.timetuple())
    return int(nd_time - st_time)
