from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newapi = NewsApiClient(api_key="0c6d46cd105a4eec899d842768e0a84e")
    topheadlines = newapi.get_top_headlines(sources="al-jazeera-english")

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
        time.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        link.append(myarticles['url'])

        mylist = zip(desc, news, img, content, link, time)

    return render_template('index.html', context=mylist)


@app.route('/bbc.html')
def bbc():
    newapi = NewsApiClient(api_key="0c6d46cd105a4eec899d842768e0a84e")
    topheadlines = newapi.get_top_headlines(sources="New York Times")

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
        time.append(myarticles['"publishedAt'])

        mylist = zip(desc, news, img, time)
    return render_template('bbc.html', context=mylist)


if __name__ == "__main__":
    app.run(debug=True)