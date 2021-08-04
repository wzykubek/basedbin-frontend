from frontend import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    return render_template("__error.j2", code=404, message="Not Found"), 404