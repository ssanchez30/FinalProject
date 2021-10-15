from datetime import datetime
from flask import flash
from final_project_app.config.MySQLConnection import connectToMySQL
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^[A-Z0-9]+')


class User:
    def __init__(self, id_user, user_type, firstname, lastname, email, address, city, state, password):
        self.id_user = id_user
        self.user_type = user_type
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.city = city,
        self.state = state,
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


######################################################################
#          Getting all Users from DataBase                           #
######################################################################

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("final_project_db").query_db(query)
        users = []
        for user in users:

            users.append(
                User(user['id'], user['user_type'], user['firstname'], user['lastname'], user['email'], user['address'], user['city'], user['state'], user['password'], user['created_at'], user['updated_at']))

        return users

######################################################################
#          Validating information of a specifique user          #
######################################################################

    @classmethod
    def get_user_to_validate(cls, email): #ok
        query = "SELECT * FROM users WHERE email=%(email)s;"
        data = {
            "email": email
        }

        result = connectToMySQL("final_project_db").query_db(query, data)

        return result

######################################################################
#      Validations of the registration on new user process           #
######################################################################

    @staticmethod
    def validate_user_password(firstname, lastname, email, password, confpass): #ok
        isValid = True
        if len(firstname) < 2:
            flash("firstname must be at least 2 characters long", "danger")
            isValid = False
        if len(lastname) < 2:
            flash("lastname must be at least 2 characters long", "danger")
            isValid = False
        if not EMAIL_REGEX.match(email):
            flash("Invalid email address!", "danger")
            isValid = False
        if len(User.get_user_to_validate(email)) > 0:
            flash("Email address found in our Database!", "danger")
            isValid = False
        if len(password) < 8:
            flash("Password must be at least 8 characters long", "danger")
            isValid = False
        if not PASS_REGEX.match(password):
            flash(
                "Password should contains at least one Uppercase letter and one number", "danger")
            isValid = False
        if password != confpass:
            flash("password and confirmation dont match", "danger")
            isValid = False
        return isValid

######################################################################
#               Validation of login process                          #
######################################################################

    @staticmethod
    def validate_info_login(email, password): #ok
        isValid = True

        if not EMAIL_REGEX.match(email):
            flash("Invalid email address!", "danger")
            isValid = False
        if len(password) < 8:
            flash("Password must be at least 8 characters long", "danger")
            isValid = False

        return isValid
