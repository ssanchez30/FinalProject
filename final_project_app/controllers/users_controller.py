from datetime import datetime
from flask import render_template, request, redirect, session
from flask import flash
from flask_bcrypt import Bcrypt
from final_project_app import app
from final_project_app.models.User import User

bcrypt = Bcrypt(app)

######################################################################
#          [POST] Authentication Process                             #
######################################################################


@app.route('/authentication', methods=['POST']) #ok
def validateCredentials():

    email = request.form['logEmail']
    developerPassword = request.form['logPass']

    if User.validate_info_login(email, developerPassword):

        result = User.get_user_to_validate(email)

        if len(result) == 1:
            encryptedPassword = result[0]['password']

            if bcrypt.check_password_hash(encryptedPassword, developerPassword):

                session['id'] = result[0]['id_user']
                session['firstname'] = result[0]['firstname']
                session['user_type'] = result[0]['user_type']
                session['org_name'] = result[0]['org_name']

                session['email'] = email

                print("user_type: ", session['user_type'])
                print("org_name: ", session['org_name'])

                if session['user_type'] == '1':

                    return redirect('/developer/edit')
                else:
                    return redirect('/dashboard/organization')

            else:
                flash("Please check password entered!!", "danger")
                return redirect('/')

        else:
            flash("Email does not found in our database", "danger")
            return redirect('/')


    else:
        return redirect('/')


######################################################################
#                [GET] Logout system process                         #
######################################################################

@app.route('/logout', methods=['GET']) #ok
def closeSession():
    session.clear()
    responseObj = {
        'message': 'logout successfully'
    }
    flash("Logout succesfull!!", "success")
    return responseObj
