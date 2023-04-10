#머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 #1
# [149, 180, 192, 170] 중 머쓱이보다 키가 큰 사람은 180, 192, 170으로 세 명입니다.


# 1. 입력받은 키를 배열에 추가
# => [149,180,192,170,167]
# 2. 배열 오름차순 정렬
# => [149,167,170,180,192] 
# 3. 배열의 길이-추가된 키 위치-키의 개수
# => 5-1-1 =3

def solution(array, height):
    array.append(height)
    array.sort()
    answer=len(array)-array.index(height)-array.count(height)
    return answer

array=list(input("array 입력: ").split()) #.split(): 쪼개서 입력받기(공백을 기준으로 분류함)
height=input("머쓱이 키 입력:")
print("array: ",array)
print("height: ",height)
print(solution(array,height))