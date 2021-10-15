from flask import flash
from final_project_app.config.MySQLConnection import connectToMySQL
from final_project_app.models.User import User


class Organization(User):
    def __init__(self, id_user, user_type, org_name, firstname, lastname, email, address, city, state, password):
        super().__init__(id_user, user_type, firstname,
                         lastname, email, address, city, state, password)
        self.org_name = org_name
        self.ListOfPositionsCreated = []
        self.devHired = []


######################################################################
#          Getting all Organizations from DataBase                   #
######################################################################

    @classmethod
    def get_all_organizations(cls):
        query = "SELECT * FROM users WHERE user_type=2;"
        results = connectToMySQL("final_project_db").query_db(query)
        organizations = []
        for organization in organizations:

            organizations.append(
                Organization(organization['id'], organization['user_type'], organization['org_name'], organization['firstname'], organization['lastname'], organization['email'], organization['address'], organization['city'], organization['state'], organization['password'], organization['created_at'], organization['updated_at']))

        return organizations

######################################################################
#          Inserting Organizations in Database, table Users          #
######################################################################

    @classmethod
    def add_organization(cls, newOrganization):
        query = "INSERT INTO users(user_type, firstname, lastname, email, address, city, state, password, org_name, created_at, updated_at) VALUES(%(user_type)s, %(firstname)s, %(lastname)s, %(email)s, %(address)s, %(city)s, %(state)s, %(password)s, %(org_name)s, %(created_at)s, %(updated_at)s);"

        data = {
            "user_type": newOrganization.user_type,
            "firstname": newOrganization.firstname,
            "lastname": newOrganization.lastname,
            "email": newOrganization.email,
            "address": newOrganization.address,
            "city": newOrganization.city,
            "state": newOrganization.state,
            "password": newOrganization.password,
            "org_name": newOrganization.org_name,
            "created_at": newOrganization.created_at,
            "updated_at": newOrganization.updated_at

        }

        result = connectToMySQL("final_project_db").query_db(query, data)
        return result
