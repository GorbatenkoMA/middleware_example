from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        print(request.session.get('timezone'))
        return super().get(request, *args, **kwargs)
