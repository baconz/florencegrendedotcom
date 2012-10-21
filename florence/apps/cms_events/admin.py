from django.contrib import admin
from florence.apps.cms_events.models import Event


class EventAdmin(admin.ModelAdmin): 
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None, {'fields': ['event_date']}),
        ("Other Info", {'fields': ['description', 'address', 'url']}),
    ]


admin.site.register(Event, EventAdmin)
