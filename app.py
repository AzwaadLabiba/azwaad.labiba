from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='About')

@app.route('/education')
@app.route('/education.html')
def education():
    return render_template('education.html', title='Education')

@app.route('/experience')
@app.route('/experience.html')
def experience():
    return render_template('experience.html', title='Experience')

@app.route('/publications')
@app.route('/publications.html')
def publications():
    return render_template('publications.html', title='Publications')

@app.route('/achievements')
@app.route('/achievements.html')
def achievements():
    return render_template('achievements.html', title='Achievements')

if __name__ == '__main__':
    app.run(debug=True, port=8000)