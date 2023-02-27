from django.shortcuts import render
# Create your views here.
def home_core(request):
    return render(request, 'main.html')
