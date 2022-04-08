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
            round2 = int(form['r2n1'].value()) + int(form['r2n2'].value()) + int(form['r2n3'].value())
            round3 = int(form['r3n1'].value()) + int(form['r3n2'].value()) + int(form['r3n3'].value())
            round4 = int(form['r4n1'].value()) + int(form['r4n2'].value()) + int(form['r4n3'].value())
            round5 = int(form['r5n1'].value()) + int(form['r5n2'].value()) + int(form['r5n3'].value())
            round6 = int(form['r6n1'].value()) + int(form['r6n2'].value()) + int(form['r6n3'].value())
            round7 = int(form['r7n1'].value()) + int(form['r7n2'].value()) + int(form['r7n3'].value())
            round8 = int(form['r8n1'].value()) + int(form['r8n2'].value()) + int(form['r8n3'].value())
            round9 = int(form['r9n1'].value()) + int(form['r9n2'].value()) + int(form['r9n3'].value())
            round10 = int(form['r10n1'].value()) + int(form['r10n2'].value()) + int(form['r10n3'].value())
            form.result = round1 + round2 + round3 + round4 + round5 + round6 + round7 + round8 + round9 + round10
            return render(request, 'Scoring/manualScoring.html', {'form': form})
        else:
            return render(request, 'Scoring/manualScoring.html', {'form': form})
    else:
        form = ManualScoringForm()
        return render(request, 'Scoring/manualScoring.html', {'form': form})

def RenewBookForm(request):
    if request.POST:
        form = RenewBookForm(request.POST)
        if form.is_valid():
            form.result = "This works"
            return render(request, 'Scoring/manualScoring.html', {'form': form})
        else:
            return render(request, 'Scoring/manualScoring.html', {'form': form})
    else:
        form = RenewBookForm()
        return render(request, 'Scoring/manualScoring.html', {'form': form})

def receiveInput(request):
   # if request.method == "POST":
       # mydict={}
       # mydict['rec_lb_no_sight']=request.POST.get('rec_lb_no_sight')
        #mydict['rec_lb_with_sight']=request.POST.get('rec_lb_with_sight')
       # mydict['rec_lb_with_sight_mech_rel']=request.POST.get('rec_lb_with_sight_mech_rel')
        #mydict['comp_bow_stand_w_no_ext']=request.POST.get('comp_bow_stand_w_no_ext')
    return render(request,'index.html')

    
def calculateScore(request):
    r1n1 = int(request.GET["r1_1"])
    r1n2 = int(request.GET["r1_2"])
    r1n3 = int(request.GET["r1_3"])
    res1 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r2_1"])
    r1n2 = int(request.GET["r2_2"])
    r1n3 = int(request.GET["r2_3"])
    res2 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r3_1"])
    r1n2 = int(request.GET["r3_2"])
    r1n3 = int(request.GET["r3_3"])
    res3 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r4_1"])
    r1n2 = int(request.GET["r4_2"])
    r1n3 = int(request.GET["r4_3"])
    res4 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r5_1"])
    r1n2 = int(request.GET["r5_2"])
    r1n3 = int(request.GET["r5_3"])
    res5 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r6_1"])
    r1n2 = int(request.GET["r6_2"])
    r1n3 = int(request.GET["r6_3"])
    res6 = r1n1 + r1n2 + r1n3  
    r1n1 = int(request.GET["r7_1"])
    r1n2 = int(request.GET["r7_2"])
    r1n3 = int(request.GET["r7_3"])
    res7 = r1n1 + r1n2 + r1n3  
    r1n1 = int(request.GET["r8_1"])
    r1n2 = int(request.GET["r8_2"])
    r1n3 = int(request.GET["r8_3"])
    res8= r1n1 + r1n2 + r1n3        
    r1n1 = int(request.GET["r9_1"])
    r1n2 = int(request.GET["r9_2"])
    r1n3 = int(request.GET["r9_3"])
    res9 = r1n1 + r1n2 + r1n3
    r1n1 = int(request.GET["r10_1"])
    r1n2 = int(request.GET["r10_2"])
    r1n3 = int(request.GET["r10_3"])
    res10 = r1n1 + r1n2 + r1n3        
    context = {
        'answer1': res1,
        'answer2': res2
    }
    return render (request,'result.html', context)



def receiveInput(request):
   # if request.method == "POST":
       # mydict={}
       # mydict['rec_lb_no_sight']=request.POST.get('rec_lb_no_sight')
        #mydict['rec_lb_with_sight']=request.POST.get('rec_lb_with_sight')
       # mydict['rec_lb_with_sight_mech_rel']=request.POST.get('rec_lb_with_sight_mech_rel')
        #mydict['comp_bow_stand_w_no_ext']=request.POST.get('comp_bow_stand_w_no_ext')
    return render(request,'index.html')

    
def calculateScore(request):
    r1n1 = int(request.GET["r1_1"])
    r1n2 = int(request.GET["r1_2"])
    r1n3 = int(request.GET["r1_3"])
    res1 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r2_1"])
    r1n2 = int(request.GET["r2_2"])
    r1n3 = int(request.GET["r2_3"])
    res2 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r3_1"])
    r1n2 = int(request.GET["r3_2"])
    r1n3 = int(request.GET["r3_3"])
    res3 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r4_1"])
    r1n2 = int(request.GET["r4_2"])
    r1n3 = int(request.GET["r4_3"])
    res4 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r5_1"])
    r1n2 = int(request.GET["r5_2"])
    r1n3 = int(request.GET["r5_3"])
    res5 = r1n1 + r1n2 + r1n3    
    r1n1 = int(request.GET["r6_1"])
    r1n2 = int(request.GET["r6_2"])
    r1n3 = int(request.GET["r6_3"])
    res6 = r1n1 + r1n2 + r1n3  
    r1n1 = int(request.GET["r7_1"])
    r1n2 = int(request.GET["r7_2"])
    r1n3 = int(request.GET["r7_3"])
    res7 = r1n1 + r1n2 + r1n3  
    r1n1 = int(request.GET["r8_1"])
    r1n2 = int(request.GET["r8_2"])
    r1n3 = int(request.GET["r8_3"])
    res8= r1n1 + r1n2 + r1n3        
    r1n1 = int(request.GET["r9_1"])
    r1n2 = int(request.GET["r9_2"])
    r1n3 = int(request.GET["r9_3"])
    res9 = r1n1 + r1n2 + r1n3
    r1n1 = int(request.GET["r10_1"])
    r1n2 = int(request.GET["r10_2"])
    r1n3 = int(request.GET["r10_3"])
    res10 = r1n1 + r1n2 + r1n3        
    context = {
        'answer1': res1,
        'answer2': res2
    }
    return render (request,'result.html', context)




