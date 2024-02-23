from flask import Flask, render_template
from custom_filters import reverse, calculate_birth_year

app = Flask(__name__)

app.add_template_filter(reverse, 'reverse_name')
app.add_template_filter(calculate_birth_year, 'birth_year')

@app.route('/')
def index():
    return render_template('index.html')

class UserInfo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"{self.name}です。"

@app.route('/userlist')
def user_list():
    users = [
        'Taro', 'Jiro', 'Saburo', 'Shiro'
    ]
    return render_template('userlist.html',users=users)

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
    # login_user = user_name
    user_info = UserInfo(user_name, age)
    return render_template('home.html', user_info=user_info)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
