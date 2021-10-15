from flask import flash
from final_project_app.config.MySQLConnection import connectToMySQL
from final_project_app.models.Language import Language
from final_project_app.models.Framework import Framework
from final_project_app.models.User import User


class Developer(User):
    def __init__(self, id_user, user_type, firstname, lastname, email, address, city, state, password, biography="", isHired="0"):
        super().__init__(id_user, user_type, firstname,
                         lastname, email, address, city, state, password)
        self.biography = biography
        self.isHired = isHired
        self.ListOfLanguages = []
        self.ListOfFrameworks = []


######################################################################
#          Getting all Developers from DataBase                      #
######################################################################

    @classmethod
    def get_all_developers(cls):
        query = "SELECT * FROM users WHERE user_type=1;"
        results = connectToMySQL("final_project_db").query_db(query)
        developers = []
        for developer in developers:

            developers.append(
                Developer(developer['id'], developer['user_type'], developer['firstname'], developer['lastname'], developer['email'], developer['address'], developer['city'], developer['state'], developer['password'], developer['created_at'], developer['updated_at'], developer['biography'], developer['isHired']))

        return developers

######################################################################
#          Inserting Developers in Database, table Users             #
######################################################################

    @classmethod
    def add_developer(cls, newDeveloper): #ok
        query = "INSERT INTO users(user_type, firstname, lastname, email, address, city, state, password, biography, isHired, created_at, updated_at) VALUES(%(user_type)s, %(firstname)s, %(lastname)s, %(email)s, %(address)s, %(city)s, %(state)s, %(password)s, %(biography)s, %(isHired)s, %(created_at)s, %(updated_at)s);"

        data = {
            "user_type": newDeveloper.user_type,
            "firstname": newDeveloper.firstname,
            "lastname": newDeveloper.lastname,
            "email": newDeveloper.email,
            "address": newDeveloper.address,
            "city": newDeveloper.city,
            "state": newDeveloper.state,
            "password": newDeveloper.password,
            "biography": "",
            "isHired": 0,
            "created_at": newDeveloper.created_at,
            "updated_at": newDeveloper.updated_at

        }

        result = connectToMySQL("final_project_db").query_db(query, data)
        return result

    @classmethod
    def get_all_languages_of_developer(cls, id_user):
        query = "SELECT * FROM languages_developer AS ld JOIN users AS u ON ld.id_user = u.id_user JOIN languages AS l ON ld.id_language = l.id_language WHERE u.id_user=%(id_user)s;"
        data = {
            "id_user": id_user
        }
        results = connectToMySQL("final_project_db").query_db(query, data)

        if results:
            newDev = Developer(results[0]['id_user'], results[0]['user_type'], results[0]['firstname'], results[0]['lastname'], results[0]['email'],
                               results[0]['address'], results[0]['city'], results[0]['state'], results[0]['password'], results[0]['biography'], results[0]['isHired'])

            for language in results:

                newDev.ListOfLanguages.append(
                    Language(language['id_language'], language['lang_name']))

            return newDev
        else:
            return results

    @classmethod
    def get_list_of_developers(cls):
        query = "SELECT * FROM languages_developer AS ld JOIN users AS u ON ld.id_user = u.id_user JOIN languages AS l ON ld.id_language = l.id_language;"

        results = connectToMySQL("final_project_db").query_db(query)

        developers = []

        for row in results:
            index = findUserInArray(developers, row['id_user'])

            if index == -1:

                newDev = Developer(row['id_user'], row['user_type'], row['firstname'], row['lastname'], row['email'],
                                   row['address'], row['city'], row['state'], row['password'], row['biography'], row['isHired'])

                newDev.ListOfLanguages.append(
                    Language(row['id_language'], row['lang_name']))
                developers.append(newDev)

            else:
                developers[index].ListOfLanguages.append(
                    Language(row['id_language'], row['lang_name']))

        return developers

    @classmethod
    def get_all_frameworks_of_developer(cls, id_user):
        query = "SELECT * FROM framework_developer AS fd JOIN users AS u ON fd.id_user = u.id_user JOIN frameworks AS f ON fd.id_framework = f.id_framework WHERE u.id_user=%(id_user)s;"
        data = {
            "id_user": id_user
        }
        results = connectToMySQL("final_project_db").query_db(query, data)

        if results:
            newDev = Developer(results[0]['id_user'], results[0]['user_type'], results[0]['firstname'], results[0]['lastname'], results[0]['email'],
                               results[0]['address'], results[0]['city'], results[0]['state'], results[0]['password'], results[0]['biography'], results[0]['isHired'])

            for framework in results:

                newDev.ListOfFrameworks.append(
                    Framework(framework['id_framework'], framework['frame_name']))

            return newDev
        else:
            return results

    @classmethod
    def update_developer(cls, data):
        query = " UPDATE users SET biography=%(biography)s WHERE id_user=%(id_developer)s;"
        results = connectToMySQL("final_project_db").query_db(query, data)

        delete_langDev(data)

        insert_langDev(data)

        return results

    @classmethod
    def update_devFrameworks(cls, data):

        delete_langFrameworks(data)

        insert_langFrameworks(data)


def delete_langDev(data):

    query = " DELETE FROM languages_developer WHERE id_user=%(id_developer)s;"
    results = connectToMySQL("final_project_db").query_db(query, data)


def insert_langDev(data):

    for i in range(0, len(data['languages'])):

        datos = {

            "id_language": data['languages'][i],
            "id_developer": data['id_developer']

        }

        query = "INSERT INTO languages_developer(id_language, id_user) VALUES(%(id_language)s, %(id_developer)s);"
        results = connectToMySQL("final_project_db").query_db(query, datos)


def delete_langFrameworks(data):

    query = " DELETE FROM framework_developer WHERE id_user=%(id_developer)s;"
    results = connectToMySQL("final_project_db").query_db(query, data)


def insert_langFrameworks(data):

    for i in range(0, len(data['frameworks'])):

        datos = {

            "id_framework": data['frameworks'][i],
            "id_developer": data['id_developer']

        }

        query = "INSERT INTO framework_developer(id_framework, id_user) VALUES(%(id_framework)s, %(id_developer)s);"
        results = connectToMySQL("final_project_db").query_db(query, datos)


def findUserInArray(users, id):
    for i in range(0, len(users), 1):
        if users[i].id_user == id:
            return i
    return -1
