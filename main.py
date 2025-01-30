import arcade


WINDOWLENGTH = 1280
WINDOWHEIGHT = 720
WINDOWNAME = "Terarriaa"


class GameView(arcade.Window):
    
    
    def __init__(self):
        
        super().__init__(WINDOWLENGTH, WINDOWHEIGHT, WINDOWNAME, fullscreen=False, resizable=True)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.dirt_texture = arcade.load_texture("dirt.png")
        self.player_texture = arcade.load_texture("player.png")
        
        self.player_list = arcade.SpriteList()
        self.player_list.append(arcade.Sprite(self.player_texture,center_x=int(WINDOWLENGTH/2),center_y=int(WINDOWHEIGHT/2)+32))
        self.dirt_list = arcade.SpriteList(use_spatial_hash=True)
        
        for x in range(16, 1280, 32):
            for y in range(int(WINDOWHEIGHT/2)-16, -16, -32):
                dirt = arcade.Sprite(self.dirt_texture)
                dirt.center_x = x
                dirt.center_y = y
                self.dirt_list.append(dirt)
            
        
        
        
    def setup(self):
        
        pass
    
    def on_draw(self):
        self.clear()
        self.player_list.draw(pixelated=True)
        self.dirt_list.draw(pixelated=True)
        
        
      
      
def main():
    
    window = GameView()
    window.setup()
    arcade.run()
    
    
    
if __name__ == "__main__":
    main()