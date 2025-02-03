import arcade
from textures import dirt_texture, player_texture
from map import Map
from methods import convert_Pos, range_Tile, wrld_Pixels_To_Tile
import settings


#-------------------------------------------------GAMEVIEW-------------------------------------------------

class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.WINDOW_NAME, fullscreen=False, resizable=False)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        
        
        self.current_Mouse_Pos = None
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
        self.current_Mouse_Pos = (0, 0)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.map.player_sprite, walls=self.map.scene["Tile"], gravity_constant=settings.GRAVITY)
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
            self.map.player_sprite.change_y = settings.PLAYER_JUMP_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.map.player_sprite.change_y = -settings.PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.map.player_sprite.change_x = -settings.PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.map.player_sprite.change_x = settings.PLAYER_MOVEMENT_SPEED
    
#----------------------------------------------ON_UPDATE----------------------------------------------------
    
    def on_update(self, delta_time):
    
        self.physics_engine.update()
        self.map.scene["Player"].update(delta_time)
        self.map.scene["Tile"].update(delta_time)
        self.map.scene["Cursor"].update(delta_time)
        self.camera.position = self.map.player_sprite.position
        self.map.draw_Cursor(*self.current_Mouse_Pos)
    
#-----------------------------------------------------ON_KEY_PRESS---------------------------------------------------
    
    def on_key_press(self, key, modifiers):
        

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
      
        pos_x, pos_y = convert_Pos(x, y, self.camera)
        
        if button == arcade.MOUSE_BUTTON_LEFT:
            if range_Tile(*wrld_Pixels_To_Tile(self.map.player_sprite.center_x, self.map.player_sprite.center_y), *wrld_Pixels_To_Tile(pos_x, pos_y)) <= settings.PLAYER_REACH:
                self.map.break_Tile(pos_x, pos_y)
            
            
    def on_mouse_motion(self, x, y, dx, dy):
        self.current_Mouse_Pos = convert_Pos(x, y, self.camera)
        
            
    
        
#---------------------------------------------------------MAIN-------------------------------------------------------  
      
def main():
    
    window = GameView()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()