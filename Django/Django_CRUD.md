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

### 1. `CREATE` 게시글 생성

> 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 1-1. HTML Form 제공

```
http://localhost:8000/articles/new/ => view 함수에서 처리하자.
```

- `urls.py`에 `new` 함수 추가

```
urlpatterns = [
	path('new/', views.new, name='new'),
]
```

- url로 전송하기 위해 action에서 지정!

```
<form action="/articles/create/">
```

📍url을 변수로 관리하기 위해 다음과 같이 form을 입력한다.

```
<!-- form : 사용자에게 양식을 제공하고 값을 받아서(input : name, value) 서버에 전송(action)-->
<form action="{% url 'articles:create' %}"> 📍url을 변수로 관리 
```

수많은 정보가 `request`라는 객체에 있고 우리는 그것을 꺼내서 쓸 수 있다.



#### 1-2. 입력받은 데이터 처리

```
http://localhost:8000/articles/create/
```

- 게시글 DB에 생성하고 index 페이지로 redirect

```
from django.shortcuts import render, redirect
from .models import Article

def create(request):
    # DB에 저장하는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index') # 목록 페이지로 돌아가!
```

`from .models import Article` : 지금 내 앱 `models.py`에 있는 `Article` 클래스를 import 하겠다!



### 2. `READ` :게시글 목록

> DB에서 게시글을 가져와서, template(ex: `index.html`)에 전달

```
# 요청 정보를 받아서
def index(request):
    # 게시글을 가져와서
    articles = Article.objects.all() 
    # template에 전달한다.
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)
```

![image-20221023155835486](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221023155835486.png)

`articles` : 모든 article을 의미

`articles = Article.objects.order_by('-pk') ` : 게시판의 글 목록은 최신글이 위에 보이기 때문에 '-pk'로 내림차순 정렬

![A basic HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/http_request.png)

#### 2-1. [🔎 HTTP 요청 메서드](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

> Article 객체를 **조회** ➡️ `GET`
>
> Article 객체를 form을 통해 **제출** ➡️ `POST`

```
<form action="{% url 'articles:create' %}" method="POST">
    <label for="title">제목 : </label>
    <input type="text" name="title" id="title">
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <input type="submit" value="글쓰기">
</form>
```

`<form>`에서 `POST` 메서드를 사용하였다면 다음과 같이 `csrf_token`을 사용해야 한다!

> CSRF (Cross Site Request Forgeries)
>
> : 웹 해킹 기법의 하나로 Django는 이를 방지하기 위한 기능을 기본적으로 제공.
>
> Django에서 HTTP POST, PUT, DELETE을 할 경우 이 태그를 넣어 주어야 한다.

```
<form method="post">
{% csrf_token %}
```

⚠️ POST 메서드를 사용하였으니, view에서도 POST 메서드를 통해 DB에 저장한다.

```
def create(request):
	title = request.GET.get('title')
```

위처럼 GET 메서드를 사용하게 되면, `None`이 되어

`NOT NULL constraint failed: articles_article.title` 에러가 발생한다.

![image-20221023165156859](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221023165156859.png)

`POST` : 메일 작성, 평점 등록 등 



#### 2-2. Modelform

DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 Django의 모델(DB)과 매우 밀접한 관계를 갖는다.

- 사용자로부터 값을 받아 **DB에 저장**하여 활용하기 때문
- 즉, 모델에 정의한 **필드**의 구성 및 종류에 따라 HTML Form이 결정됨

📍 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 **유효성 검증**이 반드시 필요하며 이는 서버 사이드에서 반드시 처리해야 함.

**❓ [Modelform을 사용하는 이유](https://eneun.tistory.com/21)**

- 폼을 위한 HTML을 작성할 필요가 없음
- 데이터 유효성 검사를 자동으로
- 올바르지 않은 데이터를 입력했을 경우 에러메시지와 함께 사용자에게 알려줌
- 재사용 가능

**❓ [Form vs Modelform](https://wayhome25.github.io/django/2017/05/06/django-form/)**

- Form (일반 폼) : 직접 필드 정의, 위젯 설정이 필요

- Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성



- articles에 `forms.py` 생성 ➡️ `new.html`에 있는 form을 대체

```
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']
        # fields = '__all__' 모든 필드
```

- `views.py`를 다음과 같이 수정한다.

```
from .forms import ArticleForm

def new(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

> `new.html`
>
> : `{{ article_form.as_p}}`  ➡️ `forms.py` article_form에 정의한 title, content에 해당하는 HTML 코드를 자동으로 생성 (p 태그로 출력)

- 기존에 작성한 label(제목, 내용)은 주석 처리!

```
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p}}
    
    <!-- <label for="title">제목 : </label>
    <input type="text" name="title" id="title">
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea> -->
    
    <input type="submit" value="글쓰기">
