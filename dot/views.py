from cgi import test
from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.
from .models import *
from django.forms import modelformset_factory

# 그림선택후 그림에 대한 정보. 컬러드닷, 언컬러드. 일기생성. 유저객체

# 이미지랑 다이어리 id, 컬러드닷.
def init_picture(request, id):
    member_data=User.objects.filter(pk=request.user.id)[0]
    memberId = request.user.id
    pictureId = id

    picture_data = Picture.objects.filter(pk=id)[0]
    lst = list(range(1,picture_data.dot_count + 1))
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
        diary_list.append(str(diary.diary_id))
    
    new_data = MemberPicture.objects.create(
        member_id = member_data,
        picture_id = picture_data,
        uncolored_dot_info = uncolored_dot_string,
        colored_dot_info = "",
        diary_id = " ".join(diary_list)
    )
    
    num=User.objects.filter(pk=memberId)[0]
    num=num.picture_list
    arr=list(map(int,num.split()))
    for n in arr: 
        if pictureId==n:
            arr.remove(n)
    new_picture =' '.join(map(str, arr))
    new_picture_list=User.objects.update(
        picture_list= new_picture
    )

    int_diary=list(map(int,diary_list)) 
    try:
        colored_dot=int(uncolored_dot_string[0])-1
    except:
        colored_dot=picture_data.dot_count

    context={
        "colored_dot" : colored_dot,
        "diary_id" : int_diary,
        "picture_data":picture_data,
        "member_picture_id":new_data.member_picture_id
    }

    return render(request, 'dot/test.html', context=context)
    

def choosen_picture(request, diary_id,member_picture_id):
    if request.method=="GET":
        diary_data=Diary.objects.filter(pk=diary_id)[0]
        choosen_picture_dic={
                "diary_id"        : diary_data.diary_id,
                "member_picture_id" : member_picture_id,
                "title"     : diary_data.title,
                "content" : diary_data.content,
                "weather"     : diary_data.weather,
                "feeling"  : diary_data.feeling,          
        }
        return render(request, 'diary.html', {"choosen_picture_dic":choosen_picture_dic})

    elif request.method=="POST":
        member_picture_data=MemberPicture.objects.filter(pk=member_picture_id)[0]
        uncolored=member_picture_data.uncolored_dot_info
        arr=list(map(int,uncolored.split()))
        del arr[0]
        arr =' '.join(map(str, arr))
        new_uncolored_dot_info=arr
    
        colored=member_picture_data.colored_dot_info
        try :
            new_colored_dot_info=int(colored)+1
        except:
            new_colored_dot_info=1

        diary_data=Diary.objects.filter(pk=diary_id)[0]
        diary_data.title=request.POST['title']
        diary_data.content=request.POST['content']
        diary_data.weather=request.POST['weather']
        diary_data.feeling=request.POST['feeling']
        diary_data.save()
        
       
        member_picture_data.uncolored_dot_info= new_uncolored_dot_info
        member_picture_data.colored_dot_info= new_colored_dot_info 
        member_picture_data.save()

        context={
        "diary_data" : diary_data,
        "member_picture_data": member_picture_data
    }

        
        return render(request, 'diary_after.html', context=context)
    # return render(request, 'output1.html')

# 그림 테마들 반환, url=/dot, 
# context={'picture_list': [<Picture: Picture object (1)>, <Picture: Picture object (2)>, 
# <Picture: Picture object (3)>, <Picture: Picture object (4)>]}
def pictures(request):
    if request.method=="GET":
        memberid=request.user.id
        user_info=User.objects.filter(pk=memberid)[0]
        # 업로드한 picturelist에 대한 정보=charfield="1 2 3 4"=picture_id

        user_picture=user_info.picture_list 
        user_picture=user_picture.split()
        for i in range(len(user_picture)):
            user_picture[i]=int(user_picture[i])
        context_list=[]
        for i in user_picture:
            picture = Picture.objects.filter(pk=i)[0]
            context_list.append(picture)
    
        context = {"picture_list" : context_list}
        print(context)

        return render(request, 'dot/pictures.html', context = context)


def cherry(request):
    return render(request, 'cherry.html')