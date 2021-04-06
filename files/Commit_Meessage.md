# 📃Commit Message 작성법

## 👩🏻‍🏫출제자

```bash
$ git add .
$ git commit -m '날짜_문제번호_문제이름_출제자'
$ git push origin master
```

<br>

---

## 👩🏻‍🎓스터디원 모두

```bash
# 본인 branch로 바뀌어 있나 확인

$ git add .
$ git commit -m "커밋 메세지"
$ git push origin 본인 branch로 이름
```

Commit 카테고리를 크게 3가지로 나눈다.

> C : Create

> U : Update

> D : Delete



## Type : C

본인이 푼 코드를 올릴 때 사용한다.

> **`Create 사이트_문제번호_문제이름_본인이름`**

```bash
$ git commit -m "Create BOJ_1004_알고리즘_bomin"
```

다른 풀이 방법을 더 올리고 싶다면 **`Create 사이트_문제번호_문제이름_본인이름_x`**

```bash
$ git commit -m "Create BOJ_1004_알고리즘_bomin_1"
```

```bash
$ git commit -m "Create BOJ_1004_알고리즘_bomin_2"
```



## Type : U

문제를 다시 풀었거나, 수정했을 경우 사용한다.

> **`Update 수정한 이유(짧게)`**

```bash
$ git commit -m "Update 수정한 이유"
```

어떤 부분을 어떻게 수정했는지 더 자세하게 적고 싶다면 줄을 바꾸고 내용을 작성하도록 한다.

```bash
$ git commit -m "Update 풀이 수정
이분 탐색 문제로 접근하고 풀어서 틀렸습니다를 받았지만, DP 방식으로 접근해서 문제를 풀 수 있었습니다."
```



## Type : D

파일을 삭제하는 경우 사용한다.

삭제를 진행할 경우 왜 삭제했는지 이유를 내용에 작성하도록 한다

> **`Delete 사이트_문제번호_문제이름_본인이름_삭제이유`**

```bash
$ git commit -m "Delete BOJ_1004_알고리즘_bomin
다른 문제 풀이가 올라갔습니다"
```