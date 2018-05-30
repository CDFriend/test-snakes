import bottle
from bsapi.models import *

from path import *

app = bottle.app()


@app.post("/start")
def start():
    return StartResponse("#FF0000")


@app.post("/move")
def move():
    request = SnakeRequest(bottle.request.json)

    board_map = make_map(request)
    d, p = dijkstra(board_map, request.you.head())

    # Find nearest food
    min_dist = np.Inf
    cx, cy = -1, -1
    for foodx, foody in request.board.food:
        if d[foody][foodx] < min_dist:
            min_dist = d[foody][foodx]
            cx, cy = foodx, foody

    path = find_path_dijkstra(cx, cy, p)
    next_move = get_next_move(request.you.head(), path)

    return MoveResponse(next_move)


if __name__ == "__main__":
    app.run(port=8080)
