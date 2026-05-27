from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

# ==================== Exercise 43 ====================
@app.route('/ex43')
def ex43():
    return "Exercise 43: index page"

# ==================== Exercise 44 ====================
@app.route('/ex44')
def ex44():
    return "Exercise 44: Hello World!"

# ==================== Exercise 45 ====================
@app.route('/ex45/user/<username>')
def ex45_user(username):
    return f"Exercise 45: User Evonne"

@app.route('/ex45/post/<int:post_id>')
def ex45_post(post_id):
    return f"Exercise 45: Post {post_id}"

# ==================== Exercise 46 ====================
@app.route('/ex46/home')
def ex46_home():
    return render_template('ex46_home.html')

# ==================== Exercise 47 ====================
@app.route('/ex47/person')
def ex47_person():
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('ex47_person.html', person=person)

@app.route('/ex47/app')
def ex47_app():
    appInfo = {
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('ex47_app.html', appInfo=appInfo, text="Python Flask !")

# ==================== Exercise 48 ====================
@app.route('/ex48', methods=['GET', 'POST'])
def ex48():
    result = None
    if request.method == 'POST':
        try:
            x = int(request.form['x'])
            result = x * 2
        except:
            result = "Error: Please enter a valid number"
    return render_template('ex48_form.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)