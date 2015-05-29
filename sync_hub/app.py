

class App(object):

    def __init__(self, adapter, api):
        self.adapter = adapter(self)
        self.api = api(self)

    def add_item(self, *args, **kwargs):
        self.api.add_item(*args, **kwargs)
