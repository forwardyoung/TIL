# Django CRUD

> 🔎 Django란?
>
> : 보안이 우수하고 유지보수가 편리한 웹사이트를 신속하게 개발하는 하도록 도움을 주는 **파이썬 웹 프레임워크**
>
> **Django는 URL로 요청을 받아서 처리하고 응답을 해 준다.**
>
> ✔️ 즉, app 단위로 별도의 MTV 패턴을 가진다.

`UI(기능) ↔️ DB`

## 1️⃣ 가상환경 및 Django 설치

> 🔎 가상환경(Virtual Environments)란?
>
> : 자신이 원하는 Python 환경을 구축하기 위해 필요한 모듈만 담아 놓는 바구니 ➡️ **프로젝트마다 패키지를 별도로 관리하기 위해** 생성

### 1. 가상환경 생성 및 실행

```
$ python -m venv venv
$ source venv/Scripts/activate
(venv) 
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip install django-bootstrap5
$ pip freeze > requirements.txt
```

`pip install django-bootstrap5` : django-bootstrap을 설치한다.

`pip freeze` : 작업 환경(가상환경)에 설치되어 있는 패키지의 리스트를 모두 출력해준다.

`requirements.txt`라는 파일에  패키지 리스트들이 그대로 담겨 있기 때문에 특정 가상환경에서 *버전에 맞게*  패키지를 설치할 수 있다.

![image-20221011230315604](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221011230315604.png)

⚠️ 루트 폴더에 `.gitignore` 파일 생성 후 가상환경 폴더를 `.gitignore`로 설정한다.

[🌍참고](https://www.toptal.com/developers/gitignore/api/django)

![image-20221006144737787](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221006144737787.png)

### 3. Django 프로젝트 생성

```
$ django-admin startproject pjt .
```

- 현재 디렉토리(.)에 `pjt`라는 프로젝트를 생성한다.

```
$ python manage.py runserver
```

- 서버를 실행시켜 django 프로젝트가 제대로 동작하는지 확인

![image-20221021111052579](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221021111052579.png)

위와 같이 서버 로그를 확인할 수 있다!



### **internationalization** 및 **localization** 추가 설정

프로젝트 폴더의 `setting.py`에서 

`LANGUAGE_CODE = 'ko-kr'`

`TIME_ZONE = 'Asia/Seoul'`



## 2️⃣ 애플리케이션 생성 및 등록

> Django : 주요 기능 단위의 App 구조, App 별로 MTV를 구조를 가지는 모습
>
> `urls.py` 설정

### 1. app 생성

```
$ python manage.py startapp articles
```

⚠️ `manage.py` 파일을 통해 앱을 생성하므로, `manage.py` 파일이 존재하는 위치에서 명령어를 실행

### 2. app 등록

![image-20221007144956626](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221007144956626.png)

- `장고 프로젝트 이름/settings.py`로 이동하여 `INSTALLED_APPS`에 생성한 앱 이름을 추가한다.
- `settings.py` : 현재 Django **프로젝트의 환경 및 구성**을 설정

⚠️ 앱이 추가될 때마다 `INSTALLED_APPS`에 앱 이름을 등록해야 하며, 설치된 앱은 `apps.py`의 경로 설정을 따라간다.

⚠️ `Bootstrap5` 도 `INSTALLED_APPS`에 등록한다. 이때, 'django_bootstrap5'라고 등록하면

​	 `ModuleNotFoundError: No module named 'django_bootstrap5'`가 발생하므로 **'bootstrap5'**라고 등록하자!

### 3. urls.py 설정

> 프로젝트별로 관리하는 것이 아닌 **app 단위**의 URL 관리

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
# reviews라는 app에 있는 urls에서 관리를 하고 싶다.
```

`include('articles.urls')` **모듈 : 앱이름.urls** 의미 ➡️ `articles/urls.py`

⚠️ `urls.py`의 메세지

```
Including another URLconf

  1. Import the include() function: from django.urls import include, path

  2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
```

`urls.py` 파일은 [장고 프로젝트 이름]으로 생성한 폴더 아래에 포함되어 있다.

⚠️ 위 상태에서 바로 server를 실행시키면 articles app에 만들지 않았기 때문에 `ModuleNotFoundError`가 발생한다.

➡️ articles app에 `urls.py` 파일을 생성

```
from django.urls import path

app_name = 'articles'

urlpatterns = [
    
]
```

- app에 있는 `urls.py` 파일에서 app_name을 설정하고, `urlpatterns`라는 빈 리스트를 생성한 후 다음 단계를 밟는다.

   

#### Index

```
from django.urls import path 
from . import views

urlpatterns = [
  # http://localhost:8000/articles/
    # 위 경로로 들어오면 페이지를 처리하겠다 
    path('', views.index, name='index'),
]
# 위 주소의 articles로 들어오면 어떤 페이지를 처리하겠다! 계획을 하고 path에 view 함수를 적는다.
```

- `from . import views`를 하지 않으면 `NameError: name 'views' is not defined`가 발생한다.

```
# 요청 정보를 받아서
def index(request):

    # 페이지를 render
    return render(request, 'articles/index.html')
```

- `AttributeError: module 'articles.views' has no attribute 'index' `➡️ `views.py`에서 index라는 함수를 정의한다.	
- `index` 함수는 `요청(request)`을 넘겨받아 `render`메서드를 호출
  - 이 함수는 `render` 메서드를 호출하여 받은(return) `articles/index.html` 템플릿을 보여준다.


![image-20221021135915085](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221021135915085.png)

html file의 이름이 같다면, `settings.py`의 `INSTALLED_APPS` 순서에 따라 앞의 앱의 template이 검색되어 제공되므로

**templates 디렉토리 하위에 app 이름의 디렉토리를 만든 후** html 파일을 생성한다.



## 3️⃣ Model 정의(DB 스키마 설계)

### 1. 클래스 정의 

app에 `models.py`

```
from django.db import models

# Create your models here.
'''
게시판 기능
- 제목(20글자 이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
'''

class Article(models.Model):
    # models에 있는 Model을 상속받아서 만든다.
    title = models.CharField(max_lenth=20)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) # 자동으로 기록
```

`auto_now_add=True` : 추가될 때 자동으로 기록

`auto_now=True` : 자동으로 기록

### 2. 마이그레이션 파일 생성

```
$ python manage.py makemigrations
```

### 3. DB 반영(migrate)

```
$ python manage.py migrate
```

![image-20221021155822136](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221021155822136.png)



## 4️⃣ CRUD 기능 구현

### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리

#### 1-1. HTML Form 제공

```
http://localhost:8000/articles/new/ => view 함수에서 처리하자.
```

`urls.py`에 `new` 함수 추가

```
urlpatterns = [
	path('new/', views.new, name='new'),
]
```





---

### References

- [가상환경](https://medium.com/@psychet_learn/python-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-a87fc6e4d12b)
- 