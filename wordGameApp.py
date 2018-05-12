import random
import csv
import operator
import datetime
from random import randint
from flask import Flask, render_template, request, url_for, session


app = Flask(__name__)

replies = ['You\'re having a giraffe.', 'I don\'t think so...', 'Nice try but try,try and try again.',
           'What in the world were you thinking?', 'Get out of here!!',
           'In which galaxy dose that word belong to?', 'Holy molly... ', 'Paul say\'s no way Jerry!']


@app.route('/')
@app.route('/start')
def display_index() -> 'html':
    return render_template('index.html', title = 'Game Start')


@app.route("/paulswordgame")
def display_form() -> 'html':
    session['challange_word'] = getWord()
    global starttime
    starttime = datetime.datetime.now()
    return render_template('start.html', title = 'Let\'s Play', word = session['challange_word'])


@app.route('/paulswordgame', methods=['POST'])
def process_the_data() -> 'html':
    session['data'] = []
    session['duplist'] = []
    session['dup'] = 0
    for k, v in request.form.items():
        v = str(v).lower()
        session['data'].append(v)
        if session['data'].count(v) > 1:
            session['dup'] += 1
            session['duplist'].append(v)
    vaildwords = vaildwordlist("treeUpToLessSeven.txt", session['data'])
    vaildword_Set = set(vaildwords)
    userword_Set = set(session['data'])
    notvaild_Set = userword_Set.symmetric_difference(vaildword_Set)
    if len(notvaild_Set) == 0 and session['dup'] == 0:
        global finishtime
        finishtime = datetime.datetime.now()
        return render_template('winner.html', title = 'Well Done')
    else:
        list = []
        for x in notvaild_Set:
            r = replies[randint(0, len(replies) - 1)]
            if len(str(x)) >= 3:
                list.append(x + ': ' + r)
        return render_template('fail.html', title='Fail', theword = session['challange_word'], list = list, num = len(list), dup = session['dup'], duplist = session['duplist'])


@app.route('/leaderboard', methods=['POST'])
def leaderboard() -> 'html':
    duration = finishtime.__sub__(starttime)
    session['dataName'] = []
    for k, v in request.form.items():
        v = str(v)
        session['dataName'].append(v)
    session['username'] = session['dataName'][0]
    rankname = [str(session['username']),str(duration)]
    writefile('rank.txt',rankname)
    rank = sortfile('rank.txt')
    writesortfile('rank.txt', rank)
    rank = readtoprank('rank.txt')
    pos = finduserrank('rank.txt',str(duration),str(session['username']))
    return render_template('leaderboard.html', title='Well Done', rank = rank, username = session['username'], pos = str(pos))


def sortfile(filename):
    rank = []
    with open(filename, newline='') as file:
        line = csv.reader(file, delimiter=',')
        sort = sorted(line, key=operator.itemgetter(1))
        for eachline in sort:
            rank.append(eachline)
        file.close()
    return rank


def getWord() -> 'returns a seven or more char word':
   random_lines = random.choice(open("sevenUp.txt").readlines())
   return str(random_lines).rstrip()


def writefile(filename,rankname):
    with open(filename, 'a', newline='') as file:
        w = csv.writer(file, delimiter=',')
        w.writerow(rankname)
    file.close()


def writesortfile(filename,rank):
    with open(filename, 'w', newline='') as file:
        w = csv.writer(file, delimiter=',')
        w.writerows(rank)
    file.close()


def finduserrank(filename,duration,usename):
    pos = 1
    data = [usename,duration]
    with open(filename, 'r', newline='') as file:
        w = csv.reader(file, delimiter=',')
        for row in w:
            if data == row:
                break
            pos += 1
    file.close()
    return pos


def readtoprank(filename):
    n = 1
    topten = []
    with open(filename, 'r', newline='') as file:
        w = csv.reader(file, delimiter=',')
        for row in w:
            if n <= 10:
                topten.append(row)
                n += 1
            else:
                break
    file.close()
    return topten


def vaildwordlist(filename,data):
    vaildwords = []
    with open(filename, "r") as file:
        for word in file:
            x = word.rstrip()
            for userword in data:
                if x == str(userword).lower():
                    if len(set(str(userword).lower()).difference(session['challange_word'])) == 0:
                        vaildwords.append(str(x))
    file.close()
    return vaildwords


if __name__ == "__main__":
    app.config['SECRET_KEY'] = "YOUWILLNEVERGUESSMYSECRETKEY"
    app.run(debug = True)
