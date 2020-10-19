# 포맷(prettier)

## Javascript 코드 포맷 방법

- 에디터마다 포맷 설정이 다르고 서로 다른 포맷은 git 변화 추적이 어렵기 때문에, prettier 를 이용하여 포맷한다.
- 어떻게 포맷할지에 대한 config file은 root 폴더의 .prettierrc에서 설정되어있다.

### 수동 포맷

- `npx prettier . --check`을 하여 현재 디렉토리 내부에 있는 파일이 올바르게 포맷되어 있는지 검사한다.
- `npx prettier . --write`를 하여 모든 파일을 포맷하여 저장한다.

## 자동 포맷

- 이 프로젝트의 `package.json`의 `scripts` 부분에 `format`이라는 명령어가 등록되어있다, 이를 통해서 다음과 같이 포맷할 수 있다

```shell
npm run format
```
