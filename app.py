from flask import Flask, render_template
from data import Articles

app = Flask(__name__)
#creating an instance of the imported flask class

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articleListView():
    return render_template('articeListView.html', articles = Articles)

@app.route('/article/string:<articleid>/')
def articleDetailView(articleid):
    return render_template('articeDetailView.html', id=articleid)

if __name__ == '__main__':
    app.run(debug = True)
#debug is set so that we dont have to restart the local server after every change for the changes to reflect
