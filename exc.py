#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import requests, bs4

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
csv_file = open('C:\\Users\\xuqin\\Desktop\\新建文件夹 (2)\\move.csv', 'w', newline='', encoding='UTF-8')
writer = csv.writer(csv_file)
writer.writerow(['序号', '电影名', '评分', '推荐语', '链接'])
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em', class_="").text
        title = titles.find('span', class_="title").text
        score = titles.find('span', class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span', class_="inq") != None:
            comment = titles.find('span', class_="inq").text
            print(num + '.' + title + '——' + score + '\n' + '推荐语：' + comment + '\n' + url_movie)
        else:
            comment = ''
            print(num + '.' + title + '——' + score + '\n' + '\n' + url_movie)

        writer.writerow([num, title, score, comment, url_movie])
csv_file.close()
