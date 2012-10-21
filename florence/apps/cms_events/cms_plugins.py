import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from django.utils.translation import ugettext as _

from florence.apps.cms_events.models import EventPlugin, EventListPlugin, Event

"""
CmsPluginEvent - Handles single events
"""
# class CmsPluginEvent(CMSPluginBase):
#     model = EventPlugin
#     name = _("Display single event")
#     render_template = "event_single.html"

#     def render(self, context, instance, placeholder):
#         context.update({
#             'event':instance.event,
#             'object':instance,
#             'placeholder':placeholder
#         })
#         return context

# plugin_pool.register_plugin(CmsPluginEvent)


"""
CmsPluginEventList - List of Events (e.g. to use on front-page)
"""
class CmsPluginEventList(CMSPluginBase):
    model = EventListPlugin
    name = _("Display event listing")
    render_template = "event_list.html"

    def render(self, context, instance, placeholder):
        events = Event.objects.filter(
            event_date__gte=datetime.date.today())[:instance.limit]
        context.update({
            'instance': instance,
            'events': events,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CmsPluginEventList)
