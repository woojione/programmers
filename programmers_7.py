# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# letter은 길이가 1인 영문자입니다.
# my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
# 대문자와 소문자를 구분합니다.

# 입출력 예 #1
# "abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.

# 입출력 예 #2
# "BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.

def solution(my_string, letter):
    a=list(my_string)
    b=list(letter)
    a_sub_b = [x for x in a if x not in b]
    answer=''.join(a_sub_b) #리스트를 문자열로 변환
    return answer

my_string=str(input("문자열: "))
letter=input("문자: ")
print(solution(my_string, letter))