from datetime import date, datetime
from flask import render_template, request, redirect, session, jsonify, json
from flask import flash
from final_project_app import app
from final_project_app.models.Developer import Developer
from final_project_app.models.User import User
from final_project_app.models.Position import Position


@app.route("/add/position", methods=['GET'])
def displayPositionAdd():

    return render_template('positionAdd.html')


@app.route('/position/PositionView/<id>', methods=['GET'])
def displayViewPosition(id):

    id_lang_skills =[]

    detail_position = Position.get_Detail_Position(id)
    print(detail_position)

    PositionRequirements = Position.get_Lang_Need_Position(id)

    for i in range(0, len(PositionRequirements)):
        id_lang_skills.append(PositionRequirements[i]['id_language'])
    
    print(id_lang_skills)

    return render_template('positionView.html', detail=detail_position, skillsRequired=id_lang_skills)


######################################################################
#                    [POST] adding a new position                        #
######################################################################



@app.route("/position/add", methods=['POST'])
def add_position():
    usernameBody = json.loads(request.data.decode('UTF-8'))

    
    if Position.validate_positions_fields(usernameBody['namePos'], usernameBody['descriptionPos']):

        data = {
            "name_position": usernameBody['namePos'],
            "descr_position": usernameBody['descriptionPos'],
            "isClosed": 0,
            "id_organization": usernameBody['id_organization'],
            "languages": usernameBody['languages'],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        result = Position.add_position(data)

        if result != False:
            flash("Position added correctly!!", "success")

    else:
        flash("There was an problem adding the position...", "danger")

@app.route("/position/apply", methods=['GET'])
def applyJob():
    flash('Application submitted successfully!!', "success")
    return redirect('/dashboard/developer')


