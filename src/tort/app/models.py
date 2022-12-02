from tortoise.models import Model
from tortoise import fields
#from enum import IntEnum
#class used_active(IntEnum):
#    y = 1
#    n = 2
#
# used = fields.IntEnumField(used_active, defaul = used_active.y)


class IpAddresses(Model):
    id = fields.IntField(pk=True)
    ip = fields.CharField(max_length = 15, unique = True)
    used =fields.BooleanField(default = False)
    comment = fields.CharField(max_length = 254)
    
    def __str__(self):
        return self.name

class Networks(Model):
    id = fields.IntField(pk=True)
    network = fields.CharField(max_length = 18, unique = True)
    active =fields.BooleanField(default = False)
    comment = fields.CharField(max_length = 254)
    
    def __str__(self):
        return self.name

