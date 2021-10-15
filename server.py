from flask import Flask, render_template, request, redirect, session
from final_project_app import app
from final_project_app.controllers import users_controller, developers_controller, organizations_controller, positions_controller


if __name__ == "__main__":
    app.run(debug=True)
