# 가상 환경 진입

- source env/Scripts/activate

# 가상 환경 나가기

- deactivate

# 장고의 모델을 이용해서 DB처리

- makemigrations: models.py에서 적용한 변경사항이나 추가된 혹은 삭제된
  사항들을 감지하여 파일로 작성
- migrate: 적용되지 않은 migrations들을 적용시키는 역학

# ORM

- ORM을 사용하면 데이터베이스의 테이블을 모델화하여 사용

# HTTP 주요 응답코드의 종류

- 오류코드 200 성공
- 오류코드 500 서버오류
- 오류코드 404 서버가 요청한 페이지를 찾을 수 없음

# 장고 템플릿 상속

- 기본틀이 되는 템플릿을 먼저 작성하고 다른 템플릿에서 그 템플릿을 상속해 사용하는 방법

# 파이썬 현재시각 가져오기

- timezone.now() 가 되지않아서
- from datetime import datetime
- create_date = datetime.now() 로 해결

# 로컬 서버 열자마자 local/cafe 로 redirect

- config urls.py

# common 회원가입 폼에서 phonenumber 정규화

- leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
- models.CharField() 로 해결
