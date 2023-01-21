from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    #무조건 class_="jobs"이렇게 _해야함
    jobs = (soup.find_all('section', class_="jobs"))
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        #이 job post는 list의 li들
        #list 안의 코드를 실행하는 방법=>for loop를 쓰면 된다
        job_posts.pop(-1) #pop=제거, 마지막 항목을 없애고 싶으면 인덱스가 -1
        for post in job_posts:
            print(post)
            print("//////////////////")
