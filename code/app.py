from flask import Flask, request, render_template_string

app = Flask(__name__)

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "123456"

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        if user == CORRECT_USERNAME and passwd == CORRECT_PASSWORD:
            return f"Welcome, {user}!"
        else:
            message = "Login failed"
    return render_template_string('''
        <form method="POST">
            <input type="text" name="username" placeholder="user" />
            <input type="password" name="password" placeholder="pass" />
            <input type="submit" value="Login" />
        </form>
        <p>{{ message }}</p>
    ''', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
