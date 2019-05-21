from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from .models import Event, Detail
from .forms import EventForm, DetailForm

# Create your views here.

def index(request):
    event = Event.objects.all()
    return render(request, 'event/index.html', {'event': event})

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail.html', {'event': event})

def create_event(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        events = Event.objects.all()
        for event in events:
            if event.event_name == form.cleaned_data.get('event_name'):
                context = {
                    'form': form,
                    'message': 'Event Already Exists!'
                }
                return render(request, 'event/create_event.html', context)
        event = form.save(commit=False)
        event.event_cover = request.FILES['event_cover']
        event.save()
        return render(request, 'event/index.html', {'form': form})
    return render(request, 'event/create_event.html', {'form': form})

class EventUpdateView(UpdateView):
    model = Event
    fields = ['event_host', 'event_name', 'event_cover']
    template_name = 'event/create_event.html'

class EventDeleteView(DeleteView):
    model = Event
    success_url = '/'

def create_detail(request, event_id):
    form = DetailForm(request.POST or None, request.FILES or None)
    event = get_object_or_404(Event, pk=event_id)
    if form.is_valid():
        detail = form.save(commit=False)
        for d in event.detail_set.all():
            if d.description == form.cleaned_data.get('description'):
                context = {
                    'form': form,
                    'message': 'Description Already Exists'
                }
                return render(request, 'event/create_detail.html', context)

        detail.event= event
        detail.save()
        return render(request, 'event/detail.html', {'event': event})
    return render(request, 'event/create_detail.html', {'form': form})

class DetailUpdateView(UpdateView):
    model = Detail
    fields = ['description', 'place', 'time']
    template_name = 'event/create_detail.html'

    def form_valid(self, form, **kwargs):
        event = get_object_or_404(Event, pk=self.kwargs.get('pk'))
        form.instance.event = event
        return super().form_valid(form)




