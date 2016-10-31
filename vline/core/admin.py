from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm, TextInput, Textarea, Select, \
                         SelectMultiple
from django.http import HttpResponseRedirect

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
            'entities':    SelectMultiple(attrs={'size':'10'}),
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
    list_display = ('name', 'type', 'entity_list', 'start_time', 'end_time', 'story_list')
    list_filter = ('type', 'entities', 'stories')
    list_per_page = 200
    list_max_show_all = 500

    def entity_list(self, obj):
        entity_names = [entity.name for entity in obj.entities.all()]
        return ', '.join(entity_names)

    def story_list(self, obj):
        story_names = [story.name for story in obj.stories.all()]
        return ', '.join(story_names)

    def response_add(self, request, obj, post_url_continue=None):
        """Display events of the first related entity"""
        return HttpResponseRedirect('/admin/core/event/?q=&entities__id__exact=' + str(obj.entities.all()[0].id))

    def response_change(self, request, obj):
        """Display events of the first related entity"""
        return HttpResponseRedirect('/admin/core/event/?q=&entities__id__exact=' + str(obj.entities.all()[0].id))

admin.site.register(Event, EventAdmin)


admin.site.register(EventRelation)


admin.site.register(Story)