from django.shortcuts import get_object_or_404, render

# Create your views here.


def cherry(request):
    return render(request, 'cherry.html')


def input(request):
    request.user.id
    return render(request, 'input.html')


def output(request, id):
    # if 'user_email' not in request.session:
    #     return redirect('login_view')
    # widget = get_object_or_404(StoreWidget, seq=id)
    # related_widgets=StoreWidget.objects.filter(widget_type=widget.widget_type).exclude(seq=id)
    # email= request.session['user_email']
    # user = User_info.objects.get(user_email=email)

    # # comment = get_object_or_404(Comment, id=id)
    # comments = Comment.objects.filter(widget=widget)
    date = get_object_or_404(date, id=id)

    return render(request, 'output.html', {"date": date, 'title': title})
