import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

url = 'https://zabgu.ru/php/news.php?category=1&page='

response = rq.get(url + "1")
response.close()
pageRaw = bs(response.text, 'lxml')
pagesAmount = int(pageRaw.find_all('div', {'class': 'pagination_pos'})[-1].text)

newsDF = pd.DataFrame()

for pn in range (1, 5):

    response = rq.get(url + str(pn))
    response.close()

    pageRaw = bs(response.text, 'lxml')

    newsRow = pageRaw.find('div', {'id': 'tested_closed_magic'})

    p_news = pageRaw.find_all('div', {'class': 'preview_new'}, )
    p_news_end = pageRaw.find_all('div', {'class': 'preview_new_end'})

    counter = 0

    for i in range(0, len(p_news), 2):

        for j in range(i, i + 2):

            header = p_news[j].find('div', {'class': 'headline'}).text
            year = p_news[j].find('p', {'class': 'yearInTileNewsOnPageWithAllNews'}).text
            daymonth = p_news[j].find('p', {'class': 'day'}).text
            date = daymonth[0:-3] + ' ' + daymonth[-3:] + ' ' + year
            tagsRaw = p_news[j].find('div', {'class': 'markersContainer'}).find_all('a', {'class': 'marker_news'})
            tags = [tagsRaw[k].text for k in range(0, len(tagsRaw))]

            newsDF = newsDF.append({'Header': header, 'Date': date, 'Tags': tags}, True)

        header = p_news_end[counter].find('div', {'class': 'headline'}).text
        year = p_news_end[counter].find('p', {'class': 'yearInTileNewsOnPageWithAllNews'}).text
        daymonth = p_news_end[counter].find('p', {'class': 'day'}).text
        date = daymonth[0:-3] + ' ' + daymonth[-3:] + ' ' + year
        tagsRaw = p_news_end[counter].find('div', {'class': 'markersContainer'}).find_all('a', {'class': 'marker_news'})
        tags = [tagsRaw[k].text for k in range(0, len(tagsRaw))]

        newsDF = newsDF.append({'Header': header, 'Date': date, 'Tags': tags}, True)

        counter += 1

file_name = '.\data.csv'

newsDF.to_csv(file_name, sep='\t', encoding='utf-16')