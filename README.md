# drf_특강.

## 6월 7일 과제1. - homework1 앱 안에 6월7일과제 폴더
1. immutable 변수, mutable 변수에는 어떤게 있는지 찾아보기 
2. postman과 django를 사용해 원하는 값 리턴해주기

## 6월 8일 과제2. - homework1 앱
1. one to one, many to many 등 다양한 속성을 가진 필드를 사용해 모델링 해보기
   - book - author(작가) : ForeignKey
   - book - genre(장르) : many to many
   - book - isbn(책고유번호) : one to one
2. 강의에서 보여드린 user / userprofile / hobby의 관계가 아닌, 어디에 어떤 관계를 사용할 수 있을지 고민해보고 만들어 보면 좋을 것 같습니다!!
3. CBV를 사용해 views.py 구성해보기
   - bookApi CBV
     - get : 저장된 book 오버젝트들을 출력
     - post : title, summary를 받아서 책 오브젝트 생성
4. custom user psermission을 활용해 내가 원하는 대로 권한 바꿔보기
   - 가입한 지 12시간이 지나야 bookapi를 사용할 수 있다. CanMakeBook 퍼미션 생성 & 적용.

## 6월 10일 과제3 - user_homework 앱에서 진행!
1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.
2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
   - BaseUserManager를 상속받는 UserCustomModel 생성.
   - create_user와 create_superuser 메소드를 가지고 있다.
   - Users 모델 생성
   - settings.py에서 AUTH_USER_MODEL = 'user_homework.Users' 등록
3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요
   - UserProfile 모델 생성
   - users를 one to one 으로 관계
4. blog라는 앱을 만든 후 settings.py에 등록해주세요
5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
   - 카테고리 모델 생성
   - name, content 를 가짐
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)
   - author 는 Users와 ForeignKey 관계
   - title 글 제목
   - category 는 Category와 many to many 관계
   - content 글 내용
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요
8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요
   - admin.site.register(Category)
   - admin.site.register(Article)
9. admin 페이지에서 사용자, 카테고리, 게시글을 자유롭게 추가해주세요
10. views.py에 username, password를 받아 로그인 할 수 있는 기능을 만들어주세요
    - user_homework.views.py 에 작성.
     
    
      def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        # 비밀번호에 해쉬를 먹이기 위한 눈물겨운 코드
        hashed_password = make_password(password)
        edit_user = Users.objects.get(username=username)
        edit_user.password = hashed_password
        edit_user.save()

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "로그인 실패! 유저정보를 확인하세요."}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)

11. views.py에 로그인 한 사용자의 정보, 게시글을 보여주는 기능을 만들어주세요
    
    
    class UserHomeworkApiView(APIView):
        def get(self, request):
            try:
                user = request.user
                print(user)
    
                print(f"유저 아이디: {user.username}")
                print(f"유저 이메일: {user.email}")
                print(f"유저 이 름: {user.fullname}")
    
                return Response({"message": '유저정보'})
            except:
                return Response({"message":'로그인 필요'})
-----
    class MakeArticle(APIView):
        permission_classes = [CanWriteArticle]
    
        def get(self, request):
            user = request.user
            articles = user.article_set.all()
            for article in articles:
                print(f'{article.title}')
            return Response({'message': "article 정보"})
---
12. views.py에 <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해주는 기능을 만들어주세요
    - 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정해주세요
    - 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 해주세요


    class CanWriteArticle(permissions.BasePermission):
        message = '가입일 기준 20분 이상 지난 사용자만 접근 가능합니다.'

    def has_permission(self, request, view):
        user = request.user

        result = bool(user and request.user.dt_created < (timezone.now() - timedelta(minutes=20)))
        return result


    class MakeArticle(APIView):
        permission_classes = [CanWriteArticle]

    def post(self, request): 
        user = request.user
    
        title = request.data.get('title', '')
        content = request.data.get('content', '')
        category = request.data.get('category', '').split(',')
    
        article = Article.objects.create(
            author=user,
            title=title,
            content=content
        )
        for i in category:
            article.category.add(i)
        return Response("{message: 게시글 생성 성공}", status=status.HTTP_200_OK)