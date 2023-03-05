from flask import Flask, render_template, url_for

app  = Flask(__name__)

#Lsit of dictionaries
posts = [
    {
        'author' : 'Ujjawal Singh',
        'title' : 'Blog Post 1',
        'content' : ' First post content',
        'date_posted': '05 March, 2023'
    },
    {
        'author' : 'Ujjawal Singh',
        'title' : 'Blog Post 2',
        'content' : ' To be filled',
        'date_posted': 'Date to be decided'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

if __name__ == '__main__':
    app.run(debug = True)