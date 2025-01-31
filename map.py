import arcade
from tile import Tile
from textures import dirt_texture, player_texture
from math import ceil

class Map():
    
    def __init__(self, size_x: int, size_y: int):
        
        self._size_x = size_x
        self._size_y = size_y
        self.tile_list = []
        self.scene = arcade.Scene()
        self.player_sprite = arcade.Sprite(player_texture,center_x=50,center_y=0)
        self.scene.add_sprite("Player", self.player_sprite)
        
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
            for y in range(0, self.size_y, 1):
                center_x = (x * 32) + 16
                center_y = -(y * 32) - 16
                tile = Tile(center_x, center_y, x, y, dirt_texture)
                row.append(tile)
                sprite = tile.sprite
                self.scene.add_sprite("Tile", sprite)
                
                # Debugging: Check if sprite was added
                if sprite in self.scene["Tile"]:
                    print(f"Added tile sprite at ({x}, {y}) to the scene.")
                else:
                    print(f"Failed to add tile sprite at ({x}, {y}) to the scene.")
            self.tile_list.append(row)
    

        
    
    
    def break_Tile(self, x, y):
        x = ceil(x / 32) - 1
        y = -ceil(y / 32)

        # Bounds check
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            print(f"Invalid tile position: ({x}, {y})")
            return

        tile = self.tile_list[x][y]
        
        if tile is None:
            print(f"Tile at ({x}, {y}) is already broken!")
            return

        # Debugging output: Check the tile sprite in the "Tile" group
        print(f"Checking if tile sprite at ({x}, {y}) exists in scene['Tile']...")
        
        # Directly access and remove the sprite from the "Tile" group
        if tile.sprite in self.scene["Tile"]:
            print(f"Tile sprite at ({x}, {y}) exists in the scene. Removing...")
            self.scene["Tile"].remove(tile.sprite)  # Remove sprite from the scene
            print(f"Tile sprite at ({x}, {y}) removed from scene.")
        else:
            print(f"Tile sprite at ({x}, {y}) does NOT exist in the scene.")
        
        self.tile_list[x][y] = None  # Remove tile from grid
        print(f"Tile at ({x}, {y}) broken!")



