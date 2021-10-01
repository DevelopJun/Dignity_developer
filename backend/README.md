Django 개발 문서  
=============
 ![image](https://user-images.githubusercontent.com/63999666/135593754-bd1f4f82-f270-42d0-96b5-3ad125b3c828.png)
![image](https://user-images.githubusercontent.com/63999666/135593766-7ab566b3-850e-481a-b925-58badf1ef401.png)

 

> - mangae.py : app을 생성, 서버 실행, 데이터베이스 관한 작업을 하는 파일
> - settings.py : 프로젝트의 환경 및 구성에 대한 설정이 있는 파일, app 생성 후 이곳에서
등록하고, static file, database 설정 이곳에서 
> - Setting.py 파일의 내용은 크게 다음 부분으로 나눌 수 있다.
1. 데이터 베이스 설정 2. 템플릿 설정 3. 지역 시각 및 다국어 설정 4. 애플리케이션의 등록, 5. 정적 파일 설정, 6, 미디어 파일 설정 
> - urls.py -> 유저가 접근하는 웹 사이트의 url과 view의 연결을 지정해준다. 
> - __init__.py 빈파일
> - asgi.py -> 웹서버, 프레임워크, 앱을 연결해주는 역할(Asynchronous SErever Gateway Interface)
> - wsgi.py -> 웹서버 Django 간의 통신 역할을 한다.

* * *
파이썬 가상환경 -> activate 실행은 git bash에서 안되고, cmd에서만 된다. 
앱은 독립되어 쓸 수 있는 모듈, 앱은 다른 프로젝트에 플러그인 할 수 있는 재사용 가능한 라이브러리,

* * *

URL과 뷰 
> - Django-amdin startapp [app이름]->Python manage.py runserver , urls.py에서 urlpatterns에서 url routing -> views.py
 모델
> - Python manage.py makemigrations -> sqlmigrate로 실제 어떤 쿼리문이 실행되는 확인할 수 있다. -> python manage.py migrate
장고 관리자 

슈퍼유저 

