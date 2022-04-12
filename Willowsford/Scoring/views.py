from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import ManualScoringForm

# Create your views here.

def manualScoring(request):
    if request.POST:
        form = ManualScoringForm(request.POST)
        if form.is_valid():
            round1 = int(form['r1n1'].value()) + int(form['r1n2'].value()) + int(form['r1n3'].value())
            form.round1 = round1
            form.round1 = round1
            round2 = int(form['r2n1'].value()) + int(form['r2n2'].value()) + int(form['r2n3'].value())
            form.round2 = round2 + round1
            form.round2 = round2
            round3 = int(form['r3n1'].value()) + int(form['r3n2'].value()) + int(form['r3n3'].value())
            form.round3 = round3 + round2 + round1 
            round4 = int(form['r4n1'].value()) + int(form['r4n2'].value()) + int(form['r4n3'].value())
            form.round4 = round4 + round3 + round2 + round1 
            round5 = int(form['r5n1'].value()) + int(form['r5n2'].value()) + int(form['r5n3'].value())
            form.round5 = round5 + round4 + round3 + round2 + round1 
            round6 = int(form['r6n1'].value()) + int(form['r6n2'].value()) + int(form['r6n3'].value())
            form.round6 = round6 + round5 + round4 + round3 + round2 + round1 
            round7 = int(form['r7n1'].value()) + int(form['r7n2'].value()) + int(form['r7n3'].value())
            form.round7 = round7 + round6 + round5 + round4 + round3 + round2 + round1 
            round8 = int(form['r8n1'].value()) + int(form['r8n2'].value()) + int(form['r8n3'].value())
            form.round8 = round8 + round7 + round6 + round5 + round4 + round3 + round2 + round1 
            round9 = int(form['r9n1'].value()) + int(form['r9n2'].value()) + int(form['r9n3'].value())
            form.round9 = round9 + round8 + round7 + round6 + round5 + round4 + round3 + round2 + round1 
            round10 = int(form['r10n1'].value()) + int(form['r10n2'].value()) + int(form['r10n3'].value())
            form.round10 = round10 + round9 + round8 + round7 + round6 + round5 + round4 + round3 + round2 + round1 
            form.result = round1 + round2 + round3 + round4 + round5 + round6 + round7 + round8 + round9 + round10
            return render(request, 'Scoring/manualScoring.html', {'form': form})
        else:
            return render(request, 'Scoring/manualScoring.html', {'form': form})
    else:
        form = ManualScoringForm()
        return render(request, 'Scoring/manualScoring.html', {'form': form})





    
