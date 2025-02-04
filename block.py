import arcade
import textures



class Block():
    
    def __init__(self, name: str, texture: arcade.Texture, breakable: bool, hardness: int):
        self.name = name
        self.texture = texture
        self.breakable = breakable
        self.hardness = hardness



dirt_Block = Block("Dirt", textures.dirt_texture, True, 1)
cobblestone_Block = Block("Cobblestone", textures.cobblestone_texture, True, 2)
air_block = Block("Air", None, False, 0)