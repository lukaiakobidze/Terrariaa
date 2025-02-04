import arcade
from tile import Tile
import textures
from math import ceil, floor
from methods import wrld_Pixels_To_Tile
import block

class Map():
    
    def __init__(self, size_x: int, size_y: int):
        
        self._size_x = size_x
        self._size_y = size_y
        self.tile_list = []
        
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Tile")
        self.scene.add_sprite_list("Breaking")
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Cursor")
        
        self.breaking_sprite = None
        #self.scene.add_sprite("Breaking", None)
        self.player_sprite = arcade.Sprite(textures.player_texture,center_x=50,center_y=0)
        self.scene.add_sprite("Player", self.player_sprite)
        self.cursor = arcade.Sprite(textures.cursor_texture, center_x=0,center_y=0)
        self.scene.add_sprite("Cursor", self.cursor)
        
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
                if y > 3:
                    tile = Tile(center_x, center_y, x, y, block.cobblestone_Block)
                else:
                    tile = Tile(center_x, center_y, x, y, block.dirt_Block)    
                row.append(tile)
                self.scene.add_sprite("Tile", tile.sprite)
                
            self.tile_list.append(row)
    
    def break_Tile(self, x, y):
        x, y = wrld_Pixels_To_Tile(x, y)

        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            print(f"Outside map: ({x}, {y})!!")
            return

        tile = self.tile_list[x][y]
        
        if tile is None:
            print(f"No Tile at ({x}, {y})!")
            return

        # if tile.sprite in self.scene["Tile"]:
        #     #print(f"Tile sprite at ({x}, {y}) exists in the scene. Removing...")
        #     self.scene["Tile"].remove(tile.sprite)  
        #     #print(f"Tile sprite at ({x}, {y}) removed from scene.")
        # else:
        #     print(f"Tile sprite at ({x}, {y}) does NOT exist in the scene.")
        
        if tile.block.breakable == True:
            self.tile_list[x][y].block = block.air_block
            self.scene["Tile"].remove(tile.sprite)
            print(f"Tile at ({x}, {y}) broken!")
        else:
            print("block not breakable!")
        
        #self.tile_list[x][y] = None  
        
        
        #tile.remove()


    def draw_Cursor(self, x, y):
        
        x, y = wrld_Pixels_To_Tile(x, y)
        
        self.cursor.center_x = (32 * x + 16)
        self.cursor.center_y = (-32 * y - 16)
        
    def draw_Cracks(self, tile: Tile, i: int):
        
        if self.breaking_sprite in self.scene["Breaking"]:
            self.scene["Breaking"].remove(self.breaking_sprite)
            
        if tile:
            if 0 > i < 0.5:
                self.breaking_sprite = arcade.Sprite(textures.breaking_textures[0], center_x=tile.center_x, center_y=tile.center_y)
                self.scene.add_sprite("Breaking", self.breaking_sprite)
            elif 0.5 <= i < 0.8:
                self.breaking_sprite = arcade.Sprite(textures.breaking_textures[1], center_x=tile.center_x, center_y=tile.center_y)
                self.scene.add_sprite("Breaking", self.breaking_sprite)
            elif 0.8 <= i < 1:
                self.breaking_sprite = arcade.Sprite(textures.breaking_textures[2], center_x=tile.center_x, center_y=tile.center_y)
                self.scene.add_sprite("Breaking", self.breaking_sprite)
        
        
        
        
        

        