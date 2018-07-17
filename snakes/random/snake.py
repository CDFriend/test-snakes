import bottle
from random import choice
from bsapi.models import *

app = bottle.app()

@app.post("/start")
def start():
    return StartResponse("#0000FF")


@app.post("/move")
def move():
    return MoveResponse(choice(['left', 'right', 'up', 'down']))


if __name__ == "__main__":
    app.run(port=8080)
