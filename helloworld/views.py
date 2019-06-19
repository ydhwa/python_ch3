from django.shortcuts import render

# Create your views here.


# Django는 forwarding이 아니라 rendering하는 개념이다.
def hello(request):
    return render(request, 'helloworld/hello.html')
