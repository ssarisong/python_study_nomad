#list_of_numbers = [1,2,3]
#first, second, third = list_of_numbers
#print(first, second, third)

from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = (soup.find_all('section', class_="jobs"))
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        #이 job post는 list의 li들
        #list 안의 코드를 실행하는 방법=>for loop를 쓰면 된다
        job_posts.pop(-1) #pop=제거, 마지막 항목을 없애고 싶으면 인덱스가 -1
        for post in job_posts:
            #anchor = <a href에서 a이고, 우리는 anchor에서 href를 찾아야해서 이렇게 함
           anchors = post.find_all('a')
           anchor = anchors[1]
           print(anchor['href'])
           company, kind, region = anchor.find_all('span', class_="company")
           #print(company, kind, region)
           #이렇게 하면 우리는 company, kind, region의 span을 얻게 됨
           title = anchor.find('span', class_='title')
           #이 과정을 통해 우리는 job의 title을 얻었음
           #title에 저장하기(title =추가)
           print(company, kind, region, title)
           print("////////////")
           print("////////////")