# CBV(class-based views)

클래스 기반 뷰는 Python 객체를 함수 대신 구현하게 해 준다.

기존에 사용하던 **function-based views**와 비교하면 다음과 같은 차이점이 있다.

- 특정 HTTP 메서드(GET, POST 등)와 관련된 코드를 조건부 분기 대신 별도의 메서드로 해결할 수 있다.

- Mixin(다중 상속)과 같은 객체 지향 기술을 사용할 수 있다.



`views.py`에서 'my_view'라는 함수가 HTTP **GET**을 처리하는 코드는 다음과 같다.

```python
from django.http import HttpResponse

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')
```



CBV에서는 다음과 같이 나타낼 수 있다.

```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
```



## Mixin 사용하기

> 믹스인이란 여러 상위 클래스의 동작과 속성을 결합하여 다중 상속 받는 것을 의미

### TemplateResponseMixin

> HTTP method를 구분해 get 함수 혹은 post 함수로 들어가게 분류해주고, template_name을 지정해주면 해당 이름이 지정한 html 파일로 보내준다.

```python
class TemplateResponseMixin:
    ...
    template_name = None
    ...
    def render_to_response(self, context, **response_kwargs):
        ...
        response_kwargs.setdefault('context_type', self.context_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
```



### SingleObjectMixin

> POST로 온 key-value의 값과 일치하는 model queryset을 가져오는 mixin

*class* `django.views.generic.detail.SingleObjectMixin`





**참고**

- https://bakjuna.tistory.com/81
- https://docs.djangoproject.com/en/3.2/
