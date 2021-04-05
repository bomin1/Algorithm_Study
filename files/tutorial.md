# github에 소스파일 올리는 방법 🙂

1. 소스파일명은 `BOJ_1004_문제이름.py`,  or`SWEA_1004_문제이름.py`로 변경해주세요. 
2. 터미널을 열어주세요.
3. 로컬디랙토리를 생성할곳으로 이동해주세요.
    - 예) 바탕화면에 `Algo_Study` 폴더를 만든상태입니다. 터미널 

명령어>

>> cd 디렉토리생성할위치

![1](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial1.png?raw=true)

4. 깃에서 주소를 복사해와서 Repository를 가져옵니다.

![2](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial2.png?raw=true)

5. 명령어>

>> git clone 복사한주소붙여놓기

![3](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial3.png?raw=true)

6. 상태확인하기

명령어>

>> ls

가져온 디렉토리 "IT-DA-3rd"가 보입니다.

7. 각자의 스터디폴더로 이동해주세요.

명령어>

>>cd 이동할디렉토리명

이때 IT-DA-3rd -> study -> JAVA1팀 -> Week1 까지 이동합니다.

![4](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial4.png?raw=true)


8. 각자의 소스파일을 해당 폴더에 넣어주세요.

![5](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial5.png?raw=true)

9. 이제 소스파일을 깃에 add 합니다. 

명령어>
>> git add 파일명

![6](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial6.png?raw=true)

10. commit 합니다.

각자의 소스상황에맞는 메시지를 넣어주세요 

명령어>

>>git commit -m “메시지를 입력하세요”

![7](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial7.png?raw=true)

11.master에 push 해줍니다. 

명령어>

>>git push origin master


![8](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial8.png?raw=true)


12. 각자의 깃허브에 들어가면 해당 소스파일이 올라간것을 확인할 수 있습니다.

![9](https://github.com/Rurril/IT-DA-3rd/blob/master/files/images/tutorial9.png?raw=true)