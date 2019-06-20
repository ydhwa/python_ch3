from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from emaillist.models import Emaillist


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')
    data = {'emaillist': emaillist}
    return render(request, 'emaillist/index.html', data)


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    # =@ResponseBody
    # return HttpResponse(f'{emaillist.first_name} : {emaiillist.last_name} : {emaillist.email}')

    # insert 후 반드시 redirect 시켜줘야 한다.
    return HttpResponseRedirect('/emaillist')
