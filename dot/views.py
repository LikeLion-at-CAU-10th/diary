from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *


def choosen_picture(request, member_picture_id):

    if request.method=="GET":
        diary_data=get_object_or_404(Diary,pk=id)
        member_picture_data=get_object_or_404(MemberPicture,pk=id)

        choosen_picture_dic={
                "diary_id"        : diary_data.diary_id,
                "member_id"        : member_picture_data.member_id,
                "picture_id"        : member_picture_data.pictrue_id,

                "title"     : diary_data.title,
                "content" : diary_data.content,
                "weather"     : diary_data.weather,
                "feeling"  : diary_data.feeling,

                "uncolored_dot_info":member_picture_data.uncolored_dot_info,
                "colored_dot_info":member_picture_data.colored_dot_info
                
        }
        
        # return render(request,)

    elif request.method=="PATCH":
        new_diary=Diary.objects.update({
        "title"  :  request.POST['title'],
        "content"  :  request.POST['content'],
        "weather"   :  request.POST['weather'],
        "feeling"   :  request.POST['feeling']
        })
    
        
        uncolored=member_picture_data.uncolored_dot_info
        new_uncolored_dot_info=uncolored-uncolored[:-1] 

        colored=member_picture_data.colored_dot_info
        new_colored_dot_info=str(int(colored)+1)

        new_dot=MemberPicture.objects.update({
            "uncolored_dot_info":new_uncolored_dot_info,
            "colored_dot_info":new_colored_dot_info
        })

        # return render(request,)











def input(request, id):
    if request.method=="POST":
        diary_data=get_object_or_404(Diary, pk=id)
        diary_data.title=request.POST['title']
        diary_data.content=request.POST['content']
        diary_data.create_date=request.POST['create_date']
        diary_data.updated_date=request.POST['updated_date']
        diary_data.weather=request.POST['weather']
        diary_data.feeling=request.POST['feeling']

def practice(request):
    print(request.user.id)




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