</form>
```

📍**유효성 검사**

```
def new(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def create(request):
    # DB에 저장하는 로직
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # ...
    # ...
    # Article.objects.create(title=title, content=content, ..., ...,)
    # 다음 한 줄의 코드로 대체할 수 있음
    
    article_form = ArticleForm(request.POST)
    if article_form.is_valid():
        article_form.save()
        return redirect('articles:index') # 목록 페이지로 돌아가!
    else:
        context = {
        'article_form': article_form
        }
        return render(request, 'articles/new.html', context=context)
```

new와 create 함수 코드가 매우 비슷하다.

➡️ 같은 함수에서 처리하자 ➡️ 같은 URL에서 처리 

```
new 함수는 주석 처리

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index') # 목록 페이지로 돌아가!
    else:
        article_form = ArticleForm()
    # 들여쓰기 하면 return 값이 없어서 오류!
    context = {
    'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
    
```

 기존에 `new` URL을 쓰고 있는 것을 `create`로 바꾼다.

`index.html` : `<a href="{% url 'articles:create' %}">글쓰기</a>`

`urls.py` : 주석처리 `path('new/', views.new, name='new')`



> ArticleForm(request.POST) : POST로 요청 보내진 것



### 3. `DETAIL` : 상세보기

> 특정한 글을 본다.

DB에 있는 `id`값을 URL에 넣어야 한다.

```
http://127.0.0.1:8000/articles/<int:pk>/
```

- `urls.py`에 경로 설정

```
urlpatterns = [
   
    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
]
```

- `views.py`에 `detail` 함수 정의

```
def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

- `detail.html` 생성

```
<h1>{{ article.pk }}번 게시글</h1>
<h6>{{ article.created_at }} | {{ article.updated_at }}</h6>
<p>{{ article.content }}</p>
```

- `index.html`에서 a 태그로 url 추가

```
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
```



### 4️⃣ `UPDATE` : 수정하기

> 특정한 글을 수정한다.  ➡️ 사용자에게 수정할 수 있는 양식을 제공(GET), 특정한 글을 수정(POST)

```
http://127.0.0.1:8000/articles/<int:pk>/update/
```

- `urls.py`에 경로 설정

```
urlpatterns = [
   
    # http://127.0.0.1:8000/articles/1/update/ : 1번글
    # http://127.0.0.1:8000/articles/3/update/ : 3번글
    path('<int:pk>/update/', views.update, name='update'),
]
```

- `detail.html`에서 a 태그로 수정하기 버튼 생성

```
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
```

- `views.py`에 `update` 함수 정의

```
def update(request, pk):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```

- `update.html` 생성 후 form 태그 만든다.

 ⚠️ action, method

```
<h1>글 수정하기</h1>

<form action="" method='POST'>
    {{ article_form.as_p }}
    <input type="submit" value="수정하기">
</form>
```

위 로직대로 수정하면 빈 화면에서 새로 작성하는 것과 같음 ➡️ 이전에 쓴 글을 가져와서 수정!

- `update`함수를 수정❗객체를 넘겨준다.

```
article = Article.objects.get(pk=pk)
    article_form = ArticleForm(instance=article)
```

`article_form` : 기존의 인스턴스의 값을 가진 상태



🧐 이제 수정하기를 누르면 ?

글 작성했을 때와 마찬가지로 **CSRF 검증**에 실패하게 됨!

- `update.html` 에서 form 태그 안에 `csrf_token`

```
<form action="" method='POST'>
    {% csrf_token %}
    {{ article_form.as_p}}
    <input type="submit" value="수정하기">
</form>
```

- 유효성 검사 

```
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POSt : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            # 유효성 검사 통과하면 상세보기 페이지로
            return redirect('articles:detail', article.pk)
    else: # 유효성 검사 통과하지 않으면 context부터 오류메시지가 담긴 article_form 렌더링
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```

🧐 이제 수정하기를 누르면 ?

❗save를 하지 않았기 때문에 수정이 안 되고 있다.

❗instance를 지정하지 않아 새로운 글이 생성된다.

`views.py` 의`update` 함수 수정

```
if request.method == 'POST':
        # POSt : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
```

`views.py`에서 `CREATE`와 `UPDATE`는 instance를 지정하는 것 빼고는 동일하다.

### 5️⃣ `DELETE` : 삭제하기

> 특정한 글을 삭제한다.

```
http://127.0.0.1:8000/articles/<int:pk>/delete/
```

- `urls.py`에 경로 설정

```
urlpatterns =[
	path('<int:pk>/delete/', views.delete, name='delete'),
]
```

- `views.py`에 함수 정의

```
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```



### References

- [가상환경](https://medium.com/@psychet_learn/python-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-a87fc6e4d12b)
- [Model](https://tutorial.djangogirls.org/ko/django_models/)

