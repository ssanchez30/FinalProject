from flask import flash
from final_project_app.config.MySQLConnection import connectToMySQL
from final_project_app.models.User import User


class Framework():
    def __init__(self, id_framework, frame_name):
        self.id_framework = id_framework
        self.frame_name = frame_name
