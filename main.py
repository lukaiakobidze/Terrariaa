import arcade
import arcade.clock
import textures
from map import Map
from methods import convert_Pos, range_Tile, wrld_Pixels_To_Tile
import settings
import time
import math




#-------------------------------------------------GAMEVIEW-------------------------------------------------

class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.WINDOW_NAME, fullscreen=False, resizable=False)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        
        
        self.current_Mouse_Pos = None
        self.last_Mouse_Pos_Screen = None
        self.map = None
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.physics_engine = None
        self.camera = None
        
        self.mouse_Pressed = False
        self.mouse_Pressed_Time = None
        self.selected_Block = None
        self.fps = 0
        self.counter = 0
        

#-----------------------------------------------------SETUP---------------------------------------------------------

    def setup(self):

        self.map = Map(500, 50)
        self.map.make_Tiles()
        self.current_Mouse_Pos = (0, 0)
        self.last_Mouse_Pos_Screen = (0, 0)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.map.player_sprite, walls=self.map.scene["Tile"], gravity_constant=settings.GRAVITY)
        self.camera = arcade.camera.Camera2D()
        
#--------------------------------------------ON_DRAW-------------------------------------------------------       
        
    def on_draw(self):
        self.clear()

        self.camera.use()
        self.map.scene["Tile"].draw(pixelated=True)
        if self.mouse_Pressed:
            self.map.scene["Breaking"].draw(pixelated=True)
        self.map.scene["Player"].draw(pixelated=True)
        self.map.scene["Cursor"].draw(pixelated=True)
        
        arcade.draw_text(
            f"FPS: {self.fps}",
            self.camera.position.x + (self.width / 2) - 100,
            self.camera.position.y + (self.height / 2) - 40,
            arcade.color.WHITE,
            14
        )
        
        
            
            
        
    
#----------------------------------------UPDATE_PLAYER_SPEED-------------------------------------------    
    
    def update_player_speed(self):

        
        self.map.player_sprite.change_x = 0
        

        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.can_jump():
                self.map.player_sprite.change_y = settings.PLAYER_JUMP_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.map.player_sprite.change_y = -settings.PLAYER_MOVEMENT_SPEED
            
        if self.left_pressed and not self.right_pressed:
            self.map.player_sprite.set_texture(1)
            self.map.player_sprite.change_x = -settings.PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.map.player_sprite.set_texture(0)
            self.map.player_sprite.change_x = settings.PLAYER_MOVEMENT_SPEED
    
#----------------------------------------------ON_UPDATE----------------------------------------------------
    
    def on_update(self, delta_time):
        if self.counter == 10:
            self.fps = math.floor(1 / delta_time)
            self.counter = 0
        else:
            self.counter += 1

        if self.map.player_sprite.change_x != 0 or self.map.player_sprite.change_y != 0:
            self.current_Mouse_Pos = convert_Pos(*self.last_Mouse_Pos_Screen, self.camera)
    
        self.physics_engine.update()
        self.map.scene["Player"].update(delta_time)
        self.map.scene["Tile"].update(delta_time)
        self.map.scene["Cursor"].update(delta_time)
        self.camera.position = self.map.player_sprite.position
        self.map.draw_Cursor(*self.current_Mouse_Pos)
        
        if not self.selected_Block and self.map.tile_list[wrld_Pixels_To_Tile(*self.current_Mouse_Pos)[0]][wrld_Pixels_To_Tile(*self.current_Mouse_Pos)[1]].block.breakable:
            self.selected_Block = self.map.tile_list[wrld_Pixels_To_Tile(*self.current_Mouse_Pos)[0]][wrld_Pixels_To_Tile(*self.current_Mouse_Pos)[1]]
            self.mouse_Pressed_Time = time.time()
        
        if self.selected_Block:
            if self.selected_Block.block.breakable:
                if self.mouse_Pressed and self.mouse_Pressed_Time is not None and self.selected_Block.block.breakable:
                    
                    if wrld_Pixels_To_Tile(*self.current_Mouse_Pos) != self.selected_Block.pos_Grid:
                        self.mouse_Pressed_Time = time.time()
                        self.selected_Block = self.map.tile_list[wrld_Pixels_To_Tile(*self.current_Mouse_Pos)[0]][wrld_Pixels_To_Tile(*self.current_Mouse_Pos)[1]]
                
                    duration = time.time() - self.mouse_Pressed_Time
                    progress = min(1, duration / self.selected_Block.block.hardness)
                    
                    self.map.draw_Cracks(self.selected_Block, progress)
                    if duration >= self.selected_Block.block.hardness:
                        self.map.break_Tile(*self.current_Mouse_Pos)
                        self.selected_Block = None
                       
                        
        
        
        
        
        
    
