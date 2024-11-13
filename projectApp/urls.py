from django.urls import path
#now import the views.py file into this code
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns=[
path('',views.index,name="index"),

 path('categories/<int:category_id>/', views.category_events, name='category_events'),
  path('admin/', admin.site.urls,name='admin'),
path('sports/', views.sports, name='sports'),
 path('events/<int:event_id>/', views.event_detail, name='event_detail'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
