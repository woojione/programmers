#문자열로 주어진 URL 주소 정보로부터 도메인 이름을 반환하는 프로그램을 구현하세요.

#ex1) domain_name("http://github.com/carbonfive/raygun")== "github"

#ex2) domain_name("www.google.com")=="google"

#ex3) domain_name("https://www.netflix.com")=="netflix"

# def domain_name(string):
#     n=string.find('.com') #찾는 단어의 위치 알려줌
#     if '.com' in string:
#         a=slice(0,n,1) #0부터 n번째(.com 전까지)까지만 잘라서 추출
#         b=string[a].split('/')[2]  #string[a]=http://github 
#         return b

def domain_name(string):
    if "/" in string:
        n=string.split("/")[2] #github.com #www.netflix.com
        if "www" in n:
            a=n.split(".")[1]
            return a
        else:
            a=n.split(".")[0]
            return a
    else:
        b=string.split(".")[1]
        return b

string=str(input("domain: "))
print(domain_name(string))