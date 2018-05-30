import numpy as np
from heapq import heapify, heappop, heappush

MAP_EMPTY = 0
MAP_SNAKE = 1
MAP_FOOD  = 2


def make_map(snakerequest):
    world = np.full((snakerequest.board.height, snakerequest.board.width), MAP_EMPTY)

    for snake in snakerequest.board.snakes:
        for point in snake.body:
            world[point.y][point.x] = MAP_SNAKE

    for food_loc in snakerequest.board.food:
        world[food_loc.y][food_loc.x] = MAP_FOOD

    return world


def neighbors_of(x, y, map):
    """Get the neighboring cells of a given cell. Excludes cells that are
    outside the boundaries of the world.
    :param x: X coordinate of cell
    :param y: Y coordinate of cell
    :param map: Map containing the cell.
    :return Iterator of all neighboring cells.
    """
    assert 0 <= x < map.shape[1], "X coordinate must be in bounds!"
    assert 0 <= y < map.shape[0], "Y coordinate must be in bounds!"

    if x + 1 < map.shape[1] and map[y][x+1] != MAP_SNAKE:
        yield x + 1, y
    if y + 1 < map.shape[0] and map[y+1][x] != MAP_SNAKE:
        yield x, y + 1
    if x - 1 >= 0 and map[y][x-1] != MAP_SNAKE:
        yield x - 1, y
    if y - 1 >= 0 and map[y-1][x] != MAP_SNAKE:
        yield x, y - 1


def dijkstra(map, point):
    """Gets the distance "scores" and predecessor matrix from a given snake's
    head.
    :param map: World map object to map for the snake.
    :param point: Snake to calculate distances from.
    :return: d[] and p[] matrices for each point on the map.
        - p[] matrix uses integers as vertex labels: (y * width) + x
        - None indicates the head of the snake (source node).
        - -1 indicates an inaccessible point.
    """
    d = np.full((map.shape[0], map.shape[1]), np.inf)
    p = np.full((map.shape[0], map.shape[1]), -1)
    visited = np.full((map.shape[0], map.shape[1]), False, dtype=np.bool)

    # d at the snake's head should be 0 (we're already there, so no cost!)
    d[point[1]][point[0]] = 0

    pq = [(1, point)]
    heapify(pq)
    while len(pq) > 0:
        next_vert = heappop(pq)[1]
        nv_x, nv_y = next_vert[0], next_vert[1]

        # ignore if we've already visited this vertex
        if visited[nv_y][nv_x]:
            continue

        # consider neighbors of this vertex
        for x, y in neighbors_of(nv_x, nv_y, map):
            if map[y][x] == MAP_SNAKE:
                d[y][x] = -1
                p[y][x] = -1
            elif d[nv_y][nv_x] + 1 < d[y][x]:
                d[y][x] = d[nv_y][nv_x] + 1
                p[y][x] = map.shape[1] * nv_y + nv_x

                # re-add to pq if d[] was updated
                heappush(pq, (d[y][x], (x, y)))

        visited[nv_y][nv_x] = True

    return d, p


def get_next_move(snake_head, path):
    """Get the snake's next move in a given path.
    :param snake_head: Location of the snake's head (x, y).
    :param path: List of points creating a path from the snake's head.
                 [ (x, y), (x, y) ... ]
    :return Next move. One of ("right", "left", "up", "down").
    """
    assert type(path) == list, "Path must be a list."
    assert len(path) > 0, "Cannot get next move for an empty path."

    nextpoint_x, nextpoint_y = path[0]

    assert snake_head != path[0], "Next coordinate cannot be the same as snake head"

    if nextpoint_x > snake_head.x:
        return "right"
    elif nextpoint_x < snake_head.x:
        return "left"
    elif nextpoint_y < snake_head.y:
        return "up"
    elif nextpoint_y > snake_head.y:
        return "down"


def find_path_dijkstra(x, y, p):
    """Get the shortest path to a given point in a predecessor matrix.
    :param x: X coordinate of destination
    :param y: Y coordinate of destination
    :param p: Predecessor matrix to get path from.
    :return List of points in path, starting from snake head [(0, 0),(0, 1)...]
    """
    path = []
    point = p[y][x]

    path.append((x, y))

    while point != -1:
        px, py = int(point % p.shape[1]), int(point / p.shape[1])
        path.append((px, py))
        point = p[py][px]

        # Path length cannot be any greater than (width * height)
        if len(path) > p.size:
            raise Exception("Error getting path from predecessor matrix!")

    path.reverse()
    return path[1:]
