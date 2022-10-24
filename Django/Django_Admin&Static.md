## Admin site

> Automatic admin interface
>
> : 관리자 페이지

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- 모델 class를 `admin.py`에 등록하고 관리
- 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

**📍 admin 계정 생성**

```python
$ python manage.py createsuperuser
```

- username과 password을 입력해 관리자 계정을 생성

❗email은 선택사항이므로 입력하지 않고 enter 가능

❗비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시해도 됨

**📍 admin site 로그인**

- http://127.0.0.1:8000/admin/ 로 접속 후 로그인

- 계정만 만든 경우 Django 관리자 화면에서 모델 클래스는 보이지 않음

**📍 admin에 모델 클래스 등록**

- 모델의 record를 보기 위해서는 `admin.py`에 등록 필요

```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

새로 고침 ➡️ 모델을 확인할 수 있다.

![image-20221024154040629](C:\Users\726jo\OneDrive\바탕 화면\TIL\Django\image-20221024154040629.png)

> admin 페이지 커스텀

```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
```

- `list_display`는 list 혹은 tuple이어야 한다.

- 하나의 필드만 보여줄 때는 `list_display = ('title',)`처럼 **,**가 있어야 한다!

![image-20221024155951719](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221024155951719.png)



## Static files

> 웹서버와 정적 파일
>
> - 웹 서버는 특정 위치(URL)에 있는 자원(resource)을 요청(HTTP request) 받아서 제공(serving)하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함
> - 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)를 제공

🧐 **정적 파일**

: 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일

➡️ 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일

ex) 웹 서버는 일반적으로 **이미지, 자바 스크립트 또는 CSS**와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함

#### 정적 파일 활용

- `setttings.py`에서 `django.contrib.staticfiles`가 `INSTALLED_APPS`에 포함

![image-20221024170655967](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221024170655967.png)

- `STATIC_URL = '/static/'`과 같이 정의
- 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드

```
{% load static %}
    <img src="{% static 'logo.png' %}" alt="">
```

- 앱의 `static` 디렉토리에 정적 파일을 저장



#### 🔎 [참고](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#collectstatic) collectstatic

```
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

- STATIC_ROOT 작성

```python
$ python manage.ly collectstatic
```

- collectstatic 명령어

> `load` : 사용자 정의 템플릿 태그 세트를 로드(load)
>
> 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 불러옴
>
> `static` : STATIC_ROOT에 저장된 정적 파일에 연결

`{% load static %}` ➡️ python에서 모듈을 import하는 것과 유사!



**bootstrap5 설치**

```python
$ pip install django-bootstrap5
```

- `settings.py` - `INSTALLED_APPS`에 'django_bootstrap5' 추가

`new.html`에 bootstrap load하기

```
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}

<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}

    {% bootstrap_form article_form %}
    {# article_form.as_p #} 
    
    <!-- <input type="submit" value="글쓰기"> -->
    {% bootstrap_button button_type='submit' content='OK' %}
```

- p 태그로 불러 온 `article_form`은 주석 처리

- input 태그 주석 처리 후, bootstrap button 불러온다.
