import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_NAME = "Terarriaa"
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 10


# class Player(arcade.Sprite):

#     def update(self, delta_time: float = 1/60):
        
        
#         if self.left < 0:
#             self.left = 0
#         elif self.right > WINDOW_WIDTH - 1:
#             self.right = WINDOW_WIDTH - 1

#         if self.bottom < 0:
#             self.bottom = 0
#         elif self.top > WINDOW_HEIGHT - 1:
#             self.top = WINDOW_HEIGHT - 1

class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME, fullscreen=False, resizable=False)
        
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        
        # self.player_sprite = None
        # self.player_list = None
        # self.dirt_list = None
        self.scene = None
        
        self.dirt_texture = arcade.load_texture("textures/dirt.png")
        self.player_texture = arcade.load_texture("textures/player.png")
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        self.physics_engine = None
        self.camera = None

    def setup(self):
        self.scene = arcade.Scene()
        
        self.player_sprite = arcade.Sprite(self.player_texture,center_x=int(WINDOW_WIDTH/2),center_y=int(WINDOW_HEIGHT/2)+32)
        self.scene.add_sprite("Player", self.player_sprite)
        self.scene.add_sprite_list("Floor", use_spatial_hash=True )
        
        for x in range(16, 1280, 32):
            for y in range(int(WINDOW_HEIGHT/2)-16, -16, -32):
                dirt = arcade.Sprite(self.dirt_texture)
                dirt.center_x = x
                dirt.center_y = y
                self.scene.add_sprite("Floor", dirt)
                
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, walls=self.scene["Floor"], gravity_constant=GRAVITY)
        self.camera = arcade.camera.Camera2D()
        
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
    
    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

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
        elif key == arcade.key.ESCAPE:
            self.setup()

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