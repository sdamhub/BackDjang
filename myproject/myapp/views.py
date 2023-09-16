from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()

    return render(request, 'index.html', {'features' : features})

def counter(request):
    texts = request.POST['texts']
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount': amount_of_words})