import FrameWork
import Main
from pico2d import *

name = "TitleState"
image = None

def enter():
    global image
    image = load_image("title.jpg")
    pass

def exit():
    global image
    del(image)
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            FrameWork.quit()
        else:
            if (event.type , event.key) == (SDL_KEYDOWN , SDLK_ESCAPE):
                FrameWork.quit()
            elif (event.type , event.key) == (SDL_KEYDOWN , SDLK_SPACE):
                FrameWork.change_state(Main)
    pass

def draw():
    clear_canvas()
    image.draw(400 , 300)
    update_canvas()
    pass

def update():
    pass

def pause():
    pass

def resume():
    pass