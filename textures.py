import arcade

dirt_texture = arcade.load_texture("textures/dirt.png")
player_texture = arcade.load_texture("textures/player.png")
cursor_texture = arcade.load_texture("textures/cursor.png")
cobblestone_texture = arcade.load_texture("textures/cobblestone.png")
air_texture = arcade.load_texture("textures/air.png")

breaking_textures = [
    arcade.load_texture("textures/breaking_1.png"),
    arcade.load_texture("textures/breaking_2.png"),
    arcade.load_texture("textures/breaking_3.png")
]