import requests
import re
def sizeof(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)
def fsize(url):
    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    return sizeof(total_size)