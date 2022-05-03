from flask import Blueprint, render_template, request
import logging
from main.utilities import *
from config import POST_PATH
from exceptions import *

# Блюпринты для главной страницы
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

# Файл, записывающий сообщения о действиях пользователя и ошибках программы
logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    """
    Главная страница
    """
    logging.info("Открыта главная страница")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    """
    Страница отображающая информацию в постах по запросу
    """
    s = request.args.get("s", "")
    logging.info("Начат поиск")
    try:
        posts = load_data_from_json(POST_PATH)
    except JsonErrors:
        return "Не удается открыть файл, содержащий посты"
    founded_posts = searching_in_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=founded_posts, s=s)
