from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello_func() -> str:
    # This next line ensures the 'data' key exists before we try to use it (the first time).
    session.setdefault('data', [])
    session['data'].append(10)
    return 'Hello from my first web app.'


@app.route('/bye')
def byebye() -> str:
    # This next line ensures the 'data' key exists before we try to use it (the first time).
    session.setdefault('data', [])
    if session['data'][0] == 10:
        # do something
        pass
    return 'So long and thanks for all the fish.'


@app.route('/input/<first>/<last>')
def display_name(first: str, last: str) -> str:
    return 'Hello, ' + str(first) + ' ' + str(last)


@app.route('/showform')
def display_form() -> 'html':
    return render_template('displayform.html',
                           title='Fill in this form')


@app.route('/processform', methods=['POST'])
def process_the_data() -> str:
    data = []
    for k, v in request.form.items():
        data.append(k)
        data.append(v)
    with open('datalog.txt', 'a') as fh:
        print(data, file=fh)
    # data.append(request.form['passwd'])
    return 'Done.'


@app.route('/showpage2')
def display_page2() -> 'html':
    return render_template('showpage.html',
                           title='This is showpage2')


if __name__ == '__main__':
    app.config['SECRET_KEY'] = "YOUWILLNEVERGUESSMYSECRETKEY"
    app.run(debug=True)
