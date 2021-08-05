from frontend import client
from basedbinpy.exceptions import InvalidObjectId, PasteNotFound, InvalidMimeType
from flask import abort


def get_paste(paste_id: str) -> dict:
    try:
        return client.get_paste(str(paste_id))
    except (InvalidObjectId, PasteNotFound):
        return abort(404)


def add_new_paste(text: str, name: str) -> dict:
    try:
        return client.upload_text(text, name)
    except InvalidMimeType:
        return abort(404)