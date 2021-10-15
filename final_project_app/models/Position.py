from flask import flash
from datetime import datetime
from final_project_app.config.MySQLConnection import connectToMySQL
from final_project_app.models.User import User
from final_project_app.models.Organization import Organization


class Position():
    def __init__(self, id_position, name_position, descr_position, isClosed, id_organization):
        self.id_position = id_position
        self.name_position = name_position
        self.descr_position = descr_position
        self.isClosed = isClosed
        self.id_organization = id_organization
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.ListOfSkillsRequired = []


######################################################################
#          Inserting Positions in Database             #
######################################################################


    @classmethod
    def add_position(cls, data):
        query = " INSERT INTO  positions (name_position, descr_position, isClosed, id_organization, created_at, updated_at) VALUES(%(name_position)s, %(descr_position)s, %(isClosed)s, %(id_organization)s, %(created_at)s, %(updated_at)s);"

        results = connectToMySQL("final_project_db").query_db(query, data)

        insert_skillPosition(data, results)

        return results

######################################################################
#      Validations of the registration on new user process           #
######################################################################

    @staticmethod
    def validate_positions_fields(name_position, descr_position):
        isValid = True
        if len(name_position) < 2:
            flash("Position's name must be at least 2 characters long", "danger")
            isValid = False
        if len(descr_position) < 2:
            flash("Position's description must be at least 2 characters long", "danger")
            isValid = False

        return isValid

    @classmethod
    def get_all_positions_of_organization(cls, id_user):
        query = "SELECT * FROM positions AS p JOIN users AS U ON p.id_organization = u.id_user  WHERE u.id_user=%(id_user)s;"
        data = {
            "id_user": id_user
        }
        results = connectToMySQL("final_project_db").query_db(query, data)

        if results:
            newOrg = Organization(results[0]['id_user'], results[0]['user_type'], results[0]['org_name'], results[0]['firstname'], results[0]
                                  ['lastname'], results[0]['email'], results[0]['address'], results[0]['city'], results[0]['state'], results[0]['password'])

            for position in results:

                newOrg.ListOfPositionsCreated.append(
                    Position(position['id_position'], position['name_position'], position['descr_position'], position['isClosed'], position['id_organization']))

            return newOrg
        else:
            return results

    @classmethod
    def get_Lang_Need_Position(cls, id_position):
        query = "SELECT * FROM languages_positions WHERE id_position=%(id_position)s;"

        data = {
            "id_position": id_position
        }

        result = connectToMySQL("final_project_db").query_db(query, data)

        return result

    @classmethod
    def get_All_Positions(cls):
        query = "SELECT * FROM positions;"


        result = connectToMySQL("final_project_db").query_db(query)

        return result

    @classmethod
    def get_Detail_Position(cls, id_position):
        query = "SELECT * FROM positions WHERE id_position=%(id_position)s;"

        data={
            "id_position": id_position
        }


        result = connectToMySQL("final_project_db").query_db(query, data)

        return result




def delete_skillPosition(data):

    query = " DELETE FROM languages_positions WHERE id_position=%(id_position)s;"
    results = connectToMySQL("final_project_db").query_db(query, data)


def insert_skillPosition(data, id):

    for i in range(0, len(data['languages'])):

        datos = {

            "id_language": data['languages'][i],
            "id_position": id,

        }

        query = "INSERT INTO languages_positions(id_language, id_position) VALUES(%(id_language)s, %(id_position)s);"
        results = connectToMySQL("final_project_db").query_db(query, datos)
