import pandas as pd
import json
import requests
import os
from base64 import b64decode
import datetime
from datetime import date
import uuid
import os


def runner():
    today = date.today()
    api_key = '11183359a2824e6b97237247a98ebcad'  # Insert your API key here

    base_url = "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy=popularity&apiKey={}&language=en"
    start_date_value = str(today - datetime.timedelta(days=1))
    end_date_value = str(today)

    df = pd.DataFrame(columns=['newsTitle', 'timestamp', 'url_source', 'content', 'source', 'author', 'urlToImage'])

    url_extractor = base_url.format('US Stock Market News', start_date_value, end_date_value, api_key)
    response = requests.get(url_extractor)
    d = response.json()

    titles_seen = set()

    for i in d['articles']:
        newsTitle = i['title']
        if newsTitle in titles_seen:
            continue

        titles_seen.add(newsTitle)
        timestamp = i['publishedAt']
        url_source = i['url']
        source = i['source']['name']
        author = i['author']
        urlToImage = i['urlToImage']
        partial_content = i['content'] or ""
        
        if len(partial_content) >= 400:
            partial_content = partial_content[:399]
        if '.' in partial_content:
            trimmed_part = partial_content[:partial_content.rindex('.')]
        else:
            trimmed_part = partial_content

        df = pd.concat([df, pd.DataFrame({
            'newsTitle': [newsTitle], 'timestamp': [timestamp], 'url_source': [url_source],
            'content': [trimmed_part], 'source': [source], 'author': [author], 'urlToImage': [urlToImage]
        })], ignore_index=True)


    # filename = str(uuid.uuid4())
    # output_file = "/home/ubuntu/{}.parquet".format(filename)
    # df1 = df.drop_duplicates()
    # df1.to_parquet(output_file)

    # return output_file
    return df
df = runner()
df.to_csv("Stock_news.csv")