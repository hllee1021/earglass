# Git Conventions && 사용가이드

- [Git Conventions && 사용가이드](#git-conventions--사용가이드)
  - [Pull Request 가이드](#pull-request-가이드)
  - [커밋 메세지 가이드](#커밋-메세지-가이드)
    - [커밋 메세지 형태](#커밋-메세지-형태)
    - [자주 사용되는 커밋 유형](#자주-사용되는-커밋-유형)

## Pull Request 가이드

1. 현재 저장소를 자신의 계정으로 포크한다.
2. 포크한 본인 저장소를 본인 컴퓨터에 clone 한다.
3. 아래 [커밋 메세지 가이드](#커밋-메세지-가이드)에 따라서 코딩의 단위별로 커밋을 한다.
4. 본인 컴퓨터의 변경 내역을 본인 저장소로 업로드한다. (`git push`)
5. 현재 저장소에 Pull Request를 보낸다.
6. Code review를 받고 코드를 수정한다.
   - 코드를 수정하기 위해서는 그냥 Pull Request를 보낸 본인 브랜치에 commit하고 push를 하면 반영된다.
   - 현재 저장소와 충돌이 있을 경우에는 충돌을 해결해서 추가적으로 commit 하여야 한다.
7. 저장소 주인이 pull request를 merge함으로써 본인이 코딩한 변경 사항이 이 저장소에 반영된다.

## pull request 충돌 발생 시
1. git fetch [upstream] master
2. git rebase [upstream]/master
3. 충돌이 발생한 파일 확인 및 수정
4. git rebase --continue
5. git push [origin] master
6. pull request

## 커밋 메세지 가이드

### 커밋 메세지 형태

- 커밋 메세지는 다음과 같이 작성한다.

```
[커밋 유형] 동사원형으로 시작하는 문장

- 상세정보 1(선택)
- 상세정보 2(선택)
...
```

- 예시

```
[feat] complete query module

- completed user query module
- completed subtitles query module
```

```
[style] match javascript semicolon style
```

```
[test] update test scripts to apply new features
```

### 자주 사용되는 커밋 유형

- `[feat]` : 새로운 기능에 대한 커밋
- `[fix]` : 버그 수정에 대한 커밋
- `[build]` : 빌드 관련 파일 수정에 대한 커밋
- `[chore]` : 그 외 자잘한 수정에 대한 커밋
- `[docs]` : 도큐먼트에 수정에 대한 커밋
- `[style]` : 코드 문법 또는 포맷에 대한 수정에 대한 커밋
- `[refactor]` : 코드 리팩토링에 대한 커밋
- `[test]` : 테스트 코드 수정에 대한 커밋
