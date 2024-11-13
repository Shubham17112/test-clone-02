from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Event
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,"hero.html")



def sports(request):
    categories = Category.objects.all()
    events = Event.objects.all()
    return render(request, 'sports.html', {'categories': categories, 'events': events})

def category_events(request, category_id):
    categories = Category.objects.all()

    category = get_object_or_404(Category, id=category_id)
    events = category.events.all()
    return render(request, 'sports.html', {'categories':categories,'category': category, 'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})



