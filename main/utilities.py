import json
from exceptions import JsonErrors

def load_data_from_json(path):
    """
    Подгружает данные постов из файла json и предупреждает об ошибке, если с файлом что-то не так
    """
    try:
        with open(path, "r", encoding="UTF-8")as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise JsonErrors

def searching_in_posts_by_substring(posts, substring):
    """
    Поиск слов в постах по совпадению с запрашиваемым словом
    """
    founded_posts = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            founded_posts.append(post)
    return founded_posts
