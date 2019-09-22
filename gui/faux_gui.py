# from raylib.static import *


# screenWidth = 800
# screenHeight = 450
# InitWindow(screenWidth, screenHeight, b"Hello Raylib")
# SetTargetFPS(60)

# image = LoadImage("/Users/eudvazquez/personal/FauxTrans/data/image/Faux/out-0.jpg".encode('ascii'))
# image = ImageResize(pyray.pointer(image), 400, 225)
# texture = LoadTextureFromImage(image)
# UnloadImage(image)

# while not WindowShouldClose():
#     BeginDrawing()
#     ClearBackground(RAYWHITE)
#     DrawTexture(texture, int(screenWidth/2 - texture.width/2), int(screenHeight/2 - texture.height/2), WHITE)
#     DrawText("this IS a texture loaded from an image!".encode('ascii'), 300, 370, 10, GRAY)
#     EndDrawing()
# CloseWindow()


from raylib.pyray import PyRay
from raylib.colors import *

pyray = PyRay()

pyray.init_window(800, 800, "Hello Pyray")
pyray.set_target_fps(60)

image = pyray.load_image("/Users/eudvazquez/personal/FauxTrans/data/image/Faux/out-0.jpg".encode('ascii'))
pyray.image_resize(pyray.pointer(image), 600, 800)
texture = pyray.load_texture_from_image(image)
pyray.unload_image(image)

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(RAYWHITE)
    pyray.draw_texture(texture, int(800/2 - texture.width/2), 0, WHITE)
    pyray.end_drawing()
pyray.close_window()