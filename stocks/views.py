from django.shortcuts import render

from .stocks import get_random_context


def index(request):
    context = get_random_context()
    template_name = 'index.html'
    return render(request, template_name, context)
