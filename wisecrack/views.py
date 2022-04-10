from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
# from django.contrib import messages
from .models import Prompt, Sub
from .forms import SubForm


class PromptList(generic.ListView):
    model = Prompt
    queryset = Prompt.objects.order_by('-date')
    template_name = 'prompt_list.html'


class UserSubList(View):
    def get(self, request, pk, *args, **kwargs):
        subs = Sub.objects.filter(user=pk)

        return render(
            request,
            "user_sub_list.html",
            {
                "subs": subs
            }
        )


class EditSub(View):
    def get(self, request, prompt, pk, id, *args, **kwargs):
        p_id = ''.join(x for x in prompt if x.isdigit())
        prompt_id = Prompt.objects.filter(pk=p_id)
        sub = Sub.objects.filter(user=pk)
        instance = get_object_or_404(Sub, id=id)
        sub_form = SubForm(instance=instance)

        return render(
            request,
            "edit_sub.html",
            {
                "prompt": prompt_id,
                "sub": sub,
                "sub_form": sub_form
            }
        )

    def post(self, request, prompt, pk, id, *args, **kwargs):
        p_id = ''.join(x for x in prompt if x.isdigit())
        # prompt = Prompt.objects.filter(pk=id)
        prompt = get_object_or_404(Prompt, pk=p_id)
        slug = prompt.slug
        
        sub = Sub.objects.filter(user=pk)
        instance = get_object_or_404(Sub, id=id)
        subs = Sub.objects.filter(user=pk)

        sub_form = SubForm(data=request.POST, instance=instance)
        
        if sub_form.is_valid():
            sub_form.instance.user = request.user
            sub_form.instance.name = request.user.username
            sub = sub_form.save(commit=False)
            sub.prompt = prompt
            prompt.slug = slug
            sub.save()
        else:
            sub_form = SubForm()

        return render(
            request,
            "user_sub_list.html",
            {
                # "prompt": prompt,
                "subs": subs,
                # "slug": slug,
                # "submitted": True,
                "sub_form": sub_form
            }
        )
        # return render(
        #     request,
        #     "user_sub_list.html",
        #     {
        #         "subs": subs
        #     }
        # )


class DeleteSub(View):
    def get(self, request, pk, sub, *args, **kwargs):
        subs = Sub.objects.filter(user=pk, sub=sub)
        subs.delete()

        # delete_sub = DeleteSub(data=request.DELETE)
        return HttpResponseRedirect(reverse('user_sub_list', args=[pk]))


class PromptDetail(View):
    def get(self, request, slug, pk, *args, **kwargs):
        queryset = Prompt.objects
        prompt = get_object_or_404(queryset, slug=slug)
        subs = Sub.objects.filter(prompt=pk).order_by('created_on')
        submitted = False

        subbed_users = []
        for user in subs:
            subbed_users.append(user)
            print(user)

        if request.user.username in subbed_users:
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

    def post(self, request, slug, pk, *args, **kwargs):
        queryset = Prompt.objects
        prompt = get_object_or_404(queryset, slug=slug)
        subs = Sub.objects.filter(prompt=pk).order_by('created_on')
        # submitted = False
        # if prompt.subs_list.filter(id=self.request.user.id).exists():
        #     submitted = True

        sub_form = SubForm(data=request.POST)

        # if submitted:
            # return render(
            #     request,
            #     "prompt_detail.html",
            #     {
            #         "prompt": prompt,
            #         "subs": subs,
            #         # "submitted": True,
            #         "sub_form": sub_form
            #     }
            # )
        # else:
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
                # "submitted": False,
                "sub_form": sub_form
            }
        )


class SubUpvote(View):
    def post(self, request, slug, pk, user, *args, **kwargs):
        sub = get_object_or_404(Sub, pk=pk)
        if request.user.username == user:
            return HttpResponseRedirect(reverse('prompt_detail', args=[slug]))
        else:
            if sub.upvotes.filter(id=request.user.id).exists():
                sub.upvotes.remove(request.user)
                # voted = True
                return HttpResponseRedirect(reverse('prompt_detail',
                                                    args=[slug]))
            else:
                sub.upvotes.add(request.user)
                # voted = False
                return HttpResponseRedirect(reverse('prompt_detail',
                                                    args=[slug]))
