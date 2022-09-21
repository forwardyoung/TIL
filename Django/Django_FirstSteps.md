## 📍 How to create virtual environment in Django

- `cd(change directory)` :디렉토리를 **이동**하는 명령어
  - `~` : **🏡HOME** 디렉토리로 이동
  - `..` : **상위** 디렉토리로 이동 ➡️ `현재 위치가 /user/ming이라면 /user로 이동`
  - `.` : **현재 위치한 폴더**로 이동 (사실상 기능은 새로고침과 동일)

- `mkdir(make directory)` : **새로운 디렉토리**를 만들 때 사용하는 명령어

- `pwd(print working directory)` : 현재 디렉토리를 알려주는 명령어

  ![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/1.png)

  

- `ls(list)` : 현재 위치한 디렉토리에 있는 **내용(디렉토리, 파일) 리스트**를 출력하는 명령어

  - `-a` : 경로안의 모든 파일을 나열한다. (숨김파일도 포함)

- `source` : **스크립트 파일**을 수정한 후에 수정된 값을 바로 **적용**하기 위해 사용하는 명령어

- `rm` : 파일 삭제 명령

  

---

1. 바탕화면에서 git bash를 연다.
2. 환경 변수의 **HOME**으로 이동한다.

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/2.png)

3. 새로운 폴더(test)를 만들고 그 폴더로 이동한다.

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/3.png)

4. **파이썬 가상환경**에 django를 설치할 것이므로 **pip 설치 리스트 및 파이썬 버전을 확인**한다.

   ![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/4.png)

5. `venv` 파이썬 모듈을 이용하여 새로운 가상 환경을 생성한다. 

​	✔️`python -m venv [가상 환경]`

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/5.png)

6. 가상 환경 폴더가 생성된 것을 확인할 수 있다.

   ![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/6.png)

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/7.png)

7. `source` 명령어를 사용해 가상 환경을 작동시킨다.

​	✔️ `source [가상 환경]/Scripts/activate` **(Windows)**

​	✔️ `source [가상 환경]/bin/activate` **(MAC)**



​	프롬프트 위에 가상 환경이 작동된 것을 확인할 수 있다.

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/8.png)



​	각 가상 환경은 **고유한** 파이썬 바이너리를 가지며 자신의 사이트 디렉터리에 **독립적으로 설치된** 파이썬 패키지 집합을 가질 수 있다.



> 만일 가상환경을 **비활성화**하고 싶다면 `deactivate`를 입력한다. 프롬프트 위에 가상 환경이 보이지 않을 것이다.

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/9.png)

> 가상 환경을 지우고 싶다면 먼저 비활성화를 한 이후에 디렉토리를 지운다.
>
> 1️⃣ `deactivate`
>
> 2️⃣ `rm r venv(디렉토리 안에 있는 가상환경의 이름)`



8. Django를 설치한다.

​	✔️`python install django==3.2.13 `

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/10.png)

9. Django 프로젝트를 시작한다.

​	✔️ `django-admin startproject [프로젝트 이름] [시작 경로]`

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/11.png)

10. vs code로 현재 폴더를 열어서 확인해 본다.

​	✔️ `code .`

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/12.png)

11. Django 프로젝트가 제대로 동작하는지 확인한다.

​	✔️ `python manage.py runserver` 입력 후 브라우저에서  `http://localhost:8000/`로 이동한다.

​	([`runserver`](https://docs.djangoproject.com/ko/4.1/ref/django-admin/#django-admin-runserver) 명령은 내부 IP의 8000 번 포트로 개발 서버를 띄운다.)

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/13.png)

![](https://github.com/forwardyoung/TIL/blob/master/Django/Django_FirstSteps.assets/8000.png)



🚀🚀 **Success!!**

