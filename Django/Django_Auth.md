## Django Auth

> 🔎 회원가입 : 게시판이랑 무엇이 같고, 무엇이 다를까?

- Django authentication system(인증 시스템)은 인증과 권한(ex: 관리자, 일반회원) 부여를 함께 제공(처리)
  - user
  - 권한 및 그룹
  - 암호 해시 시스템 유저의 비밀번호 
  - Form 및 View 도구
  - 기타 적용가능한 시스템
- `settings.py`의 `INSTALLED_APPS`에서 확인 가능
  - django.contrib.auth ➡️ 유저
  - django.contrib.admin ➡️ 관리자
- Authentication (인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
  - ex) 출입문 id 카드
- Authorization (권한 ,허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정
  - ex) 권한을 받은 사람만 연구실 출입증을 가지고 드나들 수 있음

### 사전 설정

> accounts app 생성 및 등록

```
$ python manage.py startapp accounts
```

- `INSTALLED_APPS`에 account 앱 등록

> url 분리 및 매핑

- 프로젝트 폴더에 `urls.py` 만들어 url 분리

```
urlpatterns = [
	...,
	path('accounts/', include('accounts.urls'),
]
```

- `acccounts app`에 `urls.py`	


```
# app_name은 왜 쓸까?
# 우리는 기본적으로 URL을 모두 변수화해서 쓰고 있음
# Template, View에서 직접 '/accounts/' 와 같이 쓰지 않음
# app_name과 path 이름으로 

app_name= 'accounts'

urlpatterns = [

]
```


- DB에 `앱이름_모델이름`의 auth_user 테이블이 있음

  

### Django User Model

- `Custom User Model`로 대체

- Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 **커스텀 User 모델을 설정하는 것을 강력하게 권장(high recommend)**

- 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문

  ⚠️ 단, User 모델 대체 작업은 프로젝트의 **모든 migrations 혹은 첫 migrate를 실행하기 전에** 이 작업을 마쳐야 함

> `AUTH_USER_MODEL` 을 커스텀 User 모델로 설정

- 프로젝트 폴더 `settings.py`

```
# User Model
AUTH_USER_MODEL = 'accounts.User'
accounts에 있는 User가 이제부터 내가 사용할 '사용자 정보'
```

> `AbstractUser`를 상속받는 커스텀 User 클래스 작성

- accounts앱의 `models.py`

```
from django.db import models
from django.contrib.auth.models import AbstractUser

# 원래는 class User(models.MOdel)을 직접 상속하여 만들었으나
# AbstractUser를 그대로 상속받는다.
Class User(AbstractUser):
	pass
```

```
$ python manage.py makemigrations
$ python manage.py migrate
```

> admin 계정 생성
>
> : username과 password를 입력해 관리자 계정을 생성
>
> (email은 선택사항)

```
python manage.py createsuperuser
# accounts_user에 데이터가 저장됨
```

> `admin.py`에 커스텀 User 모델을 등

- 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
- accounts 앱의 `admin.py`

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

---

### ⚠️ 데이터베이스 초기화(실습용)

- 프로젝트 중간일 경우, 데이터베이스 초기화 후 마이그레이션
- `migrations` 파일 삭제
  - `migrations` 폴더 및 `__init__.py`는 삭제하지 않음
  - 번호가 붙은 파일만 삭제

- `db.sqlite3` 삭제
- migrations 진행 및 `django-extensions`설치, `INSTALLED_APPS`에 **django_extensions **등록

```
$ python manage.py makemigrations
$ python manage.py migrate
```

```
$ pip install django-extensions
```

```
$ python manage.py shell_plus
```

```
$ pip install ipython
```

### User model 활용하기

`Article.objects.create(title='제목1, content='내용1')`

> `User.objects.create(username='bbb', password='asdf')` ❓❔
>
> 📍 password를 암호화하는 로직이 필요!

> 암호 관리

- Django에서는 기본으로 PBKDF2를 (Password-Based Key Derivation Function) 사용하여 저장
  - 단방향 해시함수를 활용

```
# User 생성
user = User.objects.create_user('john‘, ‘john@google.com’, ‘1q2w3e4r!’)

# User 비밀번호 변경
user = User.objects.get(pk=2)
User.set_password(‘new password’)
User.save()

# User 인증(비밀번호 확인)
from django.contrib.auth import authenticate

user = authenticate(username='kim', password='1234')
<User: kim> # 비밀번호가 일치하면 User 객체를 보여준다.
```

### 회원가입 기능 구현

- accounts 앱의 `urls.py`

```
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('signup/', views.signup, name='signup'),
]
```

- accounts 앱의 `views.py`

```
def signup(request):
	return render(request, 'accounts/signup.html')
```

- accounts앱 - templates 폴더 - accounts 폴더 - `signup.html`

```
{% extends 'base.html' %}
{% load django_bootstrap5 %} # bootstrap 적용

{% block body %}
{{ form.as_p}} # bootstrap 코드로 바꿔도 됨

{% endblock body %}
```

- 회원가입은 User와 연결된 **modelform**이 필요

- accounts 앱의 `views.py`

```
from django.contrib.auth.forms import UserCreationFrom

def signup(request):
	form = UserCreationForm()
	context = {
		'form': form
	}
	return render(request, 'accounts/signup.html', context)
```

> POST 요청 처리

- accounts 앱의 `views.py`

```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationFrom

def signup(request):
	if request.method == 'POST':
		form = UserCreationFrom(request.POST)
		if form.is_valid():
			form.save()
			return redirect('articles:index')
	else:
		form = UserCreationForm()
	context = {
		'form': form
	}
	return render(request, 'accounts/signup.html', context)
```

> 기존 UserCreationForm을 상속받아 User 모델 재정의

- accounts 앱에 `forms.py` 파일 생성

```
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationFrom(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', )
```

✔️ Django에서 User 클래스는 커스텀을 통해 변경 가능하여, 직접 참조하는 대신 `get_user_model()`을 사용할 것을 권장함

- account 앱의 `admin.py`

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model # user에서 get_user_model로 

admin.site.register(get_user_model, UserAdmin)
```

- accounts 앱의 `forms.py` 

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationFrom(UserCreationForm):

	class Meta:
		model = get_user_model()
		fields = ('username', )
```

---

원래는 `class ArticleFrom(forms.Modelform):` 과 같이 직접 상속하여 만들었으나, 

이미 만들어진 폼(`UsercreationForm` )을 바탕으로 상속받아 내가 커스텀하여 만들었다.

`class CustomUserCreationFrom(UserCreationForm):`



`class Article(models.Model):` 직접 상속받아 만들었으나,

`class User(AbstractUser):` django 내부에 있는 어느정도 만들어진 model을 상속받아 만들었다.
