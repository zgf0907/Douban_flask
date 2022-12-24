from urllib import request
from flask import Flask
from flask import render_template

import sqlite3
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data :
        datalist.append(item)
    cur.close()
    con.close()

    # 当前页码，从第一页开始
    page = int(request.args.get("page", 1))
    # 每页的数量
    per_page = int(request.args.get('per_page', 25))
    paginate = data.paginate(page, per_page, error_out=False)

    return render_template('movie.html',movies = datalist,paginate=paginate)
@app.route('/score')
def score():
    score = [] # 评分
    num = [] # 每一个电影评分对应的电影数量
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data :
        score.append(str(item[0]))
        num.append(item[1])
    cur.close()
    con.close()
    return render_template('score.html',score = score ,num=num)

@app.route('/word')
def word():
    return render_template('word.html')
@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run()
