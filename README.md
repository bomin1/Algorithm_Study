๐ Algorithm Study
====================================

**ํ์ฅ : `๊น์ค๋น`**

**ํ์ : `๊ถ์๋น`,`๊น๋ณด๋ฏผ`,`๊น์๊ท `**

**์กธ์์ : `์ ์์ธ`**

<br>

---

## ๐Intro

-	๐ ๋๊ฐ? : SSAFY_๊ณ๋3๋ฐ
-	๐ ๋ฌด์์? : [๋ฐฑ์ค](https://www.acmicpc.net/) , [SWEA](https://swexpertacademy.com/main/code/problem/problemList.do) ์๊ณ ๋ฆฌ์ฆ ๋ฌธ์ 
-	โฐ ์ธ์ ? : ๋งค์ฃผ ํ์์ผ 20:00 ~ , ๋ชฉ์์ผ 20:00 ~
-	๐ ์ด๋์? : Webex / Discord
-	โ๏ธ ์ด๋ป๊ฒ? : ์ผ์ฃผ์ผ์ 4๋ฌธ์ ๋ฅผ ํ๊ณ  `์ฝ๋๋ฆฌ๋ทฐ` ํฉ๋๋ค.

<br>

---

## โโ ์คํฐ๋ ์งํ ๊ณผ์  ๋ฐ Github Push ๋ฐฉ๋ฒโโ

- [๐ฃํํ ๋ฆฌ์ผ](files/tutorial.md)์ ์งํํ๋ ๊ฒ์ผ๋ก ์คํฐ๋์ ์ฐธ์ฌํด๋ณด์ธ์!

- ์ถ์ ์

  1. ์ต์ ํ ์์์ ์ํด master์์ PULL ๋ฐ์์ค๊ธฐ

     ```bash
     $ git pull origin master
     ```

  2. README.md์ ์ฃผ์ฐจ๋ณ ๋ฌธ์  ๋งํฌ ์ถ๊ฐํ๊ธฐ

     1. ์คํฐ๋ ์ด๋ฃจ์ด์ง๋ ๋  ์์ฑ `ex) (21.01.01)`
     2. ๋ฌธ์  ์ถ๊ฐ `ex) ์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ`

  3. **``Study/week_x/์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ/input.txt``** ๋ฃ๊ธฐ

  4. master์ ์ฌ๋ ค์ฃผ๊ธฐ

     ```bash
     $ git add .
     $ git commit -m '์ถ์ ๋ ์ง_์ฌ์ดํธ_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_์ถ์ ์'
     $ git push origin master
     ```

- ์คํฐ๋์ ๋ชจ๋

  1. ๋ณธ์ธ branch๋ก ์ด๋ํ ๋ค, master์ ์๋ ์ต์  ํ์ผ PULL ๋ฐ์์ค๊ธฐ

     ```bash
     $ git switch ๋ณธ์ธbranch์ด๋ฆ
     ```

     ```bash
     $ git pull origin master
     ```

  2. ๊ฐ ์ฃผ์ฐจ๋ณ ํด๋น ๋ฌธ์  ํด๋์ ๋ค์ด๊ฐ์

     `๋ฌธ์ ์์น_๋ฌธ์ ๋ฒํธ_๋ฌธ์ ์ด๋ฆ_๋ณธ์ธ์ด๋ฆ.py`,

     `solution_๋ณธ์ธ์ด๋ฆ.md`

     ๋ ํ์ผ ์ถ๊ฐํ ๋ค, ๋ณธ์ธ branch์์ ์ปค๋ฐ ๋ฉ์ธ์ง ์ ์ง์ผ ํธ์ฌํ๊ธฐ

     ```bash
     $ git add .
     $ git commit -m '์ปค๋ฐ ๋ฉ์ธ์ง'
     $ git push origin ๋ณธ์ธbranch์ด๋ฆ
     ```
     
  3. ๋ ํฌ๋ก ๋ค์ ๋์์์ Pull requests ํญ ๋ค์ด์จ ๋ค์์ create pull request ๊น์ง๋งํ๊ธฐ

     Mergeโโโ

  4. ์คํฐ๋ ๋๋๊ณ  Merge๊ฐ ์๋ฃ๋ ํ branch ์ญ์ ํ๊ธฐ
  
     >  ๊ด๋ฆฌ์๊ฐ ์๊ฒฉ์ ์๋ ๋ธ๋์น๋ ์ญ์ ํ ์ํ์ด๋ฏ๋ก ๋ก์ปฌ  branch๋ง ์ญ์ ํด์ฃผ๊ธฐ
  
     ```bash
     $ git switch master
     
     (master)
     $ git pull origin master  
     $ git branch -d ๋ณธ์ธ branch ์ด๋ฆ
     ```

<br>

---

## ๐จ Github Commit Message

- [๐กCommit Message](files/Commit_Meessage.md)์ ์ฐธ๊ณ ํด์ ์ปค๋ฐ ๋ฉ์์ง๋ฅผ ์์ฑํด์ฃผ์ธ์!

<br>

---

## ๐ ์คํฐ๋ ์งํ

### [1์ฃผ์ฐจ](Study/Week_1)

- (21.02.16)

  [SWEA_1961_์ซ์ ๋ฐฐ์ด ํ์ ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=1961&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1954_๋ฌํฝ์ด ์ซ์](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

- (21.02.18)

  [SWEA_1216_ํ๋ฌธ2](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=1216&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_2805_๋์๋ฌผ ์ํํ๊ธฐ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=2805&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- (21.02.21)

  [SWEA_1234_๋น๋ฐ๋ฒํธ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=1234&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1974_์ค๋์ฟ  ๊ฒ์ฆ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=1974&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [2์ฃผ์ฐจ](Study/Week_2)

- (21.02.23)

  [SWEA_1289_์์ฌ์ ๋ฉ๋ชจ๋ฆฌ ๋ณต๊ตฌํ๊ธฐ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=1289&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_3499_ํผํํธ ์ํ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE&problemTitle=3499&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- (21.02.25)

  [SWEA_2007_ํจํด ๋ง๋์๊ธธ์ด](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=2007&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1225_์ํธ ์์ฑ๊ธฐ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=1225&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [3์ฃผ์ฐจ](Study/Week_3)

- (21.03.02)

  [SWEA_2814_์ต์ฅ๊ฒฝ๋ก](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=2814&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

  [SWEA_1493_์์ ์๋ก์ด์ฐ์ฐ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=1493&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

- (21.03.04)

  [BOJ_6603_๋ก๋](https://www.acmicpc.net/problem/6603)

  [BOJ_17478_์ฌ๊ทํจ์๊ฐ ๋ญ๊ฐ์](https://www.acmicpc.net/problem/17478)

- (21.03.07)

  [BOJ_1074_Z](https://www.acmicpc.net/problem/1074)

  [BOJ_11729_ํ๋ธ์ด ํ ์ด๋ ์์](https://www.acmicpc.net/problem/11729)

### [4์ฃผ์ฐจ](Study/Week_4)

- (21.03.09)

  [BOJ_2504_๊ดํธ์ ๊ฐ](https://www.acmicpc.net/problem/2504)

  [BOJ_14888_์ฐ์ฐ์ ๋ผ์๋ฃ๊ธฐ](https://www.acmicpc.net/problem/14888)

- (21.03,14)

  [SWEA_5215_ํ๋ฒ๊ฑฐ ๋ค์ด์ดํธ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=5215&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_4299_ํํ์ด์ ์ฌ๋์ ํ์ด๋ฐ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWLv6mx6htoDFAVV&categoryId=AWLv6mx6htoDFAVV&categoryType=CODE&problemTitle=4299&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [5์ฃผ์ฐจ](Study/Week_5)

- (21.03.16)

  [BOJ_17070_ํ์ดํ ์ฎ๊ธฐ๊ธฐ](https://www.acmicpc.net/problem/17070)

  [BOJ_17281_์ผ๊ตฌ](https://www.acmicpc.net/problem/17281)

### [6์ฃผ์ฐจ](Study/Week_6)

- (21.03.29)

  [SWEA_1244_์ต๋์๊ธ](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=1244&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_10580_์ ๋ด๋](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO8QBw6Qu4DFAXS&categoryId=AXO8QBw6Qu4DFAXS&categoryType=CODE&problemTitle=10580&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_1249_๋ณด๊ธ๋ก](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=1249&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

  [SWEA_2117_ํ ๋ฐฉ๋ฒ ์๋น์ค](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE&problemTitle=2117&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

### [7์ฃผ์ฐจ](Study/Week_7)

- (21.04.04)

  [BOJ_1002_ํฐ๋ ](https://www.acmicpc.net/problem/1002)

  [BOJ_9375_ํจ์์ ์ ํด๋น](https://www.acmicpc.net/problem/9375)

  [BOJ_1969_DNA](https://www.acmicpc.net/problem/1969)

  [BOJ_1475_๋ฐฉ ๋ฒํธ](https://www.acmicpc.net/problem/1475)

### [8์ฃผ์ฐจ](Study/Week_8)

- (21.04.08)

  [BOJ_1365_๊ผฌ์ธ ์ ๊น์ค](https://www.acmicpc.net/problem/1365)

  [BOJ_1764_๋ฃ๋ณด์ก](https://www.acmicpc.net/problem/1764)

### [9์ฃผ์ฐจ](Study/Week_9)

- (21.04.13)
  
  [BOJ_20364_๋ถ๋์ฐ ๋คํผ](https://www.acmicpc.net/problem/20364)
  
  [BOJ_9372_์๊ทผ์ด์ ์ฌํ](https://www.acmicpc.net/problem/9372)

- (21.04.15)

  [BOJ_13305_์ฃผ์ ์](https://www.acmicpc.net/problem/13305)

### [10์ฃผ์ฐจ](Study/Week_10)

* (21.04.20)

  [BOJ_9020_๊ณจ๋๋ฐํ์ ์ถ์ธก](https://www.acmicpc.net/problem/9020)

  [BOJ_11501_์ฃผ์](https://www.acmicpc.net/problem/11501)
  
  [BOJ_2217_๋กํ](https://www.acmicpc.net/problem/2217)

* (21.04.22)

  ๊ธฐ์ถ๋ฌธ์  3๋ฒ
### [11์ฃผ์ฐจ](Study/Week_11)

* (21.04.26)

  [BOJ_6064_์นด์๋ฌ๋ ฅ](https://www.acmicpc.net/problem/6064)

  [BOJ_1946_์ ์์ฌ์](https://www.acmicpc.net/problem/1946)
  
  [BOJ_12100_2048](https://www.acmicpc.net/problem/12100)

* (21.04.29)

  [BOJ_2644_์ด์๊ณ์ฐ](https://www.acmicpc.net/problem/2644)

### [12์ฃผ์ฐจ](Study/Week_12)

* (21.05.04)

  [BOJ_14501_ํด์ฌ](https://www.acmicpc.net/problem/14501)
  
  [BOJ_1026_๋ณด๋ฌผ](https://www.acmicpc.net/problem/1026)
  
  [BOJ_1004_์ด๋ฆฐ์์](https://www.acmicpc.net/problem/1004)

* (21.05.06)

  [BOJ_7785_ํ์ฌ์ ์๋ ์ฌ๋](https://www.acmicpc.net/problem/7785)

### [13์ฃผ์ฐจ](Study/Week_13)

* (21.05.11)

  [BOJ_14889_์คํํธ์๋งํฌ](https://www.acmicpc.net/problem/14889)

  [BOJ_14916_๊ฑฐ์ค๋ฆ๋](https://www.acmicpc.net/problem/14916)

  [BOJ_1181_๋จ์ด์ ๋ ฌ](https://www.acmicpc.net/problem/1181)

* (21.05.13)

  [BOJ_2169_๋ก๋ด ์กฐ์ขํ๊ธฐ](https://www.acmicpc.net/problem/2169)

### [14์ฃผ์ฐจ](Study/Week_14)

* (21.05.18)

  [BOJ_18187_ํ๋ฉด๋ถํ ](https://www.acmicpc.net/problem/18187)
  
  [BOJ_7576_ํ ๋งํ ](https://www.acmicpc.net/problem/7576)
  
  [BOJ_1016_์ ๊ณฑ ใดใด ์](https://www.acmicpc.net/problem/1016)
  
  

<br>

---

 ## ๐ ํ๋กํ



<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/kwonay11"><img src="https://avatars.githubusercontent.com/u/50578895?v=4" width="100px;" alt=""/><br /><sub><b>์๋น</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td align="center"><a href="https://github.com/bomin1"><img src="https://avatars.githubusercontent.com/u/73024054?v=4" width="100px;" alt=""/><br /><sub><b>๋ณด๋ฏผ</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td align="center"><a href="https://github.com/zero-bacteria"><img src="https://avatars.githubusercontent.com/u/77529078?v=4" width="100px;" alt=""/><br /><sub><b>์๊ท </b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
    <td align="center"><a href="https://github.com/kimyunbin"><img src="https://avatars.githubusercontent.com/u/50879954?v=4" width="100px;" alt=""/><br /><sub><b>์ค๋น</b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
    <td align="center"><a href="https://github.com/chanin-shim"><img src="https://avatars.githubusercontent.com/u/77476360?v=4" width="100px;" alt=""/><br /><sub><b>์ฐฌ์ธ</b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
  </tr>
</table>
</div>
