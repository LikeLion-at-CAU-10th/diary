from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *
from django.forms import modelformset_factory

def init_picture(request, id):
    memberId = request.user.id
    pictureId = id

    picture_data = get_object_or_404(Picture, pk = id)
    lst = list(range(1,len(picture_data.dot_count) + 1))
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

    num=get_object_or_404(User, memberId)
    num=num.picture_list
    arr=list(map(int,num.split()))
    for n in arr: 
        if pictureId==n:
            arr.remove(n)
    new_picture =' '.join(map(str, arr))
    new_picture_list=User.objects.update({
        "picture_list": request.POST['new_picture_list'],
    })
    
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
        
        arr=list(map(int,uncolored.split()))
        arr.pop()
        arr =' '.join(map(str, arr))
        new_uncolored_dot_info=arr
    
        colored=member_picture_data.colored_dot_info
        new_colored_dot_info=str(int(colored)+1)

        new_dot=MemberPicture.objects.update({
            "uncolored_dot_info": request.POST['new_uncolored_dot_info'],
            "colored_dot_info": request.POST['new_colored_dot_info']
        })

        return render(request, input.html, {"new_dot":new_dot} )
# GET/ POST:
# GET : User.picture_list 끌고와서 알아서 보여줘
# <img src = "{{ picture.picture_info.url }}"> <-- 이거로 접근가능 ... 이거 이용해서 화면에 잘 보여주도록 
def pictures(reqeuest):
    pass

def practice(request):
    if request.method=="GET":
        picture = Picture.objects.all()
        context_list=[]
        for i in range(len(picture)):
            context_list.append(picture[i])
    
        context = {"picture_list" : context_list}
        return render(request, 'dot/practice.html', context = context)

