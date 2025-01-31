import arcade
from textures import dirt_texture, player_texture
from map import Map
from methods import convert_Pos


#---------------------------------------------------VARIABLES------------------------------------------

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_NAME = "Terarriaa"
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.5
PLAYER_JUMP_SPEED = 8


#-------------------------------------------------GAMEVIEW-------------------------------------------------

class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME, fullscreen=False, resizable=False)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        
        
        
        self.map = None
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.physics_engine = None
        self.camera = None

#-----------------------------------------------------SETUP---------------------------------------------------------

    def setup(self):
        
        self.map = Map(100, 20)
        self.map.make_Tiles()
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.map.player_sprite, walls=self.map.scene["Tile"], gravity_constant=GRAVITY)
        self.camera = arcade.camera.Camera2D()
        
#--------------------------------------------ON_DRAW-------------------------------------------------------       
        
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.map.scene.draw()
    
#----------------------------------------UPDATE_PLAYER_SPEED-------------------------------------------    
    
    def update_player_speed(self):

        
        self.map.player_sprite.change_x = 0
        

        if self.up_pressed and not self.down_pressed:
            #if self.physics_engine.can_jump():
            self.map.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.map.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.map.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.map.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
#----------------------------------------------ON_UPDATE----------------------------------------------------
    
    def on_update(self, delta_time):
    
        self.physics_engine.update()
        
        # for row in self.map.tile_list:
        #     for tile in row:
        #         if tile is not None:  # Make sure the tile exists
        #             if tile.sprite not in self.map.scene["Tile"]:
        #                 print(f"Tile at ({tile.grid_x}, {tile.grid_y}) is correctly removed.")
        
        self.map.scene["Player"].update(delta_time)
        self.map.scene["Tile"].update(delta_time)
        self.camera.position = self.map.player_sprite.position
    
#-----------------------------------------------------ON_KEY_PRESS---------------------------------------------------
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.R:
            self.setup()
        elif key == arcade.key.ESCAPE:
            self.close()

#----------------------------------------------------ON_KEY_RELEASE---------------------------------------------------------

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()
        
#------------------------------------------------ON_MOUSE_PRESS------------------------------------------------------------- 
        
    def on_mouse_press(self, x, y, button, modifiers):
        # for tiles in self.map.tile_list:
        #     for tile in tiles:
        #         if tile is not None:
        #             print(f"[{tile.grid_x} {tile.grid_y}   ]")
        pos_x, pos_y = convert_Pos(x, y, self.camera)
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.map.break_Tile(pos_x, pos_y)
            
            
            
            
    
        
#---------------------------------------------------------MAIN-------------------------------------------------------  
      
def main():
    
    window = GameView()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()