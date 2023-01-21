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
    print(website)