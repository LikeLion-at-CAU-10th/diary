from django.shortcuts import get_object_or_404, render

# Create your views here.


def cherry(request):
    return render(request, 'cherry.html')


def input(request):
    return render(request, 'input.html')
