from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


# Django는 forwarding이 아니라 rendering하는 개념이다.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')


def hello2(request, id=0):
    return HttpResponse(f'id: {id}')


def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]
    }
    return JsonResponse(jsonresult)


def counter_add(request):
    c = Counter()
    c.orderno = 1
    c.groupno = 4
    c.depth = 1
    c.save()

    c = Counter()
    c.orderno = 2
    c.groupno = 4
    c.depth = 1
    c.save()

    c = Counter()
    c.orderno = 3
    c.groupno = 4
    c.depth = 1
    c.save()

    return HttpResponse('ok')


def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value["max_groupno"] is None else value["max_groupno"] + 1
    return HttpResponse(f'max groupno: {value["max_groupno"]}')

def counter_update(request):
    # queryset
    # groupno = 1 이고 orderno >= 2 의 게시물의
    # orderno를 1씩 증가
    # __gt, __lt, __gte, __lte
    Counter.objects.filter(groupno=4).filter(orderno__gte=2).update(orderno=F('orderno') + 1)

    return HttpResponse('ok')
