from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='About')

@app.route('/education')
def education():
    return render_template('education.html', title='Education')

@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')

@app.route('/publications')
def publications():
    return render_template('publications.html', title='Publications')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', title='Achievements')

# @app.route('/blog')
# def blog():
#     return render_template('blog.html', title='Blog')

# @app.route('/blog/<slug>')
# def blog_post(slug):
#     # In a real app, you'd fetch the post from a database
#     # For now, just render the template
#     return render_template('blog_post.html', slug=slug)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
