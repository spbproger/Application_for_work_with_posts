from flask import Blueprint, render_template, request
import logging
from loader.utilities import saving_pic, make_new_post, WrongTypeForImage, img_format
from main.utilities import *
from config import POST_PATH

# Блюпринты для страниц, связанных с загрузкой контента для постов
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

# Файл, записывающий сообщения о действиях пользователя и ошибках программы
logging.basicConfig(filename="logger.log", level=logging.INFO)

@loader_blueprint.route("/post", methods=["GET"])
def new_post_page():
    """
     Возвращает страницу с формой для добавления нового поста
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def new_post():
    """
    Добавление загруженного изображения и текста поста в json-файл с постами,
    а также проверка на присутствие контента в формах и формата файла (изображения)
    """
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Скорее всего не загружено изображение или не добавлен текст для поста")
        return "Отсутствует часть данных"
    posts = load_data_from_json(POST_PATH)
    try:
        new_post = {"pic": saving_pic(picture), "content": content}
    except WrongTypeForImage:
        return "Выбран файл с форматом, отличным от формата изображения:" + ", ".join(img_format) + "."
    make_new_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)

