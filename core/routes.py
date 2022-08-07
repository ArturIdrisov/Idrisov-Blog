from flask import render_template, request
from core import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        with open('data.txt', 'a', encoding='utf-8') as f:
            data = {
                'title': title,
                'description': description
            }
            f.write(str(data) + '\n')
    return render_template('create_post.html')