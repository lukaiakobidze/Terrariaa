import arcade
from math import floor
from map import Map


@staticmethod
def convert_Pos(x, y, camera):
    world_x = x - int(1280/2) + int(camera.position.x)
    world_y = y - int(720/2) + int(camera.position.y)
    print(f"Mouse ({x}, {y}) → World ({world_x}, {world_y}) {camera.position.x} {camera.position.y}")  # Debugging print
    return int(world_x), int(world_y)
