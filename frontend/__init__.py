from flask import Flask
from basedbinpy import Client
from frontend.config import HOST_URL

app = Flask(__name__)
client = Client(HOST_URL)

from . import routes, errors