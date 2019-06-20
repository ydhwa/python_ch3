# helloworld

## 1. helloworld 어플리케이션 추가
### [터미널]
`python manage.py startapp helloworld`

## 2. 어플리케이션 등록 (settings.py)
```python
# Application definition

INSTALLED_APPS = [
    'helloworld',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
## 3. 어플리케이션 template 디렉터리 생성
templates  디렉터리에 helloworld 디렉터리를 생성한다.

## 4. Model 정의(생략)
내장된 DB를 사용하지 않기 때문이다.

## 5. urls.py에서 url-view의 handler 매핑
```python
import helloworld.views as helloworld_views

urlpatterns = [
    path('helloworld/', helloworld_views.hello),
    path('admin/', admin.site.urls),
]
```

## 6. views.py에서 핸들러 함수 구현(요청처리, 모델작업, 응답)
```python
def hello(request):
    return render(request, 'helloworld/hello.html')

```

## 7. 혹시 화면이 필요한 경우, 해당 template 작업 추가
