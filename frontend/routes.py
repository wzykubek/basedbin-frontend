from frontend import app, helpers, client, pastes
from flask import jsonify, render_template
import requests
import json


@app.errorhandler(404)
def page_not_found(error):
    return render_template("__error.j2", code=404, message="Not Found"), 404


@app.route("/")
def home():
    return "<h1>basedbin</h1>"


@app.route("/<paste_id>")
def paste(paste_id: str):
    paste = pastes.get_paste(paste_id)
    file_name = paste["file_name"]
    datetime = helpers.local_datetime_from_iso_str(paste["upload_date"])
    date = datetime.strftime("%Y/%m/%d")
    time = datetime.strftime("%H:%M:%S")
    content = paste["file_content"]
    return render_template(
        "paste.j2", file_name=file_name, date=date, time=time, content=content
    )
