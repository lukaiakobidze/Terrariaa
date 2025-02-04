import arcade
import textures



class Block():
    
    def __init__(self, name: str, texture: arcade.Texture, breakable: bool, hardness: int, invisible: bool):
        self.name = name
        self.texture = texture
        self.breakable = breakable
        self.hardness = hardness
        self.invisible = invisible



dirt_Block = Block("Dirt", textures.dirt_texture, True, 0.1, False)
cobblestone_Block = Block("Cobblestone", textures.cobblestone_texture, True, 0.1, False)
air_block = Block("Air", textures.air_texture, False, 0, True)