# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 입출력 예 #1
# [1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.

# 입출력 예 #2
# [1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.

# 입출력 예 #3
# [1]에는 1만 있으므로 최빈값은 1입니다.

from collections import Counter #counter:배열 요소 개수, .most_common(): 각 요소 개수 딕셔너리 값으로 반환(3이 1개 => 3:1)
def solution(array):
    answer=Counter(array) #배열의 각 요소 개수 구하기 
    m=answer.most_common() #입출력 예2 -> [(1,2), (2,2)]
    if len(answer)==1: 
        return m[0][0] #[1] = return 1
    else: #[세로크기][가로크기]
        first=m[0][1] #[0][1] => 1행 (총 1줄)
        second=m[1][1] #[1][1] => 1행 1열 (총 2줄)
        if first==second: #입출력 예2 -> [1,1] == [2,2]
            return -1
        else: # 입출력 예1 -> [1] = [2] != [3,3,3] != [4]
            return m[0][0]


array=list(input("array 입력: ").split())
print("array: ",array)
print(solution(array))
