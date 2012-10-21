from django.db import models
from cms.models import CMSPlugin, Page
import datetime
from django.utils.translation import ugettext as _


class Event(models.Model):

    title = models.CharField(max_length=200)
    event_date = models.DateField('date of event', default=datetime.date.today())
    description = models.TextField(blank=True, default="")
    address = models.TextField(blank=True, default="")
    url = models.URLField(blank=True, default="")

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('event_date', )

    def __unicode__(self):
        return self.title

    def is_today(self):
        return self.event_start == datetime.date.today()

class EventPlugin(CMSPlugin):
    event = models.ForeignKey(Event)

    def __unicode__(self):
      return self.event.title

class EventListPlugin(CMSPlugin):

    limit = models.IntegerField(default=8)

    def __unicode__(self):
      return "%d" % self.limit
