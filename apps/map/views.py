from django.views.generic.edit import CreateView
from .models import map

# Create your views here.

class MapView(CreateView):
        model = map
        fields = ['address']
        template_name = 'map/map.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['mapbox_access_token'] = 'pk.eyJ1IjoiY3JhdXoiLCJhIjoiY2w0dzZjZWk5MjV4eTNqczg2bmIwazNoMCJ9.VaYyChMCUOnf5dJjUhDwDg'
            context['addresses'] = map.objects.all()
            return context