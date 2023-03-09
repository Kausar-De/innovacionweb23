from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Participant
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        exclude = ['participant', 'created_date']
        widgets = {
            'levelchoice': forms.RadioSelect(),
        }
        labels = {
            'teamname': _('Team Name'),
            'teamlead': _('Name of Team Lead'),
            'leadphone': _('Phone No. of Team Lead (Preferably WhatsApp)'),
            'leademail': _('Email ID of Team Lead'),
            'member2': _('Name of Member 2'),
            'member3': _('Name of Member 3'),
            'member4': _('Name of Member 4'),
            'levelchoice': _('Difficulty Level'),
            'repolink': _('Link to GitHub Repository'),
            'livelink': _('Link to Live Deployment'),
            'videolink': _('Link to Submission Video'),
            'created_date': _('Submission Date & Time'),
        }
