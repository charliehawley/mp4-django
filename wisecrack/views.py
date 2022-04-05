from django.shortcuts import render
from django.views import generic
from .models import Prompt


class PromptList(generic.ListView):
    model = Prompt
    queryset = Prompt.objects.order_by('-date')
    template_name = 'prompt_list.html'
