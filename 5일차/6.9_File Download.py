from flask import Flask,render_template,request,redirect,send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {
    'python': []
}

@app.route("/") #이게 있어야만 Flask가 함수 호출
def home():
    return render_template("home.html", name="sujin")  #문자열 안에 HTML을 넣어야 함(큰 따옴표""도 상관X)

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None: #키워드가 없으면
        return redirect("/")
    if keyword not in db: #키워드가 데이터베이스 안에 없으면
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")