# emaillist

## 1. emaillist 어플리케이션 추가
### [터미널]
`python manage.py startapp emaillist`

## 2. 어플리케이션 등록 (settings.py)
```python
# Application definition

INSTALLED_APPS = [
    'emaillist',
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
templates  디렉터리에 emaillist 디렉터리를 생성한다.

## 4. Model 설정
### 4-1. Model 정의
`models.py`에서 다음과 같은 작업을 진행한다.

```python
class Emaillist(models.Model):
    first_name = models.CharField(max_length=50)        # ORM 사용
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'Emaillist({self.first_name}, {self.last_name}, {self.email})'
```

모든 클래스는 models.Model을 상속받으며, ORM을 사용하여 표현한다.

### 4-2. admin.py에 내용 추가
```python
from emaillist.models import Emaillist

# Register your models here.
admin.site.register(Emaillist)

```

### 4-3. migrations 이름의 DDL Python 모듈을 생성
`python manage.py makemigrations`

`/emaillist/migrations/`에서 제대로 생성되었는지 확인한다.

### 4-4. 물리 DB와 스키마 동기화 작업을 한다.
`python manage.py migrate`

**모델이 변화할 때마다 4-3, 4-4 작업은 반드시 해줘야 문제가 발생하지 않는다.**

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
