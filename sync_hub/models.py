from django.db import models


class ItemMapping(models.Model):

    items_ids = models.ManyToManyField(ItemMeta)
    item_hash = models.CharField(max_length=100)

    @classmethod
    def get_by_item(cls, item):
        if not item:
            return None
        try:
            return cls.object.get(apps_ids=item)
        except ItemMapping.DoesNotExist:
            return None

    @classmethod
    def get_by_hash(cls, hash):
        try:
            return cls.object.get(apps_ids=hash)
        except ItemMapping.DoesNotExist:
            return None

    def save(self, *args, **kwargs):
        super(ItemMapping, self).save(*args, **kwargs)


class ItemMeta(models.Model):
    app_name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)

    @classmethod
    def get_item(cls, app_name, id):
        try:
            cls.objects.get(app_name, id)
        except ItemMeta.DoesNotExist:
            return None
