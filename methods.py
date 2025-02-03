import arcade
from math import floor
from map import Map
import settings

@staticmethod
def convert_Pos(x, y, camera):
    world_x = x - int(settings.WINDOW_WIDTH/2) + int(camera.position.x)
    world_y = y - int(settings.WINDOW_HEIGHT/2) + int(camera.position.y)
    return int(world_x), int(world_y)
