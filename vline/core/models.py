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
        ordering = ['name']
        verbose_name_plural = "Entities"


class EventType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    type        = models.ForeignKey('EventType')
    name        = models.CharField(max_length=200)
    start_time  = models.DateTimeField('Start')
    end_time    = models.DateTimeField('End', blank=True, null=True)
    entities    = models.ManyToManyField('Entity')
    location    = models.CharField(max_length=200, blank=True, null=True)
    participant = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cause       = models.TextField(blank=True, null=True)
    effect      = models.TextField(blank=True, null=True)
    stories     = models.ManyToManyField('Story', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_time']


class EventRelation(models.Model):
    from_event  = models.ForeignKey('Event', related_name='from_event')
    to_event    = models.ForeignKey('Event', related_name='to_event')
    description = models.TextField()


class Story(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stories"