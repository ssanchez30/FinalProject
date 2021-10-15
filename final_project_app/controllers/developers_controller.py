from flask import render_template, request, redirect, session, jsonify, json
from flask import flash
from flask_bcrypt import Bcrypt
from final_project_app import app
from final_project_app.models.Developer import Developer
from final_project_app.models.User import User
from final_project_app.models.Position import Position

bcrypt = Bcrypt(app)


######################################################################
#          [GET] Displaying Developer Register options               #
######################################################################


@app.route('/', methods=['GET'])
def displayRegisterDeveloper():

    if 'id' in session:

        id = session['id']

        return redirect('/dashboard')
    else:

        return render_template("index.html")


######################################################################
#                    [POST] adding a new developer                        #
######################################################################

@app.route("/developer/create", methods=['POST']) #ok
def addDeveloper():

    user_type = 1
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    password = request.form['password']
    confpass = request.form['confpass']

    if User.validate_user_password(firstname, lastname, email, password, confpass):

        encryptedPassword = bcrypt.generate_password_hash(password)

        newDeveloper = Developer(0, user_type, firstname, lastname, email,
                                 address, city, state, encryptedPassword)

        result = Developer.add_developer(newDeveloper)
        if result != False:
            flash("Developer added correctly!!", "success")
            return redirect('/loginDeveloper')
        else:
            flash("There was an problem adding the developer...", "danger")
            return redirect('/')

    return redirect('/loginDeveloper')


######################################################################
#            [GET] Display Login Developer option                    #
######################################################################


@app.route('/loginDeveloper', methods=['GET'])
def displayLoginDeveloper():
    return render_template("loginDeveloper.html")

######################################################################
#                    [GET] Display Developer Dashboard               #
######################################################################


@app.route('/dashboard', methods=['GET'])
def displayDeveloper():
    if 'id' in session:

        id = session['id']

        results = Developer.get_all_languages_of_developer(id)

        return render_template("dashboard.html", developer=results)
    else:
        flash("Please login first!!", "info")
        return render_template("index.html")


@app.route("/developer/edit", methods=['GET'])
def displayEditDev():
    if 'id' in session:

        id = session['id']

        results = Developer.get_all_languages_of_developer(id)

        return render_template("edit_profile.html", developer=results)
    else:
        flash("Please login first!!", "info")
        return render_template("index.html")


@app.route("/developer/editFrame", methods=['GET'])
def displayEditDevFrame():
    if 'id' in session:

        id = session['id']

        results = Developer.get_all_frameworks_of_developer(id)

        return render_template("edit_profile_frame.html", developer=results)
    else:
        flash("Please login first!!", "info")
        return render_template("index.html")


@app.route("/developer/update", methods=['PUT'])
def updateDeveloper():
    usernameBody = json.loads(request.data.decode('UTF-8'))
    print(usernameBody)

    data = {
        "biography": usernameBody['biography'],
        "id_developer": usernameBody['id_developer'],
        "languages": usernameBody['languages']
    }

    result = Developer.update_developer(data)

    return redirect('/best')


@app.route("/developer/updateFrameworks", methods=['PUT'])
def updateDevFrameworks():
    usernameBody = json.loads(request.data.decode('UTF-8'))
    print(usernameBody)

    data = {
        "id_developer": usernameBody['id_developer'],
        "frameworks": usernameBody['frameworks']
    }

    result = Developer.update_devFrameworks(data)

    return redirect('/best')



@app.route('/dashboard/developer', methods=['GET'])
def displayDashDevelop():


    if 'id' in session:

        id = session['id']

        results = Position.get_All_Positions()
      

        return render_template("dashboard_dev.html", positions=results)
    else:
        flash("Please login first!!", "info")
        return render_template("index.html")