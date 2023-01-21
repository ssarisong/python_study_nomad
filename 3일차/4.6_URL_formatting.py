websites = ( #튜플이나 리스트 만들 떄는 복수로 사용(s)
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

for website in websites:
    #if website.startswith("https://") #https://로 시작하는 리스트 찾기
        #print("good to go")
    #else:
        #print("we have to fix it")
    
    #https://가 없는 리스트에 https:// 추가
    if not website.startswith("https://"):
        print("have to fix")
        website = f"https://{website}" #f"" = 변수안에 list 넣기
    print(website)