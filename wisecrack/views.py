from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Prompt, Sub
from .forms import SubForm


class PromptList(generic.ListView):
    model = Prompt
    queryset = Prompt.objects.order_by('-date')
    template_name = 'prompt_list.html'


class PromptDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Prompt.objects
        prompt = get_object_or_404(queryset, slug=slug)
        subs = Sub.objects.order_by('created_on')

        return render(
            request,
            "prompt_detail.html",
            {
                "prompt": prompt,
                "subs": subs,
                "sub_form": SubForm
            }
        )
