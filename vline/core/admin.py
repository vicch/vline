from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm, TextInput, Textarea, Select, \
                         SelectMultiple

from .models import EntityType, Entity, EventType, Event, EventRelation, \
                    Story

from suit.widgets import SuitSplitDateTimeWidget, AutosizedTextarea, \
                        LinkedSelect


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
            'entities':    SelectMultiple,
            'location':    TextInput,
            'participant': AutosizedTextarea,
            'description': AutosizedTextarea,
            'cause':       AutosizedTextarea,
            'effect':      AutosizedTextarea,
            'stories':     SelectMultiple,
        }

class EventAdmin(ModelAdmin):
    form = EventForm
    search_fields = ('name',)
    list_display = ('name', 'start_time', 'end_time', 'location')

admin.site.register(Event, EventAdmin)


admin.site.register(EventRelation)


admin.site.register(Story)