Django 개발 문서  
=============
 ![image](https://user-images.githubusercontent.com/63999666/135593754-bd1f4f82-f270-42d0-96b5-3ad125b3c828.png)
![image](https://user-images.githubusercontent.com/63999666/135593766-7ab566b3-850e-481a-b925-58badf1ef401.png)
* * * 
> - manage.py : app을 생성, 서버 실행, 데이터베이스 관한 작업을 하는 파일
> - settings.py : 프로젝트의 환경 및 구성에 대한 설정이 있는 파일, app 생성 후 이곳에서
등록하고, static file, database 설정 이곳에서 
> - Setting.py 파일의 내용은 크게 다음 부분으로 나눌 수 있다.
1. 데이터 베이스 설정 2. 템플릿 설정 3. 지역 시각 및 다국어 설정 4. 애플리케이션의 등록, 5. 정적 파일 설정, 6, 미디어 파일 설정 
> - urls.py -> 유저가 접근하는 웹 사이트의 url과 view의 연결을 지정해준다. 
> - __init__.py 빈파일
> - asgi.py -> 웹서버, 프레임워크, 앱을 연결해주는 역할(Asynchronous SErever Gateway Interface)
> - wsgi.py -> 웹서버 Django 간의 통신 역할을 한다.

 * * * 
### Django에서 settings.py 여러 개를 분리하기 
> Django 프로젝트를 진행하다보면 여러 개발자가 한 프로젝트를 작업하게 됩니다.
 
> 또한 각 개발자분들마다 사용하던(혹은 익숙한) 데이터베이스와 환경 설정 등이 다를 수 있다. 그리고 제일 중요한 부분은 실제 배포 환경에서는 settings.py의 DEBUG가 False여야 하는데, 개발 환경에서는 True로 해놓고 작업하다가 다시 False 로 바꿔주고 서버로 올려줘야 하는 아주 귀찮은 일이 닥치게 된다. 

> 따라서 settings라는 폴더를 하나 만들어서, base.py, local.py, production.py로 변경하여 분리한다.

> 에를 들어 만약 로컬에서는 로컬의 PostgreSQL을 사용하고, 프로덕션에서는 AWS의 RDS를 사용한다면, Local.py 에선 DB HOST 부분을 Localhost로, 그리고 production.py에서는 AWS 의 RDS 주소를 사용해주면 된다. 

* * *
파이썬 가상환경 -> activate 실행은 git bash에서 안되고, cmd에서만 된다. 

앱은 독립되어 쓸 수 있는 모듈, 앱은 다른 프로젝트에 플러그인 할 수 있는 재사용 가능한 라이브러리,

* * *

URL과 뷰 
> - Django-amdin startapp [app이름]->Python manage.py runserver , urls.py에서 urlpatterns에서 url routing -> views.py
 모델
> - Python manage.py makemigrations -> sqlmigrate로 실제 어떤 쿼리문이 실행되는 확인할 수 있다. -> python manage.py migrate
장고 관리자 

* * *
## drf-yasg 를 이용한 Swagger 문서 자동화 
### Swagger? 
> API 서버를 자동으로 문서화 시켜주는 툴이다. API 주소나 각 API의 메소드를 명시해주고, query string이나 body 같은 payload 도 문서 내에서 사용 가능하게 해준다. **정리하면, API를 한꺼번에 문서화하여 볼 수 있게 하는 패키지로, API 관리에 매우 용이하다.** 
> Django 프레임워크를 사용한 경우, drf-yasg, djangorestframework 라이브러리를 이용하여 python 코드로 더욱 쉽게 문서 자동화가 가능하다는 것이다. 
> - pip install drf-yasg
> - pip install djangorestframework 
1. settings.py installed_apps 두 패키지 추가.
2. Schema_url_patterns 정의
3. urlpatterns 정의
4. API 데코레이터 추가 

* * * 
## Django Postgress (DB 연결 연동) 
### 
> - psycopg2 설치 : python과 postgreSQL 을 연동하기 위해 필요한 python 라이브러리 
> [명령어] pip install psycopg2

