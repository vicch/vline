from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm, TextInput, Textarea, Select

from .models import EntityType, Entity, EventType, Event, EventRelation, \
                    EntityEvent, Story, StoryEvent

from suit.widgets import SuitSplitDateTimeWidget, AutosizedTextarea


admin.site.register(EntityType)
admin.site.register(Entity)
admin.site.register(EventType)


class EventForm(ModelForm):
    class Meta:
        widgets = {
            'type':        Select,
            'name':        TextInput,
            'start_time':  SuitSplitDateTimeWidget,
            'end_time':    SuitSplitDateTimeWidget,
            'location':    TextInput,
            'description': AutosizedTextarea,
            'cause':       AutosizedTextarea,
            'effect':      AutosizedTextarea,
        }

class EventAdmin(ModelAdmin):
    form = EventForm
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)


admin.site.register(EventRelation)
admin.site.register(EntityEvent)
admin.site.register(Story)
admin.site.register(StoryEvent)