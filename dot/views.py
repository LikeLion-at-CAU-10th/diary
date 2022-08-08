from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *

def init_picture(request, id):
    memberId = request.user.id
    pictureId = id
    picture_data = get_object_or_404(Picture, pk = id)
    lst = list(range(1,len(picture_data) + 1))
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    uncolored_dot_string = " ".join(lst)    
    diary_list = []
    for _ in range(len(lst)):
        diary = Diary.objects.create(
            title = '',
            content = '',
            weather = None,
            feeling = None,
        )
        diary_list.append(str(diary.id))
    
    new_data = MemberPicture.objects.create(
        member_id = memberId,
        picture_id = pictureId,
        uncolored_dot_info = uncolored_dot_string,
        colored_dot_info = "",
        diary_id = " ".join(diary_list)
    )
    # return render()
    

def choosen_picture(request, diary_id, memberpicture_id):

    if request.method=="GET":
        diary_data=get_object_or_404(Diary,pk=diary_id)
        choosen_picture_dic={
                "diary_id"        : diary_data.diary_id,
                "title"     : diary_data.title,
                "content" : diary_data.content,
                "weather"     : diary_data.weather,
                "feeling"  : diary_data.feeling,          
        }
        
        return render(request, output.html, {"choosen_picture_dic":choosen_picture_dic})

    elif request.method=="PATCH":
        member_picture_data=get_object_or_404(MemberPicture,pk=memberpicture_id)
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

        return render(request, input.html, {"new_dot":new_dot} )
# GET/ POST:
# GET : User.picture_list 끌고와서 알아서 보여줘
# <img src = {% static %}
# POST : 
# 

def pictures(reqeuest):
    pass

def practice(request):
    picture = Picture.objects.filter(pk = 1)

    context = {"picture" : picture}
    return render(request, 'dot/practice.html', context = context)