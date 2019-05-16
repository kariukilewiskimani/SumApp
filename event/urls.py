from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<event_id>[0-9]+)/', views.detail, name='detail'),
    path('create_event', views.create_event, name='create_event'),
    path('<int:pk>/update-event', views.EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete-event', views.EventDeleteView.as_view(), name='event-delete'),
    path('(?P<event_id>[0-9]+)/create_detail', views.create_detail, name='create_detail'),
    path('<int:pk>/update-detail', views.DetailUpdateView.as_view(), name='detail-update'),


]