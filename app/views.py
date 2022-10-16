from app import flask_app
from flask import render_template, request


@flask_app.route('/', methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        return render_template('shorten.html', title="Главная")
    elif request.method == "GET":
        return render_template('longer.html', title="Главная")