from frontend import client
from basedbinpy.exceptions import InvalidObjectId, PasteNotFound
from flask import abort


def get_paste(paste_id: str) -> dict:
    try:
        return client.get_paste(str(paste_id))
    except (InvalidObjectId, PasteNotFound):
        return abort(404)
