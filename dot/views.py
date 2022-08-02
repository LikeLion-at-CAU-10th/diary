from django.shortcuts import render

# Create your views here.


def cherry(request):
    return render(request, 'cherry.html')
