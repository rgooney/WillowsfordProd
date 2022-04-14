from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import ManualScoringModelForm

# Create your views here.
@login_required(login_url='signIn')
def manualScoring(request):
    if request.POST:
        form = ManualScoringModelForm(request.POST)
        user = User.objects.get(username=request.user)
        account = user.useraccount
        if form.is_valid():
            score = form.save(commit=False)

            score.account_id=account

            round1 = int(form['r1n1'].value()) + int(form['r1n2'].value()) + int(form['r1n3'].value())
            score.subtotalRoundOne = round1
            score.cumulativeRoundOne = round1
            round2 = int(form['r2n1'].value()) + int(form['r2n2'].value()) + int(form['r2n3'].value())
            score.subtotalRoundTwo = round2
            score.cumulativeRoundTwo = round2 + round1
            round3 = int(form['r3n1'].value()) + int(form['r3n2'].value()) + int(form['r3n3'].value())
            score.subtotalRoundThree = round3
            score.cumulativeRoundThree = round3 + round2 + round1
            round4 = int(form['r4n1'].value()) + int(form['r4n2'].value()) + int(form['r4n3'].value())
            score.subtotalRoundFour = round4
            score.cumulativeRoundFour = round4 + round3 + round2 + round1
            round5 = int(form['r5n1'].value()) + int(form['r5n2'].value()) + int(form['r5n3'].value())
            score.subtotalRoundFive = round5
            score.cumulativeRoundFive = round5 + round4 + round3 + round2 + round1
            round6 = int(form['r6n1'].value()) + int(form['r6n2'].value()) + int(form['r6n3'].value())
            score.subtotalRoundSix = round6
            score.cumulativeRoundSix = round6 + round5 + round4 + round3 + round2 + round1
            round7 = int(form['r7n1'].value()) + int(form['r7n2'].value()) + int(form['r7n3'].value())
            score.subtotalRoundSeven = round7
            score.cumulativeRoundSeven = round7 + round6 + round5 + round4 + round3 + round2 + round1
            round8 = int(form['r8n1'].value()) + int(form['r8n2'].value()) + int(form['r8n3'].value())
            score.subtotalRoundEight = round8
            score.cumulativeRoundEight = round8 + round7 + round6 + round5 + round4 + round3 + round2 + round1
            round9 = int(form['r9n1'].value()) + int(form['r9n2'].value()) + int(form['r9n3'].value())
            score.subtotalRoundNine = round9
            score.cumulativeRoundNine = round9 + round8 + round7 + round6 + round5 + round4 + round3 + round2 + round1
            round10 = int(form['r10n1'].value()) + int(form['r10n2'].value()) + int(form['r10n3'].value())
            score.subtotalRoundTen = round10
            score.cumulativeRoundTen = round10 + round9 + round8 + round7 + round6 + round5 + round4 + round3 + round2 + round1
            score.score = round1 + round2 + round3 + round4 + round5 + round6 + round7 + round8 + round9 + round10
            score.save()
            return render(request, 'Scoring/manualScoring.html', {'form': form})
        else:
            return render(request, 'Scoring/manualScoring.html', {'form': form})
    else:
        form = ManualScoringModelForm()
        return render(request, 'Scoring/manualScoring.html', {'form': form})

    return render(request, 'Scoring/manualScoring.html', {'form': form})




    
