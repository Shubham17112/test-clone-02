from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)  # Location field

    def __str__(self):
        return self.title


# Create your models here.
class EventDetail(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='details')
    image = models.ImageField(upload_to='event_images/')
    detailed_description = models.TextField()

    def __str__(self):
        return f"Details for {self.event.title}"
    
    
class EventImage(models.Model):
    event_detail = models.ForeignKey(EventDetail, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')
    def __str__(self):
        return f"Image for {self.event_detail.event.title}"