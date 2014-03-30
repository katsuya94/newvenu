from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'start', 'tipped')

# Register your models here.
admin.site.register(Event, EventAdmin)