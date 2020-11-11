# Earglass

## 서비스 소개

- 농인을 위한 자막 서비스

## 문서

- [문서 목록](docs/index.md)

## 레포지토리 구성
### API 팀
- `app.py`: Flask application 초기화 파일
- `controllers/`: 카테고리별 요청 처리 함수(controller) 모음

### DB 팀
- `services/`: 데이터베이스에서 데이터를 읽어오고 쓰는 기능 모듈
- `database/`: 데이터베이스 연결 관리 모듈
- `query/`: 참고할 수 있는 쿼리 모음

### 프론트 팀
- `templates/`: 프론트엔드 웹 페이지 모듈(flask template folder로 사용됨) 
- `publishing/`: 실제로 작동하지는 않는 껍데기뿐인 html파일 모음
