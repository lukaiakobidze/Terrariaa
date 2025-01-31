import arcade
from textures import dirt_texture, player_texture
from map import Map




WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_NAME = "Terarriaa"
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.5
PLAYER_JUMP_SPEED = 8


class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME, fullscreen=False, resizable=False)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        
        # self.player_sprite = None
        # self.player_list = None
        # self.dirt_list = None
        self.scene = None
        
        self.map = None
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.physics_engine = None
        self.camera = None

    def setup(self):
        self.scene = arcade.Scene()
        self.map = Map(100, 20, self.scene)
        self.player_sprite = arcade.Sprite(player_texture,center_x=20,center_y=50)
        self.scene.add_sprite("Player", self.player_sprite)
        self.map.make_Tiles()
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, walls=self.scene["Tile"], gravity_constant=GRAVITY)
        self.camera = arcade.camera.Camera2D()
        
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
    
    def update_player_speed(self):

        
        self.player_sprite.change_x = 0
        

        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    
    
    
    def on_update(self, delta_time):
    
        self.physics_engine.update()
        self.scene["Player"].update(delta_time)
        self.camera.position = self.player_sprite.position
    
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
        
      
      
def main():
    
    window = GameView()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()