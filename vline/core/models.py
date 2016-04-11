from django.db import models


class EntityType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Entity(models.Model):
    type = models.ForeignKey('EntityType')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Entities"


class EventType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    type        = models.ForeignKey('EventType')
    name        = models.CharField(max_length=200)
    start_time  = models.DateTimeField('Start')
    end_time    = models.DateTimeField('End')
    location    = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cause       = models.TextField(blank=True, null=True)
    effect      = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class EventRelation(models.Model):
    from_event  = models.ForeignKey('Event', related_name='from_event')
    to_event    = models.ForeignKey('Event', related_name='to_event')
    description = models.TextField()


class EntityEvent(models.Model):
    entity      = models.ForeignKey('Entity')
    event       = models.ForeignKey('Event')
    description = models.TextField(blank=True, null=True)
    cause       = models.TextField(blank=True, null=True)
    effect      = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.entity.name + ' - ' + self.event.name


class Story(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stories"


class StoryEvent(models.Model):
    story = models.ForeignKey('Story')
    event = models.ForeignKey('Event')

    def __str__(self):
        return self.story.name + ' - ' + self.event.name