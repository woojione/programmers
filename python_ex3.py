#소문자 문자열로부터 자음 서브문자의 최대합을 구하는 프로그램을 구현하세요.
#solve(문자열)함수
#입력된 문자열은 소문자이고, 문자간에 공백이 없다.
#문자열에서 모음(aeiou)은 제외한다.
#알파벳 값은 a=1, b=2, c=3, ...,z=26

#예1) solve("zodiacs")일때 반환 값은 26
#"zodiacs"에서 모음(o,ia)을 뺀 자음은 "z d cs"
#자음은 "z","d"와 "cs"이고, z=26, d=4와 cs=3+19=22를 가진다. 여기서 최대 값은 26
#반환값 26

#solve("strength")일때 반환값은 57
#자음은 "str" and "ngth"이고, 자음이 연속일때 전체 합으로 표현한다.
#"str"=19+20+18=57이고, "ngth"+14+7+20+8=49이다.



#순서도
#1.입력받은 문자열에서 모음 제거 (모음을 띄어쓰기로 대체)
#2.모음이 제거된 문자열을 소문자로 구성된 문자열로 바꾸고 / 각 알파벳을 숫자로 바꿈
#2-1. 띄어쓰기로 나눠진 소문자 문자열을 숫자로 변경
def solve(string):
    alpha=['a','e','i','o','u']
    b=[]
    for char in alpha: #1
        string=string.replace(char,' ')# z, d, cs
    #a=string.split(' ')
    print('모음제거:',string) 
    for answer in string.lower(): #알파벳을 숫자로 바꿈. 아스키코드 ord('a')=97, ord('z')=122, ord('A')=65, ord('Z')=90,  string.lower(): string에 입력받은 문자를 모두 소문자로 바꿔줌 (.upper()는 소문자를 대문자로 바꿔줌)
        t=0
        t+= ord(answer) - ord('a') + 1
        b.append(t)
    #print(b)

    j=[]
    sum=0
    for i in b:
        if i>=0:
            sum+=i
            j.append(sum)
        else:
            sum=0
    print(j)
    largest=j[0]
    for n in j: #n=0부터 b[]의 마지막까지
        if n>largest: #가장 작은값 구할땐 부호 반대
            largest=n
    return largest

string=str(input("문자열: "))
print("반환값: ",solve(string))