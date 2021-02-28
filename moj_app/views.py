from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def o_sajtu(request):
    return render(request, 'o_sajtu.html', {})

def kontakt(request):
    return render(request, 'kontakt.html', {})
