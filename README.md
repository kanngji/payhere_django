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
