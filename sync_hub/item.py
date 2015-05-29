import json
import hashlib
import datetime

from django.utils.encoding import force_bytes, force_text


class Item(object):

    def __init__(self, map, checked=False, content='', date_string=None):
        self.map = map
        self.checked = bool(checked)
        self.content = content or ''
        self.date_string = date_string or None

    def get_hash(self):
        data = [self.map.pk, self.checked, self.content, self.date_string]
        str_obj = json.dumps(data, separators=',:', sort_keys=True,
                             default=json_default)
        return hashlib.sha256(force_bytes(str_obj)).hexdigest()


def json_default(obj):
    if isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%dT%TZ')
    raise TypeError('%r is not JSON serializable' % obj)
