from django.shortcuts import render
from django.views import generic

from application.models import Media

def hello_world(request):
    return render(request, 'application/hello_world.html', {})

class MediaListView(generic.ListView):
    """
    View for all media items
    """
    model = Media
    context_object_name = 'media_list'
    queryset = Media.objects.all()
    template_name = 'application/media_list.html'

    # def get_queryset(self):
    #     return Media.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super(MediaListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'some_data'
    #     return context

class MediaDetailView(generic.DetailView):
    model = Media