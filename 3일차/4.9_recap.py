from requests import get

websites = ( #튜플이나 리스트 만들 떄는 복수로 사용(s)
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website) #if문에서 나옴
    #다시 if문 시작
    if response.status_code >= 200 or response.status_code < 300:
        results[website] = "OK"
    else:
        results[website] = "FAILED"

print(results)