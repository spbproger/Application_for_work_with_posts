from config import POST_PATH, UPLOAD_FOLDER
from exceptions import WrongTypeForImage
import json
img_format = ["tiff", "jgp", "jpeg", "png", "bmp", "gif"]

def saving_pic(picture):
    """
    Сохраняет изображение и выполняет проверку на соответствие загружаемого файла формату изображений
    """
    type_of_picture = picture.filename.split(".")[-1]
    if type_of_picture not in img_format:
        raise WrongTypeForImage(f"Выбран файл с форматом, отличным от изображения: {','.join(img_format)}")
    save_pic = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(save_pic)
    return save_pic


def make_new_post(posts, new_post):
    """
    Записывает новый пост в файл json
    """
    posts.append(new_post)
    with open(POST_PATH, "w", encoding="UTF_8") as file:
        json.dump(posts, file)

