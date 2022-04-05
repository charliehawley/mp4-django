from django.shortcuts import render
from django.views import generic
from .models import Prompt


class PromptList(generic.ListView):
    model = Prompt
    queryset = Prompt.objects.order_by('created_on')
    template_name = 'index.html'
