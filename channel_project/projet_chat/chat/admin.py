from django.contrib import admin
from .models import Chat
# Register your models here.


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'message',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter =(
        'user',
        'status',
        'date_add',
        'date_upd'
    )
    search_field = (
        'message',
    )


