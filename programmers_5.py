# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예 #1
# [1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.

# 입출력 예 #2
# [1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.


def solution(num_list):
    answer = [0,0]
    for i in num_list: #numlist[0]=1  / numlist[1]=2 /numlist[2]=3
        answer[i%2]+=1 
        #answer[1%2=1]=>answer[0,1] /answer[2%2=0]=>answer[1,1] /answer[3%2=1]=>answer[1,2]
    return(answer)
        
num_list=list(map(int,input("정수 리스트: ").split()))
        #list타입 map여러개 int정수형 input입력 split 띄어쓰기로 구분
print(num_list)
print(solution(num_list))