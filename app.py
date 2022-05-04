from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

# Регистрация блюпринтов для работы страниц
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """
    Показ загруженных изображений из папки uploads
    """
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()

