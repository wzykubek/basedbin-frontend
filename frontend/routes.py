from frontend import app, helpers, client, pastes
from flask import render_template, Response, request, redirect, url_for
import requests
import json


@app.route("/")
def home():
    return render_template("home.j2")


@app.route("/<paste_id>")
def paste(paste_id: str):
    paste = pastes.get_paste(paste_id)
    file_name = paste["file_name"]
    datetime = helpers.local_datetime_from_iso_str(paste["upload_date"])
    date = datetime.strftime("%Y/%m/%d")
    time = datetime.strftime("%H:%M:%S")
    content = paste["file_content"]
    return render_template(
        "paste.j2",
        file_name=file_name,
        date=date,
        time=time,
        content=content,
        paste_id=paste_id,
    )


@app.route("/raw/<paste_id>")
def raw_paste(paste_id: str):
    paste = pastes.get_paste(paste_id)
    content = paste["file_content"]
    return Response(content, mimetype="text/plain")


@app.route("/dl/<paste_id>")
def download_paste(paste_id: str):
    paste = pastes.get_paste(paste_id)
    content = paste["file_content"]
    content_type = paste["content_type"]
    file_name = paste["file_name"]
    response = Response(content, mimetype=content_type)
    response.headers["Content-Disposition"] = f'attachment; filename="{file_name}"'
    return response


@app.route("/upload")
def upload():
    return render_template("upload.j2")


@app.route("/upload_", methods=["POST"])
def upload_():
    file_name = request.form["file_name"]
    print(file_name)
    file_content = request.form["file_content"]
    print(file_content)
    status = pastes.add_new_paste(file_content, file_name)
    paste_id = status["paste_id"]
    return redirect(url_for("paste", paste_id=paste_id))