## Django ORM

`filter()` : 특정 조건에 부합하는 데이터셋 가져오기

### filter() 응용

`필드명__in` = iterable 객체

```python
Product.objects.filter(id__in=[1, 3, 4])
```

iterable 객체에 해당 필드가 존재하는 데이터를 모두 반환
즉, Product의 id가 1 또는 3 또는 4 인 객체들을 리턴한다.

`office_id_id__in` = lv3_office

`필드명__contains = 조건값` 을 통해 조건값이 포함되는 데이터를 모두 가져온다.

`product_contract_date__contains` = selected_schedule_date



### `.annotate()`

'필드'를 추가



![](https://github.com/forwardyoung/TIL/blob/master/Django/ORM_1.png)

각 레코드가 전자책인지 일반책인지 추가로  출력하고자 한다.

```python
from django.db.models import Value

books = Book.objects.annotate(book_type=Value('일반책'))
ebooks = EBook.objects.annotate(book_type=Value('전자책'))

books.union(ebooks, all=True)
```



### `.values()`

쿼리셋의 값을 딕셔너리 형태로 반환



### F()

`F()`는 모델 필드의 값, 모델 필드의 변환된 값 또는 주석이 달린 열을 나타낸다. 모델 필드 값을 참조하고 실제로 데이터베이스에서 Python 메모리로 가져오지 않고도 쿼리 내에서 필드 값을 참조하고 비교할 수 있다.



### Lazy-loading

`ORM`에서 명령을 실행할 때마다 데이터베이스에 접근하여 데이터를 가져오는 것이 아닌 모든 명령처리가 끝나고 **실제 데이터를 불러와야할 때** 데이터베이스 `Query`문을 실행하는 방식

📍 N+1 Query 문제

: 외래키(`Foreign Key`)를 참조해서 데이터를 가져올 때 발생

1:1 관계인 모델이 있을 때, N+1개의 쿼리가 날아감.



### ETC

```python
JsonObject = json.loads(request.body)
```

JSON 형태로 들어오는 `request`의 `body`를 파이썬에서 읽어올 수 있도록 'JsonObject'에 담는 과정



### 에러 해결



![](https://github.com/forwardyoung/TIL/blob/master/Django/ORM_2.png)

`search_customer_information.html`에서

`<input type="hidden" name="office_id" id="office_id" value="{{customer.office_id}}">`라고 입력되어 있었음.

`office_id`는 foreign key이므로 숫자가 아닌 객체를 불러 온다.



![](https://github.com/forwardyoung/TIL/blob/master/Django/ORM_3.png)

```python
package_product = Package_product.objects.filter(package_id_id=id, is_cancel="N").order_by("package_product_type", "package_product_goout", "product_name").values()
```

product_type, product_goout, product_name 필드를 기준으로 `order_by`를 하려고 했음.

But, **Package_product** 모델에 해당 필드가 없으며, 언급된 Choices를 기준으로 정렬을 해야 한다고 알려줌.

```python
detail_product_id, detail_product_id_id, id, is_cancel, office_id, office_id_id, package_id, package_id_id, package_product_number, product_count
```
![](https://github.com/forwardyoung/TIL/blob/master/Django/ORM_4.png)

package_product 모델



![](https://github.com/forwardyoung/TIL/blob/master/Django/ORM_5.png)

`detail_product`에 해당 필드가 있는 것 확인.



```python
from django.db.models import F

package_product = Package_product.objects.filter(package_id_id=id, is_cancel="N").order_by(
        "detail_product_id__product_type", "detail_product_id__product_goout", "detail_product_id__product_name"
    ).annotate(detail_product_type=F('detail_product_id__product_type')).values()
```

`annotate()`와 `F()`expressions으로 해결
