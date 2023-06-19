import requests
import re
from fake_headers import Headers
import bs4


def keywords_scrapping(KEYWORDS):
    headers = Headers(browser='chrome', os='win')
    headers_data = headers.generate()

    html = requests.get('https://habr.com/ru/all/', headers=headers_data).text
    main_soup = bs4.BeautifulSoup(html, 'lxml')

    div_article_list = main_soup.find('div', class_='tm-articles-list')
    article_tags_with_ids = div_article_list.find_all('article', id=re.compile(r'\d+'))

    articles_info = []

    for WORD in KEYWORDS:
        for article_tag in article_tags_with_ids:
            published_dt = f"Дата публикации: {article_tag.find('time')['title']}"
            h2_tag = article_tag.find('h2')
            title = h2_tag.text
            link = f'https://habr.com{h2_tag.find("a")["href"]}'
            hubs_container_tag = article_tag.find('div', class_='tm-article-snippet__hubs-container').text
            preview_body_tag = article_tag.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
            if preview_body_tag is not None:
                preview_body = preview_body_tag.text
            else:
                preview_body = article_tag.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-1').text

            if WORD in title or WORD in hubs_container_tag or WORD in preview_body:
                articles_info.append(
                    {
                        'WORD': WORD,
                        'published_dt': published_dt,
                        'title': title,
                        'link': link
                    }
                )
    return articles_info
