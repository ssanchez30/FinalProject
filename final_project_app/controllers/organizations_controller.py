from datetime import datetime
from typing import List
from flask import render_template, request, redirect, session
from flask import flash
from final_project_app.models.Developer import Developer
from final_project_app.models.Position import Position
from flask_bcrypt import Bcrypt
from final_project_app import app
from final_project_app.models.Organization import Organization
from final_project_app.models.User import User

bcrypt = Bcrypt(app)


######################################################################
#          [GET] Display Organization Register options                 #
######################################################################

@app.route('/add/organization', methods=['GET'])
def displayFrmRegOrg():
    return render_template('org_signup.html')


######################################################################
#                    [POST] adding a new organization                #
######################################################################

@app.route("/organization/create", methods=['POST'])
def addOrganization():

    user_type = 2
    org_name = request.form['orgName']
    firstname = request.form['orgFirstname']
    lastname = request.form['orgLastname']
    email = request.form['orgEmail']
    address = request.form['orgAddress']
    city = request.form['orgCity']
    state = request.form['orgState']
    password = request.form['password']
    confpass = request.form['confpass']

    if User.validate_user_password(firstname, lastname, email, password, confpass):

        encryptedPassword = bcrypt.generate_password_hash(password)

        newOrganization = Organization(0, user_type, org_name, firstname, lastname, email,
                                       address, city, state, encryptedPassword)

        result = Organization.add_organization(newOrganization)
        if result != False:
            flash("Organization added correctly!!", "success")
            return redirect('/loginOrganization')
        else:
            flash("There was an problem adding the organization...", "danger")
            return redirect('/add/organization')

    return redirect('/loginOrganization')

######################################################################
#            [GET] Display Login Organization option                 #
######################################################################


@app.route('/loginOrganization', methods=['GET'])
def displayLoginOrganization():
    return render_template("loginOrg.html")

######################################################################
#                [GET] Display Organizations Dashboard               #
######################################################################


@app.route('/dashboard/organization', methods=['GET'])
def displayAllOrganizations():
    if 'id' in session:

        id = session['id']

        results = Position.get_all_positions_of_organization(id)
        developers = Developer.get_list_of_developers()

        return render_template("dashboard_org.html", org=results, developers=developers)
    else:
        flash("Please login first!!", "info")
        return render_template("index.html")


@app.route('/positions/add', methods=['GET'])
def displayPositions():
    return render_template('positionAdd.html')


@app.route('/bestFitPosition/<id>/<position>', methods=['GET'])
def displayBestFitPosition(id, position):
    context = {
        "id_position": id,
        "position": position
    }

    id_lang_requirements = []
    id_lang_skills = []
    listaNotas = []

    ListDevelopers = Developer.get_list_of_developers()
    PositionRequirements = Position.get_Lang_Need_Position(id)

    for i in range(0, len(PositionRequirements)):
        id_lang_skills.append(PositionRequirements[i]['id_language'])

    for j in range(0, len(ListDevelopers)):

        nota = 0
        for k in range(0, len(ListDevelopers[j].ListOfLanguages)):

            if ListDevelopers[j].ListOfLanguages[k].id_language in id_lang_skills:
                nota += 1

        usuarioNota = {
            "user_id": ListDevelopers[j].id_user,
            "nota": nota*20
        }
        listaNotas.append(usuarioNota)

    return render_template('bestFitPosition.html', developers=ListDevelopers, position=context, notas=listaNotas)


@app.route('/dashboard/frameworks', methods=['GET'])
def displayDashboardFrameworks():
    return render_template('dashboardFrame.html')


@app.route('/email/<id_position>/<position>/<name>/<lastname>', methods=['GET'])
def sendInvitation(id_position, position, name, lastname):

    flash(f'Email sent. Invitation to participate for {name} {lastname} to the position {position}', "success")
    return redirect(f'/bestFitPosition/{id_position}/{position}')
