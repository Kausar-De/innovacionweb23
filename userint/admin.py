from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin

# Register your models here.

class ParticipantAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('participant', 'teamname', 'teamlead', 'leadphone', 'leademail', 'member2', 'member3', 'member4', 'levelchoice', 'repolink', 'livelink', 'codingvideolink', 'videolink', 'created_date')

admin.site.register(Participant, ParticipantAdmin)