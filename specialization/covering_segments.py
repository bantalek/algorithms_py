# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda tup: tup[1])

    pre = segments[0].end
    coord = pre
    coords = [pre]

    for s in segments[1:]:
        if s.start <= coord <= s.end:
            continue

        else:
            coord = s.end
            coords.append(s.end)

    return coords

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
