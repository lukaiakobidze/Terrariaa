import arcade

class Tile():
    
    def __init__(self, center_x: int, center_y: int, grid_x: int, grid_y: int, texture: arcade.Texture):
        
        self._center_x = center_x
        self._center_y = center_y
        self._grid_x = grid_x
        self._grid_y = grid_y
        self.sprite = arcade.Sprite(texture, center_x= self._center_x, center_y= self._center_y)
        self.draw = True
        
    def __str__(self):
        return f"x{self.center_x}  y{self.center_y}"
       
    @property 
    def grid_x(self):
        return self._grid_x
    
    @property 
    def grid_y(self):
        return self._grid_y
        
    @property
    def center_x(self):
        return self._center_x
    
    @property
    def center_y(self):
        return self._center_y
    
    def remove(self):
        del self
    
        