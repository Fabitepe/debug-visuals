from shapely import Polygon, LineString, LinearRing
import random

# import the visualizer to get access to all functions
from debug_visuals import Visualizer


geoms = []
coord_values = []
geoms.append(
    Polygon(
        shell=[
            (0, 0),
            (2, 0),
            (2, 2),
            (0, 2),
            (0, 0)
        ],
        holes=[
            [
                (0.5, 0.5),
                (1.5, 0.5),
                (1.5, 1.5),
                (0.5, 1.5),
                (0.5, 0.5)
            ]
        ]
    )
)
test = {
    "key1": {"key2": "Hello", "key3": "World"},
    "key4": "!!!",
    12: "Number",
    42: [
        1,
        2,
        3,
        4,
        1.5,
        "A String in a list for some reason",
        [
            "Test1",
            "Test2",
            3,
            4,
            5.5
        ],
        geoms[0]
    ],
    "geoms:": geoms
}
geoms.append(LineString([(0, 0), (1, 1)]))
for i in range(10):
    coords = []
    for ii in range(random.randrange(4, 6, 1)):
        coords.append(
            (random.randrange(-1, 4, 1), random.randrange(-1, 4, 1))
        )
        coord_values.extend([coords[ii][0], coords[ii][1]])
    geoms.append(LinearRing(coords))

print("test")
