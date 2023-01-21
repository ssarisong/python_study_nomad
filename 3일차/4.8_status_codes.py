#status codes = 상태 코드
#에러 코드인지 알려줌
#숫자로 판단

from requests import get
#request = 웹사이트로 이동

websites = ( #튜플이나 리스트 만들 떄는 복수로 사용(s)
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

for website in websites:
    if not website.startswith("https://"):
        print("have to fix")
        website = f"https://{website}" #f"" = 변수안에 list 넣기
    response = get(website)
    #print(response) 
    #response [200]에서 200이 제일 좋은거
    #not found 404 같은 것은 에러 코드
    
    #오류가 안 뜨는 리스트만 OK가 뜸
    if response.status_code == 200:
        print(f"{website} is OK")
    else:
        print(f"{website} not OK")