from flask import render_template, request
from testapp import app
from testapp.save import saver
from testapp.read import reader
from testapp.setQ import random_q
import csv
import pprint

mydict = reader()
En = []


def readLatestData():
    global mydict
    global En
    mydict = reader()
    En = []
    for word in mydict:
        En.append(word)
    print(En)


readLatestData()


@app.route('/')
def index():
    return render_template('testapp/index.html')


@app.route('/add', methods=["get"])
def addword():
    return render_template('testapp/add.html')


@app.route('/added', methods=["POST"])
def wordadded():
    datas = []
    data = request.form['data1']  # POSTされたデータを読み込む
    datas = data.split(' ')  # 英語と日本語でセパレート
    mydict[datas[0]] = datas[1]
    saver(mydict)
    readLatestData()
    return render_template('testapp/added.html')


@app.route('/check')
def checkword():
    mydict = reader()
    return render_template('testapp/check.html', mydict=mydict, En=En)


@app.route('/question', methods=["POST", "GET"])
def solveQuestions():
    maxNum = len(En)
    print(maxNum)
    return render_template('testapp/question.html', max=maxNum)


@app.route('/rand_q', methods=["POST", "GET"])
def solving():
    num = request.form.get('questionNum')
    return render_template('testapp/solving.html', num=num, dictData=mydict)


@app.route('/result', methods=["post", "GET"])
def Check_ans():
    score = int(request.form.get("CorrectCount"))
    num = int(request.form.get("questionNum"))
    accuracy = int(100*score/num)
    print(f"正解数:{score} 問題数:{num} 正答率:{accuracy}")
    return render_template('testapp/TorF.html', num=num, score=score, accuracy=accuracy)
