from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hey World!')

def home(request):
    context = {"greeting": "Have a good day"}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', )

def contact(request):
    contact = {
        "email": "wambo@gmail"
    }
    return render(request, 'contact.html', contact )


