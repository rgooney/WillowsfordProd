from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request, 'MemberManagement/signIn.html')

def adminPanel(request):
    return render(request, 'MemberManagement/adminPanel.html')