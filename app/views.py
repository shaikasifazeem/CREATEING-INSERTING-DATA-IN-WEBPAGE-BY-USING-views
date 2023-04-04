from django.shortcuts import render
from app.models import *

def display(request):

    LOT=Topic.objects.all()
    d={'Topics':LOT}

    return render(request,'display.html',context=d)

def display2(request):
    LOW=Webpage.objects.all()
    d={'Webpages':LOW}
    return render(request,'display2.html',context=d)



def display3(request):
    LOA=AccessRecord.objects.all()
    d={'AccessRecords':LOA}
    return render(request,'display3.html',context=d)

