from frontend import app, client, helpers
from basedbinpy.exceptions import InvalidObjectId, PasteNotFound
from flask import jsonify, render_template, abort
import requests
import json


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html", message="Not Found"), 404


@app.route("/")
def home():
    return "<h1>basedbin</h1>"


@app.route("/<paste_id>")
def get_paste(paste_id: str):
    try:
        paste = client.get_paste(str(paste_id))
    except (InvalidObjectId, PasteNotFound):
        return abort(404)
    file_name = paste["file_name"]
    datetime = helpers.local_datetime_from_iso_str(paste["upload_date"])
    date = datetime.strftime("%Y/%m/%d")
    time = datetime.strftime("%H:%M:%S")
    content = paste["file_content"]
    return render_template(
        "paste.html", file_name=file_name, date=date, time=time, content=content
    )
