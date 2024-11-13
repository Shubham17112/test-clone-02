



from django.contrib import admin
 
# Register your models here.
from .models import Category,Event, EventDetail
 
 
admin.site.register(Category)
from django.contrib import admin
from .models import  EventImage

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1  # Allows adding multiple images initially

@admin.register(EventDetail)
class EventDetailAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Event)
