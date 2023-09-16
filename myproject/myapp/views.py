from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Quick'
    feature1.details = 'Exceptional delivery done at lightning speed'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Trustworthy'
    feature2.details = 'We value your confidence in our service'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Remarkable'
    feature3.details = 'We strive to ensure delivery of service you cannot forget in a hurry'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Prepared'
    feature4.details = 'Come rain, come sunshine, we are here to serve you'

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features' : features})

def counter(request):
    texts = request.POST['texts']
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount': amount_of_words})