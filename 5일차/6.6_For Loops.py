from flask import Flask,render_template,request

app = Flask("JobScrapper")

@app.route('/') #이게 있어야만 Flask가 함수 호출
def home():
    return render_template('home.html', name="sujin")  #문자열 안에 HTML을 넣어야 함(큰 따옴표""도 상관X)

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)

app.run("127.0.0.1")