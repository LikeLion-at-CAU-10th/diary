from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *

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
    # User 안에있는 picutre_list에서 picutre_id있는 string을 없애야됨...
    # update해야함 >>> "1 2 3 4 5" >> string
    # pictureId = int 
    # arr = map(int,string.split()) -- > 얘는 안에 다 int형임
    # new_string = " ".join(arr)
    
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
# <img src = "{{ picture.picture_info.url }}"> <-- 이거로 접근가능 ... 이거 이용해서 화면에 잘 보여주도록 
# 이미지 누르면 갈 url과 어떠한 이미지를 띄울지랑 언제부터 언제까지의 일기인지
def pictures(request):
    user = User.objects.filter(pk = request.user.id)
    print(user)
    return render(request,'rocket.html')
    

def practice(request):
    picture = Picture.objects.filter(pk = 1)
   
    context = {"picture" : picture[0]}
    return render(request, 'dot/practice.html', context = context)

