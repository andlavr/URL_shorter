from flask import render_template, request, redirect

import db
from app import app
from utils import shorten


@app.route('/', methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        long_url = request.form["longUrl"]
        short_url = shorten(long_url)

        return render_template('shorten.html', title="Главная", short_url=f"{request.host}/{short_url}")
    elif request.method == "GET":
        return render_template('longer.html', title="Главная")


@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = db.get_long_by_short(short_url)
    return redirect(long_url)


app.run()
