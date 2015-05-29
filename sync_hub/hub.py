import datetime

from .models import ItemMapping


SWITCH_TIME_INTERVAL = 60  # 1 minute


class SyncHub(object):

    def __init__(self, *apps):
        self.switcher = Switcher([Collector(), Collector()])
        self.apps = apps

    def add_items(self, app, items):
        for item in items:
            self.switcher.push(app.adapter(item), app, self.send_for_add_item_to_apps)

    def update_items(self):
        pass

    def delete_items(self):
        pass

    def send_for_add_item_to_apps(self, item, from_app):
        for app in self.apps:
            if app.name == from_app.name:
                continue
            app.add_item(item)


class Collector(object):

    def __init__(self):
        self.last_update = datetime.datetime.now()
        self.data = []

    def push(self, item, app, action):
        self.data.append({
            'item': item,
            'app': app,
            'action': action,
            'time': datetime.datetime.now()
        })
        self.__change_last_update()

    def execute_all(self):
        self.__delete_enuque()

        for value in self.data:
            value['action'](value['item'], value['app'])

        self.__init__()

    def __change_last_update(self):
        self.last_update = datetime.datetime.now()

    def __delete_enuque(self):
        hash_map = dict()
        for value in self.data:
            hash = value['item'].get_hash
            if hash in hash_map:
                if hash_map[hash]['time'] < value['time']:
                    hash_map[hash] = value
            else:
                hash_map[hash] = value

        for hash in hash_map:
            if ItemMapping.get_by_hash(hash):
                del hash_map[hash]

        self.data = hash_map.values()


class Switcher(object):

    def __init__(self, collectors):
        self.collectors = collectors
        if not collectors:
            raise RuntimeError('Collectors not found')

        self.current = 0

    def push(self, item, app, action):
        current_collector = self.collectors[self.current]

        if (current_collector.last_update - datetime.datetime.now).total_seconds() > SWITCH_TIME_INTERVAL:
            current_collector.execute_all()
            self.current = (self.current + 1) % len(self.collectors)

        current_collector.push(item, app, action)
