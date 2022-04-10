'''
Admin module manages tables in django database
'''

from django.contrib import admin
from .models import Prompt, Sub


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    '''
    Registers 'prompt' table and organises search and display fields
    in database.
    '''

    prepopulated_fields = {'slug': ('prompt',)}
    list_display = ('date', 'prompt', 'id')
    list_filter = ('date',)


@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    '''
    Registers 'submission' table and organises search and display fields
    in database.
    '''

    list_display = ('sub', 'user', 'prompt', 'pk')
    list_filter = ('prompt',)
