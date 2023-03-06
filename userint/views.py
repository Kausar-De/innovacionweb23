from urllib import response
from django.shortcuts import render, redirect
from userint.models import Participant
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ParticipantForm
import datetime
import csv
from django.http import HttpResponse

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        user = authenticate(request, username = userid, password = password)

        if user is not None:
            login(request, user)
            return redirect('entry')
        else:
            messages.info(request, 'User ID OR Password is incorrect!')
            return render(request, 'userint/login.html')

    context = {}

    return render(request, 'userint/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'Successfully logged out!')
    return redirect('login')

def entryPage(request):
    currenttime = datetime.datetime.now()
    beforetime = datetime.datetime(2022, 4, 2, hour = 18, minute = 0, second = 0)
    aftertime = datetime.datetime(2023, 4, 3, hour = 18, minute = 0, second = 0)
    if currenttime < beforetime:
        return redirect('tooearly')
    elif currenttime > aftertime:
        return redirect('toolate')
    else:
        subs = Participant.objects.filter(participant = request.user)
        subcount = subs.count()
        form = ParticipantForm()

        if subcount > 0:
            sub = Participant.objects.get(participant = request.user)
            form = ParticipantForm(instance = sub)

            if request.method == 'POST':
                form = ParticipantForm(request.POST, instance = sub)
                if form.is_valid():
                    form.save()
                    return redirect('thankyou')
        else:
            if request.method == 'POST':
                form = ParticipantForm(request.POST)        
                if form.is_valid():
                    stock = form.save(commit = False)
                    stock.participant = request.user
                    stock.created_date = datetime.datetime.now()
                    stock.save()
                
                    return redirect('thankyou')

    context = {'form':form}

    return render(request, 'userint/entry.html', context)

def thankyouPage(request):
    return render(request, 'userint/thankyou.html')

def tooearlyPage(request):
    return render(request, 'userint/tooearly.html')

def toolatePage(request):
    return render(request, 'userint/toolate.html')

def extract_CSV(request):
    response = HttpResponse(content_type = 'text/csv')
    
    writer = csv.writer(response)
    writer.writerow(['Participant ID', 'Team Name', 'Team Lead Name', 'Team Lead Phone No.', 'Team Lead Email', 'Member 2 Name', 'Member 3 Name', 'Member 4 Name', 'GitHub Repository Link', 'Live Deployment Link', 'Creation Date'])

    for parti in Participant.objects.all().values_list('participant', 'teamname', 'teamlead', 'leadphone', 'leademail', 'member2', 'member3', 'member4', 'repolink', 'livelink', 'created_date'):
        writer.writerow(parti)

    response['Content-Disposition'] = 'attachment; filename = "404Submissions.csv"'

    return response
