from flask import flash
from final_project_app.config.MySQLConnection import connectToMySQL
from final_project_app.models.User import User


class Language():
    def __init__(self, id_language, lang_name):
        self.id_language = id_language
        self.lang_name = lang_name
