import arcade
from tile import Tile
from textures import dirt_texture


class Map():
    
    def __init__(self, size_x: int, size_y: int, scene: arcade.Scene):
        
        self._size_x = size_x
        self._size_y = size_y
        self.tile_list = []
        self.scene = scene
        
    @property
    def size_x(self):
        return self._size_x
    
    @property
    def size_y(self):
        return self._size_y
        
        
    def make_Tiles(self):
        row = []
        for x in range(self.size_x):
            row = []
            for y in range(0, -self.size_y, -1):
                center_x = (x * 32) + 16
                center_y = (y * 32) + 16
                tile = Tile(center_x, center_y, dirt_texture)
                row.append(tile)
                sprite = arcade.Sprite(dirt_texture, center_x= center_x, center_y= center_y)
                self.scene.add_sprite("Tile", sprite)
            self.tile_list.append(row)
        
                