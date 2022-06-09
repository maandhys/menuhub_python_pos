from django.contrib import admin

# Register your models here.
from menus.models import ReservaItem, Restaurant, MenuItem

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(ReservaItem)

