from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


def getvid(url):
    # noinspection PyBroadException
    try:
        metadata = extractMetadata(createParser(url))
        duration = str(metadata.get("duration")).split(".")[0]
        width = str(metadata.get("width"))
        height = str(metadata.get("height"))
        return duration, width, height
    except Exception:
        return
        pass


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
