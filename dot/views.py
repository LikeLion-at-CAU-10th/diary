from datetime import datetime, date
from cgi import test
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from .models import *
from django.forms import modelformset_factory

# from dateime import datetime
# from django.utils.dateformat import DateFormat

# def date(request):
#     tody=DateFormat(datetime.now()).format('Ymd')


# 그림선택후 그림에 대한 정보. 컬러드닷, 언컬러드. 일기생성. 유저객체
# 이거 나중에 배포하면 picture_id 다 조절해야됨.
# 이미지랑 다이어리 id, 컬러드닷.
def init_picture(request, id):
    if request.method == 'POST':
        member_data = User.objects.filter(pk=request.user.id)[0]
        memberId = request.user.id
        pictureId = id
        picture_data = Picture.objects.filter(pk=id)[0]
        if MemberPicture.objects.filter(member_id=memberId, picture_id=pictureId):
            member_picture_data = MemberPicture.objects.filter(
                member_id=memberId, picture_id=pictureId)[0]

            int_diary = list(map(int, member_picture_data.diary_id.split()))

            try:
                colored_dot = int(member_picture_data.uncolored_dot_info[0])-1
            except:
                colored_dot = picture_data.dot_count

            context = {
                "colored_dot": colored_dot,
                "diary_id": int_diary,
                "picture_data": picture_data,
                "member_picture_id": member_picture_data.member_picture_id
            }

            if pictureId == 1:
                return render(request, 'rocket.html', context=context)
            elif pictureId == 2:
                return render(request, 'cherry.html', context=context)
            elif pictureId == 3:
                return render(request, 'bear.html', context=context)
            elif pictureId == 4:
                   return render(request, 'star.html', context=context)        

            return render(request, 'dot/test.html', context=context)
        else:
            lst = list(range(1, picture_data.dot_count + 1))
            for i in range(len(lst)):
                lst[i] = str(lst[i])
            uncolored_dot_string = " ".join(lst)
            diary_list = []
            for _ in range(len(lst)):
                diary = Diary.objects.create(
                    title='',
                    content='',
                    weather=None,
                    feeling=None,
                )
                diary_list.append(str(diary.diary_id))

            new_data = MemberPicture.objects.create(
                member_id=member_data,
                picture_id=picture_data,
                uncolored_dot_info=uncolored_dot_string,
                colored_dot_info="",
                diary_id=" ".join(diary_list)
            )

            num = User.objects.filter(pk=memberId)[0]
            num = num.picture_list
            arr = list(map(int, num.split()))
            for n in arr:
                if pictureId == n:
                    arr.remove(n)
            new_picture = ' '.join(map(str, arr))
            new_picture_list = User.objects.update(
                picture_list=new_picture
            )

            int_diary = list(map(int, diary_list))
            try:
                colored_dot = int(uncolored_dot_string[0])-1
            except:
                colored_dot = picture_data.dot_count

            context = {
                "colored_dot": colored_dot,
                "diary_id": int_diary,
                "picture_data": picture_data,
                "member_picture_id": new_data.member_picture_id
            }

            if pictureId == 1:
                return render(request, 'rocket.html', context=context)
            elif pictureId == 2:
                return render(request, 'cherry.html', context=context)
            elif pictureId == 3:
                return render(request, 'bear.html', context=context)
            elif pictureId == 4:
                return render(request, 'star.html', context=context)  
            return render(request, 'dot/test.html', context=context)
    if request.method == 'GET':
        member_data = User.objects.filter(pk=request.user.id)[0]
        memberId = request.user.id
        pictureId = id
        picture_data = Picture.objects.filter(pk=id)[0]

        member_picture_data = MemberPicture.objects.filter(
            member_id=memberId, picture_id=pictureId)[0]

        int_diary = list(map(int, member_picture_data.diary_id.split()))
        try:
            colored_dot = int(member_picture_data.uncolored_dot_info[0])-1
        except:
            colored_dot = picture_data.dot_count

        context = {
            "colored_dot": colored_dot,
            "diary_id": int_diary,
            "picture_data": picture_data,
            "member_picture_id": member_picture_data.member_picture_id
        }
        
        if pictureId == 1:
            return render(request, 'rocket.html', context=context)
        elif pictureId == 2:
            return render(request, 'cherry.html', context=context)
        elif pictureId == 3:
            return render(request, 'bear.html', context=context)
        elif pictureId == 4:
                return render(request, 'star.html', context=context)  

        return render(request, 'dot/test.html', context=context)


def what_day_is_it(date):
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = date.weekday()
    return days[day]


def what_month_is_it(month):
    months = ['January', 'February', 'March', 'April', 'May', "June",
              'July', 'August', "September", "October", "November", 'December']
    return months[month-1]


