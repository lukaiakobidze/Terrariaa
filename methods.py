import arcade
from math import sqrt, floor, ceil
import settings

@staticmethod
def convert_Pos(x, y, camera):
    world_x = x - int(settings.WINDOW_WIDTH/2) + int(camera.position.x)
    world_y = y - int(settings.WINDOW_HEIGHT/2) + int(camera.position.y)
    return int(world_x), int(world_y)

@staticmethod
def range_Tile(x1, y1, x2, y2):
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    answ = floor(sqrt((x * x) + (y * y)))
    print(f"range: {answ}")
    return answ

@staticmethod
def wrld_Pixels_To_Tile(x, y):
    x1 = floor(x / 32)
    y1 = -ceil(y / 32)   
    
    return x1, y1 