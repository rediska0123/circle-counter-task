from PIL import Image, ImageColor
import numpy as np
from queue import Queue
import math


# get_array_from_image returns a numpy.array from the picture in
# filename.
def get_array_from_image(filename):
    img = Image.open(filename)
    return np.array(img)


# bfs visits non-used img pixels which satisfy predicate and calls
# action function with two arguments, the coordinates of pixel.
def bfs(img, used, start, predicate, action):
    (n, m, _) = img.shape
    (i, j) = start
    if not predicate(img[i][j]):
        return
    used[i][j] = True
    q = Queue()
    q.put((i, j))
    while not q.empty():
        (x, y) = q.get()
        action(x, y)
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not used[nx][ny] and predicate(img[nx][ny]):
                used[nx][ny] = True
                q.put((nx, ny))


# count_circles returns (red_cnt, black_cnt) --- the number of red and
# black circles found in filename picture.
def count_circles(filename):
    img = get_array_from_image(filename)
    (n, m, _) = img.shape

    used = np.zeros((n, m), dtype=bool)

    is_green = lambda pixel: pixel[0] < 10 and pixel[1] > 10 and pixel[2] < 10

    # mark all green pixels
    for i in range(n):
        for j in range(m):
            if not used[i][j]:
                bfs(img, used, (i, j), is_green, lambda x, y: 0)

    black_cnt = red_cnt = 0
    for i in range(n):
        for j in range(m):
            if not used[i][j]:
                # mark new component (circle or rectangle)
                component = []
                bfs(img, used, (i, j), lambda p: not is_green(p),
                    lambda x, y: component.append((x, y)))

                # check if component is a circle
                if not circle_shape(component):
                    continue

                # red or black is decided according to the average red
                # hue
                red = np.average([img[i][j] for (i, j) in component],
                                 axis=0)[0]
                if red > 10:
                    red_cnt = red_cnt + 1
                else:
                    black_cnt = black_cnt + 1

    return red_cnt, black_cnt


# circle_shape returns True if the figure with (x, y) coordinates from
# component is a circle more likely than a rectangle.
def circle_shape(component):
    # compute center coordinates
    (cx, cy) = np.average(np.array(component), axis=0)

    # compute maximum component distance from center
    sq_radius = max([(x - cx) ** 2 + (y - cy) ** 2 for (x, y) in component])

    # compute approximate square if the figure is a circle
    square = sq_radius * math.pi

    # compare square to the component length
    return len(component) > 0.9 * square
