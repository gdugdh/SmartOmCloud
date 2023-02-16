from django.contrib import admin

from .models import Home, DevicePLC, DataPLC, DeviceType, DeviceModel


admin.site.register(Home)
admin.site.register(DeviceType)
admin.site.register(DeviceModel)
admin.site.register(DevicePLC)
admin.site.register(DataPLC)
