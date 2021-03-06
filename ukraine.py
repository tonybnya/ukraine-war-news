import requests
import time
import os
from pushbullet import Pushbullet
from datetime import date
from get_process import get_pid_process

NEWS_API_KEY = '933bc3cad7fe4d799845a8aa6a6bd49e'
PB_API_KEY = 'o.PjiOdgZCAGzcqnpdvSpVi6X6YaAiEmF6'
BASE_URL = 'https://newsapi.org/v2/top-headlines?q=ukraine&apiKey='


def build_url(url, key):
    return url + key


def get_news(response):
    data = response.json()
    articles = data['articles']

    for idx, article in enumerate(articles, start=1):
        news = f'''
        - {idx} -
        Date: {article['publishedAt'][:10]}
        Title: {article['title']}
        Author: {article['author']}
        Description: {article['description']}
        Link: {article['url']}
        Image: {article['urlToImage']}
        Source: {article['source']['name']}
        '''

        return news


def push_notification(msg):
    today = date.today()
    current_date = today.strftime('%B %d, %Y')
    pb = Pushbullet(PB_API_KEY)

    pb.push_note(f'War in Ukraine - {current_date}', msg)


def main():
    url = build_url(BASE_URL, NEWS_API_KEY)
    response = requests.get(url)

    if response.status_code == 200:
        news = get_news(response)
        push_notification(news)

        try:
            '''
            If the program is running using Spotlight on Mac,
            the default shell, Terminal will be open and the part of code
            is to kill the process after the job is done.
            '''
            name = 'Terminal'
            pid = get_pid_process(name)
            # Wait for 10 seconds.
            time.sleep(10)
            # Kill the process.
            os.kill(pid, 9)
        except:
            pass
    else:
        print('An error occurred!')


if __name__ == '__main__':
    main()
