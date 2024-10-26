from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    return redirect(f'https://www.google.com/search?q={query}')

if __name__ == '__main__':
    app.run(debug=True)