def choosen_picture(request, diary_id, member_picture_id):
    if request.method == "GET":
        diary_data = Diary.objects.filter(pk=diary_id)[0]
        print("이거는",diary_data.foreign_key_tape)


        # if diary_data.foreign_key_tape=="False":
        #     tape_data = Tape.objects.filter(pk = 1)[0]
        # else :
        tape_data = Tape.objects.filter(pk = int(diary_data.foreign_key_tape))[0]




        
        member_picture_data = MemberPicture.objects.filter(pk=member_picture_id)[
            0]
        picture_id = member_picture_data.picture_id.picture_id
        day_en = what_day_is_it(date(diary_data.create_date.year,
                                diary_data.create_date.month, diary_data.create_date.day))
        tapes = Tape.objects.all()
        
        tape = []
        for i in tapes:
            tape.append(i)
       
        choosen_picture_dic = {
            "diary_id": diary_data.diary_id,
            "member_picture_id": member_picture_id,
            "tape_info" : tape_data.tape_info,
            "picture_id" : picture_id, 
            "title": diary_data.title,
            "content": diary_data.content,
            "year": diary_data.create_date.year,
            "month": what_month_is_it(diary_data.create_date.month),
            "day": diary_data.create_date.day,
            "day_en": day_en,
            "tape_all" : tape,
        }

        return render(request, 'diary.html', {"choosen_picture_dic": choosen_picture_dic})

    elif request.method == "POST":
        member_picture_data = MemberPicture.objects.filter(pk=member_picture_id)[
            0]
        uncolored = member_picture_data.uncolored_dot_info
        diary = list(map(int, member_picture_data.diary_id.split()))
        arr = list(map(int, uncolored.split()))
        try:
            value = int(arr[0]) - 1
            if diary[value] == diary_id:
                del arr[0]
        except:
            pass

        arr = ' '.join(map(str, arr))
        new_uncolored_dot_info = arr

        colored = member_picture_data.colored_dot_info
        try:
            new_colored_dot_info = int(colored)+1
        except:
            new_colored_dot_info = 1
        
        
        diary_data = Diary.objects.filter(pk=diary_id)[0]
        # diary_data.foreign_key_tape = request.POST.get('foreign_key_tape', "False" )
        diary_data.foreign_key_tape = request.POST['foreign_key_tape']

        diary_data.title = request.POST['title']
        diary_data.content = request.POST['content']
        diary_data.save()
        print(diary_data.foreign_key_tape)

        member_picture_data.uncolored_dot_info = new_uncolored_dot_info
        member_picture_data.colored_dot_info = new_colored_dot_info
        member_picture_data.save()

        context = {
            "diary_data": diary_data,
            "member_picture_data": member_picture_data
        }

        return redirect('init_picture', member_picture_data.picture_id.picture_id)
        # return render(request, 'output1.html', {"diary_data":diary_data})
    # return render(request, 'output1.html')

# 그림 테마들 반환, url=/dot,
# context={'picture_list': [<Picture: Picture object (1)>, <Picture: Picture object (2)>,
# <Picture: Picture object (3)>, <Picture: Picture object (4)>]}


def pictures(request):
    if request.method == "GET":
        memberid = request.user.id
        user_info = User.objects.filter(pk=memberid)[0]
        # 업로드한 picturelist에 대한 정보=charfield="1 2 3 4"=picture_id

        user_picture = user_info.picture_list

        user_picture = list(map(int, user_picture.split()))

        picture_list = Picture.objects.all()
        context_list = []
        for i in range(4):
            picture = Picture.objects.filter(pk=picture_list[i].picture_id)[0]
            context_list.append(picture)
        real_idx = 0
        idx = 0
        three_context_list = []
        while real_idx < len(context_list):
            three_context_list.append([])
            for _ in range(3):
                try:
                    three_context_list[idx].append(context_list[real_idx])
                    real_idx += 1
                except:
                    break
            idx += 1
        
        context = {
            "picture_list": three_context_list,
        }

        return render(request, 'select.html', context=context)


def gallery(request):
    user = User.objects.filter(pk=request.user.id)[0]
    member_pictures = MemberPicture.objects.filter(member_id=request.user.id)
    complete_member_picture = []
    count = 0
    complete_member_picture.append([])
    idx = 0
    for member_picture in member_pictures:
        if member_picture.uncolored_dot_info == '':
            if count == 3:
                complete_member_picture.append([])
                idx += 1
                count = 0
            picture = Picture.objects.filter(
                picture_id=member_picture.picture_id.picture_id)[0]
            count += 1
            complete_member_picture[idx].append(picture)
            
    context = {
        "picture": complete_member_picture
    }

    return render(request, 'gallery.html', context=context)
