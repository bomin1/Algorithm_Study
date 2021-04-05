# Commit Message 작성법

Commit 카테고리를 크게 3가지로 나눈다.

> C : Create

> U : Update

> D : Delete

일반적으로 CLI를 통해서 깃에 커밋 명령어를 전달하는 데, 다음과 같다.

> ```
> git commit -m "커밋 메시지"
> ```



## Type : C

파일을 만들 때 사용한다.

> **Create 사이트_문제 번호_문제 이름**

ex) git commit -m "**Create** "

ex ) git commit -m "**Create** BOJ_1004_문제 이름.py"



## Type : U

문제를 다시 풀었거나, 수정했을 경우 사용한다.

> **Update 수정한 이유(짧게)**

ex) git commit -m "**Update** 파일 이름 수정"

ex) git commit -m "**Update** 풀이 수정"

어떤 부분을 어떻게 수정했는지 더 자세하게 적고 싶다면 줄을 바꾸고 내용을 작성하도록 한다.

ex)

```
git commit -m "Update 풀이 수정

이분 탐색 문제로 접근하고 풀어서 틀렸습니다를 받았지만, DP 방식으로 접근해서 문제를 풀 수 있었습니다."
```



## Type : D

파일을 삭제하는 경우 사용한다.

> **Delete 사이트_문제 번호_문제 이름**

ex ) git commit -m "**Delete** BOJ_1004_문제 이름.py"

삭제를 진행할 경우 왜 삭제했는지 이유를 내용에 작성하도록 한다

ex)

```
git commit -m "Update 풀이 수정

삭제 이유"
```

