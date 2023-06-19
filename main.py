from data import keywords_scrapping


def main():
    # Определяем список ключевых слов:
    KEYWORDS = ['разработчик', 'сервер', 'Git', 'домен']

    articles_info = keywords_scrapping(KEYWORDS)

    for item in articles_info:
        print(f"Ключевое слово: \"{item['WORD']}\" - <{item['published_dt']}> - <{item['title']}> - <{item['link']}>")


if __name__ == '__main__':
    main()
