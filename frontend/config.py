from os import getenv

server_hostname = getenv("SERVER_HOSTNAME")
if getenv("SERVER_PORT"):
    server_port = getenv("SERVER_PORT")
else:
    server_port = "80"

HOST_URL = f"http://{server_hostname}:{server_port}"
