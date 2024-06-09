from django.contrib import admin
from actors.models import actor


@admin.register(actor)
class actorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
