from flask import Flask, render_template, request

## Flask 클래스 생성
## __name__ : 파일의 이름
app = Flask(__name__)

# @ 네비게이터 : 바로 아래에 있는 함수를 실행하겠다. 
# route(주소) : 주소에 요청을 하면 아래의 함수를 실행
# @app.route('/') : 127.0.0.1:5000/ 요청 하는 경우 아래의 함수를 실행
@app.route('/')
def index():
    return 'Hello World'


# 127.0.0.1 = localhost
# 127.0.0.1:5000/main 이라는 주소로 요청을 하는 경우 아래의 함수를 실행
@app.route('/main')
def main():
    return render_template('main.html')

# 새로운 api 생성
# localhost:5000/login 주소로 생성
@app.route("/login")
def login():
    # main.html에서 데이터를 보내는 형식
    # {id: xxxx ,  pass: xxxx }
    _id = request.args.get("id")
    _pass = request.args.get('pass')
    print(_id, _pass)
    if (_id == 'test') & (_pass == '1234'):
        return '로그인 성공'
    else:
        return '로그인 실패'
    # return _id, _pass

app.run()