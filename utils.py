from .sync_hub.models import ItemMapping, ItemMeta
from .sync_hub import Item


class TodoistAdapter(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, data, *args, **kwargs):
        item = ItemMeta.get_item(app_name=self.app.name, id=data['id'])
        if not Item:
            item = ItemMeta.objects.create(app_name=self.app.name, id=data['id'])
            map = ItemMapping()
            map.items_ids.add(item)
            
        map = ItemMapping.get_by_item_id(app_name=app.name, data['id'])

        return Item()
