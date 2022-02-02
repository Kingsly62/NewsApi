from flask import Flask, render_template, request, redirect, url_for
from newsapi import NewsApiClient
API_KEY = "0c6d46cd105a4eec899d842768e0a84e"

app = Flask(__name__)


@app.route('/alja')
def index():
    newapi = NewsApiClient(API_KEY="0c6d46cd105a4eec899d842768e0a84e")
    topheadlines = newapi.get_top_headlines(
        sources="al-jazeera-english,bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    time = []
    content = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['content'])
        link.append(myarticles['url'])
        time.append(myarticles['publishedAt'])

        mylist = zip(desc, news, img, content, link, time)

    return render_template('index.html', context=mylist)


@app.route('/')
def blog():
    return render_template('blog.html')


@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    request_method = request.method
    if request.method == 'POST':
        print('---------')
        print(request.form)
        print('---------')
        return redirect(url_for('name'))

    return render_template('contact.html', request_method=request_method)


@app.route('/name')
def name():
    return render_template('submit.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/bbc')
def bbc():
    newapi = NewsApiClient(API_KEY="0c6d46cd105a4eec899d842768e0a84e")
    topheadlines = newapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])

        mylist = zip(desc, news, img, time)
    return render_template('bbc.html', context=mylist)


if __name__ == "__main__":
    app.run(debug=True)

# API_KEY="0c6d46cd105a4eec899d842768e0a84e"
