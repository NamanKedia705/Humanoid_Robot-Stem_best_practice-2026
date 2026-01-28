from flask import Flask, request
from command_router import route_command

app = Flask(__name__)

@app.route("/move")
def move():
    direction = request.args.get("dir")

    if direction:
        route_command("app", direction)
        return "OK"

    return "NO COMMAND"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
