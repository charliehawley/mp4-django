from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Prompt, Sub
from .forms import SubForm


class PromptList(generic.ListView):
    model = Prompt
    queryset = Prompt.objects.order_by('-date')
    template_name = 'prompt_list.html'

# class UserSubList(generic.ListView):
#     model = Sub
#     queryset = Sub.objects.filter(user=request.user)
#     template_name = 'user_sub_list.html'


class PromptDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Prompt.objects
        prompt = get_object_or_404(queryset, slug=slug)
        subs = Sub.objects.order_by('created_on')
        submitted = False
        if prompt.subs_list.filter(pk=self.request.user.pk).exists():
            submitted = True

        return render(
            request,
            "prompt_detail.html",
            {
                "prompt": prompt,
                "subs": subs,
                "submitted": submitted,
                "sub_form": SubForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Prompt.objects
        prompt = get_object_or_404(queryset, slug=slug)
        subs = Sub.objects.order_by('created_on')
        submitted = False
        if prompt.subs_list.filter(id=self.request.user.id).exists():
            submitted = True

        sub_form = SubForm(data=request.POST)

        if submitted:
            return render(
                request,
                "prompt_detail.html",
                {
                    "prompt": prompt,
                    "subs": subs,
                    "submitted": True,
                    "sub_form": sub_form
                }
            )
        else:
            if sub_form.is_valid():
                sub_form.instance.user = request.user
                sub_form.instance.name = request.user.username
                sub = sub_form.save(commit=False)
                sub.prompt = prompt
                sub.save()
            else:
                sub_form = SubForm()

            return render(
                request,
                "prompt_detail.html",
                {
                    "prompt": prompt,
                    "subs": subs,
                    "submitted": False,
                    "sub_form": sub_form
                }
            )


class SubUpvote(View):

    def post(self, request, slug, pk, *args, **kwargs):
        queryset = Prompt.objects
        prompt = get_object_or_404(queryset, slug=slug)
        subs = Sub.objects.order_by('created_on')
        sub = get_object_or_404(Sub, pk=pk)
        # if request.user.id == sub.user.id: #alert "Can't vote for your own!"
        # if authenticated!
        # @loginrequired
        if sub.pk == request.user.id:
            return HttpResponseRedirect(reverse('prompt_detail', args=[slug]))
        else:
            if sub.upvotes.filter(id=request.user.id).exists():
                sub.upvotes.remove(request.user)
            else:
                sub.upvotes.add(request.user)

            # sub_form = SubForm(data=request.POST)

            # return render(
            #     request,
            #     "prompt_detail.html",
            #     {
            #         "prompt": prompt,
            #         "subs": subs,
            #         "voted": True,
            #         "sub_form": sub_form
            #     }
            # )

        return HttpResponseRedirect(reverse('prompt_detail', args=[slug]))
