# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 #1
# "hello"의 각 문자를 세 번씩 반복한 "hhheeellllllooo"를 return 합니다.

#1.['hello']를 [h, e, l, l, o] 로 바꿈 => a=list(my_string)
#2. a[i] n번 반복해서 answer에 저장 =>

def solution(my_string, n):
    answer=''
    a=list(my_string)

    for i in a: #a[0]=h
        answer+=i*n
    return answer

my_string=str(input("문자열 입력: "))
n=int(input("정수 입력: "))
print(solution(my_string,n))