#-----------------------------------------------------ON_KEY_PRESS---------------------------------------------------
    
    def on_key_press(self, key, modifiers):
        

        if key == arcade.key.W:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.R:
            self.setup()
        elif key == arcade.key.ESCAPE:
            self.close()

#----------------------------------------------------ON_KEY_RELEASE---------------------------------------------------------

    def on_key_release(self, key, modifiers):
       

        if key == arcade.key.W:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()
        
#------------------------------------------------ON_MOUSE_PRESS------------------------------------------------------------- 
        
    def on_mouse_press(self, x, y, button, modifiers):
      
        self.last_Mouse_Pos_Screen = (x, y)
        self.current_Mouse_Pos = convert_Pos(x, y, self.camera)
        pos_x, pos_y = self.current_Mouse_Pos
        
        if button == arcade.MOUSE_BUTTON_LEFT:
            if range_Tile(*wrld_Pixels_To_Tile(self.map.player_sprite.center_x, self.map.player_sprite.center_y), *wrld_Pixels_To_Tile(pos_x, pos_y)) <= settings.PLAYER_REACH:
                self.mouse_Pressed = True
                self.mouse_Pressed_Time =time.time()
                self.selected_Block = self.map.tile_list[wrld_Pixels_To_Tile(pos_x, pos_y)[0]][wrld_Pixels_To_Tile(pos_x, pos_y)[1]]
        if self.map.breaking_sprite in self.map.scene["Breaking"]:
            self.map.scene["Breaking"].remove(self.map.breaking_sprite)
        
    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_Pressed = False
        self.mouse_Pressed_Time = None
        self.selected_Block = None
        
            
    def on_mouse_motion(self, x, y, dx, dy):
        current_tile = wrld_Pixels_To_Tile(*convert_Pos(x, y, self.camera))
        
        if self.selected_Block and self.mouse_Pressed:
            if self.map.tile_list[current_tile[0]][current_tile[1]] != self.selected_Block and range_Tile(*current_tile, *wrld_Pixels_To_Tile(self.map.player_sprite.center_x, self.map.player_sprite.center_y)) <= settings.PLAYER_REACH:
                self.selected_Block = self.map.tile_list[current_tile[0]][current_tile[1]]
                self.mouse_Pressed_Time = time.time()
                if self.map.breaking_sprite in self.map.scene["Breaking"]:
                    self.map.scene["Breaking"].remove(self.map.breaking_sprite)
        elif range_Tile(*current_tile, *wrld_Pixels_To_Tile(self.map.player_sprite.center_x, self.map.player_sprite.center_y)) <= settings.PLAYER_REACH:
            self.selected_Block = self.map.tile_list[current_tile[0]][current_tile[1]]
            self.mouse_Pressed_Time = time.time()
        
        self.last_Mouse_Pos_Screen = (x, y)
        self.current_Mouse_Pos = convert_Pos(x, y, self.camera)
        
        
            
    
        
#---------------------------------------------------------MAIN-------------------------------------------------------  
         

def main():
    
    window = GameView()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()