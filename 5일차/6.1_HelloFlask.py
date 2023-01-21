from flask import Flask

app = Flask("JobScrapper")

@app.route("/") #이게 있어야만 Flask가 함수 호출
def home():
    return 'Hey there!'

app.run("0.0.0.0")