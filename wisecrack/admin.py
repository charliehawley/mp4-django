from django.contrib import admin
from .models import Prompt, Sub


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('prompt',)}


admin.site.register(Sub)
