from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page'

# @app.route('/login')
# @app.get('/login')
# @app.post('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'

@app.route("/hello")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
# def hello():
    # return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    # show the profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id , the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
    
# url_for('static', filename='style.css')
# byebug
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))