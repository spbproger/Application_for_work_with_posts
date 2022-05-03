class JsonErrors(Exception):
    """
    Класс ошибок - оповещает об ошибке в файле json
    """
    pass

class WrongTypeForImage(Exception):
    """
    Класс ошибок - оповещает об ошибке в файле с загрузкой изображения (неверный формат)
    """
    pass