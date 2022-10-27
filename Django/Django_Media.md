## 미디어 파일

- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
- 유저가 업로드 한 모든 정적 파일

## 미디어 관련 필드

**📷 ImageField**

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있음
- ⚠️ 사용하려면 반드시 [**Pillow**](https://pillow.readthedocs.io/en/latest/) 라이브러리가 필요

> Pillow
>
> : Python Image Library

```python
$ pip install Pillow
```

이미지를 관리하기 위해 Pillow를 설치한다.

**🗂️ FileField**

- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 가지고 있음
  - `upload_to`
  - `storage`

### URL 설정

> MEDIA_ROOT : 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로

- django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음

  ⚠️ 실제 데이터베이스에 저장되는 것은 파일의 경로

> MEDIA_URL : MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL

- 업로드 된 파일의 주소(URL)를 만들어 주는 역할
- 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

`settings.py`

```
# Media files (user uploaded filed)

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
```

📍개발 단계에서 사용자가 업로드 한 파일 제공하기

프로젝트 폴더의 `urls.py`

```
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

사용자가 업로드 한 파일이 우리 프로젝트에 업로드 되지만, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함

## 이미지 업로드 (CREATE)

### 모델 설정

- `upload_to='images/'`

  : 실제 이미지가 저장되는 경로를 지정

- `blank=True`

  : 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정 (이미지를 선택적으로 업로드 할 수 있도록) 

`models.py`에서 다음과 같이 필드를 지정

```
class Article(models.Model):
    # models에 있는 Model을 상속 받아서 만든다.
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
```

- DB 마이그레이션

```python
$ python manage.py makemigrations
$ python manage.py migrate
```

`forms.py`에 image 필드 추가

```
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
```



### HTML 설정

`form.html`에서 게시글 작성 form enctype 속성을 지정한다.

```
<form action="" method='POST' enctype='multipart/form-data'>
</form>
```

- form 요소 - enctype(인코딩) 속성

  - `multipart/form-data` 

    : 파일/이미지 업로드 시에 반드시 사용해야 하며(전송되는 데이터의 형식을 지정)

    `<input type='file'>`을 사용할 경우에 사용

  - `application/x-www-form-urlencoded`

    : (기본값) 모든 문자 인코딩

  - `text/plain`

    : 인코딩을 하지 않은 문자 상태로 전송

    공백은 '+' 기호로 변환하지만, 특수 문자는 인코딩 하지 않음

- input 요소의 accept 속성 확인

```
<input type='file' accept='image/*'>
```

![image-20221025220400182](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221025220400182.png)

> **[Unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input/file#unique_file_type_specifiers)(고유 파일 유형 지정자)**
>
> `image/*` : 모든 이미지 파일을 

### View 설정

`views.py`

```
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index') # 목록 페이지로 돌아가!
    else:
        article_form = ArticleForm()
    # 들여쓰기 하면 return 값이 없어서 오류!
    context = {
    'article_form': article_form
    }
    return render(request, 'articles/form 	.html', context=context)
```

- 업로드한 파일은 `request.FILES` 객체로 전달됨



1️⃣ HTML form 자체에서 파일을 업로드

2️⃣ view에서 파일을 별도로 modelform에 넣어 보여줌

---

## 이미지 업로드 (READ)

### img 태그 활용

`detail.html`

```
{% if article.image %} <!-- article.image가 있으면 보여주세요 -->
	<img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
{% endif %}
```

`article.image.url` : 업로드 파일의 경로

`article.image` : 업로드 파일의 파일 이름

## 이미지 업로드 (UPDATE)

### 이미지 수정하기

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정 하는 것 은 불가능하고, 새로운 사진으로 덮어 씌우는 방식을 사용

`update.html`

```
<form action="{% url 'articles:update' article.pk %}" method='POST' enctype='multipart/form-data'>
</form>
```

`views.py`

CREATE와 마찬가지로 업로드 한 파일은 `request.FILES` 객체로 전달됨

```
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            # POST : input 값 가져와서, 검증하고, DB에 저장
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                article_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/form.html', context)
    else:
        # 작성자가 아닐 때
        # (1) 에러메시지를 던져버린다. 403 메세지
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)
```

## 이미지 Resizing

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업

- `<img>` 태그에서 직접 사이즈를 조정할 수도 있지만 (width와 height), 업로드 될 때 이미지 자체를 **resizing**하는 것을 사용해 볼 것

  📍**[django-imagekit](https://github.com/matthewwithanm/django-imagekit/)** 라이브러리 활용

  1) Pillow 설치하기
  2) `pip install django-imagekit`
  3) `settings.py` - `INSTALLED_APPS`에 'imagekit' 추가하기

`models.py`

```
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
```

- `ProcessedImageField()`의 parameter로 작성된 값들은 변경이 되더라도 다시 makemigrations를 해줄 필요없이 즉시 반영이 된다.
