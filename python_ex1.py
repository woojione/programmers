#두개의 리스트를 입력 받아 A-B를 빼는 프로그램을 구현하라 (리스트 차집합)
#예1) array_diff([1,2],[1])
#여기서 list A=[1,2]이고, list B=[1]이다.
#A-B를 통해 [2]를 반환한다.

#예2) array_diff([1,2,2,2,3],[2])일때 반환 값 [1,3]

#예3) array_diff([1,2,2],[])일때 반환 값 [1,2,2]

#예4) array_diff([],[1,2])일때 반환 값 []

def array_diff(A,B):
    answer=[x for x in A if x not in B]
    return answer

A=list(input("A 입력: ").split()) #문자 입력받고 싶으면 list(input())
B=list(input("B 입력: ").split())
print("A: ",A)
print("B: ",B)
print(array_diff(A,B))

#A=[1,2,2,2,3], B=[2]
# set(A) = {1,2,3}   set은 중복 없애줌.
# set(B) = {2}
# list(set(A)-set(B))=[1,3]