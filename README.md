🎈 Algorithm Study
====================================

**팀장 : `김윤빈`**

**팀원 : `권예빈`,`김보민`,`김영균`**

**졸업자 : `정예울`**

<br>

---

## 🎉Intro

-	💁 누가? : SSAFY_계란3반
-	🎁 무엇을? : [백준](https://www.acmicpc.net/) , [SWEA](https://swexpertacademy.com/main/code/problem/problemList.do) 알고리즘 문제
-	⏰ 언제? : 매주 화요일 20:00 ~ , 목요일 20:00 ~
-	🏛 어디서? : Webex / Discord
-	✏️ 어떻게? : 일주일에 4문제를 풀고 `코드리뷰` 합니다.

<br>

---

## ❗❗ 스터디 진행 과정 및 Github Push 방법❗❗

- [🐣튜토리얼](files/tutorial.md)을 진행하는 것으로 스터디에 참여해보세요!

- 출제자

  1. 최신화 작업을 위해 master에서 PULL 받아오기

     ```bash
     $ git pull origin master
     ```

  2. README.md에 주차별 문제 링크 추가하기

     1. 스터디 이루어지는 날 작성 `ex) (21.01.01)`
     2. 문제 추가 `ex) 사이트_문제번호_문제이름`

  3. **``Study/week_x/사이트_문제번호_문제이름/input.txt``** 넣기

  4. master에 올려주기

     ```bash
     $ git add .
     $ git commit -m '출제날짜_사이트_문제번호_문제이름_출제자'
     $ git push origin master
     ```

- 스터디원 모두

  1. 본인 branch로 이동한 뒤, master에 있는 최신 파일 PULL 받아오기

     ```bash
     $ git switch 본인 branch 이름
     ```

     ```bash
     $ git pull origin master
     ```

  2. 각 주차별 해당 문제 폴더에 들어가서

     `문제위치_문제번호_문제이름_본인이름.py`,

     `문제위치_문제번호_문제이름_본인이름.md`

     두 파일 추가한 뒤, 본인 branch에서 커밋 메세지 잘 지켜 푸쉬하기

     ```bash
     $ git add .
     $ git commit -m '커밋 메세지'
     $ git push origin 본인 branch 이름
     ```
     
  3. 스터디 끝나고 Merge가 완료된 후 branch 삭제하기

     >  관리자가 원격에 있는 브랜치는 삭제한 상태이므로 로컬  branch만 삭제해주기

     ```bash
     $ git switch master
     
     (master)
     $ git pull origin master  
     $ git branch -d 본인 branch 이름
     ```

<br>

---

## 📨 Github Commit Message

- [💡Commit Message](files/Commit_Meessage.md)을 참고해서 커밋 메시지를 작성해주세요!

<br>

---

## 📅 스터디 진행

### [1주차](Study/Week_1)

- (21.02.16)

  [SWEA_1961_숫자 배열 회전](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=1961&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1954_달팽이 숫자](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

- (21.02.18)

  [SWEA_1216_회문2](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=1216&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_2805_농작물 수확하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=2805&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- (21.02.21)

  [SWEA_1234_비밀번호](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=1234&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1974_스도쿠 검증](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=1974&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [2주차](Study/Week_2)

- (21.02.23)

  [SWEA_1289_원재의 메모리 복구하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=1289&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_3499_퍼펙트 셔플](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE&problemTitle=3499&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- (21.02.25)

  [SWEA_2007_패턴 마디의길이](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=2007&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1225_암호 생성기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=1225&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [3주차](Study/Week_3)

- (21.03.02)

  [SWEA_2814_최장경로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=2814&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

  [SWEA_1493_수의 새로운연산](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=1493&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- (21.03.04)

  [BOJ_6603_로또](https://www.acmicpc.net/problem/6603)

  [BOJ_17478_재귀함수가 뭔가요](https://www.acmicpc.net/problem/17478)

- (21.03.07)

  [BOJ_1074_Z](https://www.acmicpc.net/problem/1074)

  [BOJ_11729_하노이 탑 이동 순서](https://www.acmicpc.net/problem/11729)

### [4주차](Study/Week_4)

- (21.03.09)

  [BOJ_2504_괄호의 값](https://www.acmicpc.net/problem/2504)

  [BOJ_14888_연산자 끼워넣기](https://www.acmicpc.net/problem/14888)

- (21.03,14)

  [SWEA_5215_햄버거 다이어트](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=5215&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_4299_태혁이의 사랑은 타이밍](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWLv6mx6htoDFAVV&categoryId=AWLv6mx6htoDFAVV&categoryType=CODE&problemTitle=4299&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [5주차](Study/Week_5)

- (21.03.16)

  [BOJ_17070_파이프 옮기기](https://www.acmicpc.net/problem/17070)

  [BOJ_17281_야구](https://www.acmicpc.net/problem/17281)

### [6주차](Study/Week_6)

- (21.03.29)

  [SWEA_1244_최대상금](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=1244&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_10580_전봇대](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO8QBw6Qu4DFAXS&categoryId=AXO8QBw6Qu4DFAXS&categoryType=CODE&problemTitle=10580&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1249_보급로](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=1249&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_2117_홈 방법 서비스](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE&problemTitle=2117&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [7주차](Study/Week_7)

- (21.04.04)

  [BOJ_1002_터렛](https://www.acmicpc.net/problem/1002)

  [BOJ_9375_패션왕 신해빈](https://www.acmicpc.net/problem/9375)

  [BOJ_1969_DNA](https://www.acmicpc.net/problem/1969)

  [BOJ_1475_방 번호](https://www.acmicpc.net/problem/1475)

### [8주차](Study/Week_8)

- (21.04.08)

  [BOJ_1365_꼬인 전깃줄](https://www.acmicpc.net/problem/1365)

  [BOJ_1764_듣보잡](https://www.acmicpc.net/problem/1764)

### [9주차](Study/Week_9)

- (21.04.13)
  
  [BOJ_20364_부동산 다툼](https://www.acmicpc.net/problem/20364)
  
  [BOJ_9372_상근이의 여행](https://www.acmicpc.net/problem/9372)

- (21.04.15)

  [BOJ_13305_주유소](https://www.acmicpc.net/problem/13305)

### [10주차](Study/Week_10)

* (21.04.20)

  [BOJ_9020_골드바흐의 추측](https://www.acmicpc.net/problem/9020)

  [BOJ_11501_주식](https://www.acmicpc.net/problem/11501)
  
  [BOJ_2217_로프](https://www.acmicpc.net/problem/2217)

* (21.04.22)

  기출문제 3번
### [11주차](Study/Week_11)

* (21.04.26)

  [BOJ_6064_카잉달력](https://www.acmicpc.net/problem/6064)

  

<br>

---

 ## 👀 프로필



<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/kwonay11"><img src="https://avatars.githubusercontent.com/u/50578895?v=4" width="100px;" alt=""/><br /><sub><b>예빈</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td align="center"><a href="https://github.com/bomin1"><img src="https://avatars.githubusercontent.com/u/73024054?v=4" width="100px;" alt=""/><br /><sub><b>보민</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td align="center"><a href="https://github.com/zero-bacteria"><img src="https://avatars.githubusercontent.com/u/77529078?v=4" width="100px;" alt=""/><br /><sub><b>영균</b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
    <td align="center"><a href="https://github.com/kimyunbin"><img src="https://avatars.githubusercontent.com/u/50879954?v=4" width="100px;" alt=""/><br /><sub><b>윤빈</b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
  </tr>
</table>
</div>

