# "*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다. 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

# 입출력 예 #1
# n이 3이므로 첫째 줄에 * 1개, 둘째 줄에 * 2개, 셋째 줄에 * 3개를 출력합니다.
# *
# **
# ***

n = int(input('숫자 입력: '))
for i in range(1,n+1):
    for j in range(i):
        print('*',end='')
    print('')


#입출력 예 반전
# n = int(input('숫자 입력: '))
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end='')
#     print('')