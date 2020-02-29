import arcade
import math
import random

WIDTH = 800
HEIGHT = 800
points = 0
frames = 0
hits = 0
misses = 0

window = arcade.Window(WIDTH, HEIGHT, "Off Brand Tile Frenzy")
arcade.set_background_color(arcade.color.WHITE)

circle_x = WIDTH//2
circle_y = HEIGHT//2
mouse_x = 0
mouse_y = 0
circle_radius = 50
circle_x2 = WIDTH//2
circle_y2 = HEIGHT//2
circle_radius2 = 10
output_string = ' '
game_over_string =' '

@window.event("on_draw") 
def game_loop(): #the main game loop that runs 60 times a second

    global circle_radius
    global frames
    global circle_x
    global circle_y
    global points
    global output_string
    global game_over_string

    frames += 1

    if frames > 1800: #end game stuff
        circle_radius += 8
    if frames == 1950:
        output_string = (f'Your final score was {points}! You made {hits} out of {hits + misses}! You only missed {misses}! Your Accuracy was {int((hits / (hits + misses) * 100))}%!')
    if frames == 1900:
        game_over_string = ('Game Over!')

    arcade.start_render()
    arcade.draw_circle_filled(circle_x, circle_y, circle_radius, arcade.color.CHERRY_BLOSSOM_PINK) 
    arcade.draw_text(output_string, 80, 400, arcade.color.BLACK)
    arcade.draw_text(game_over_string, 340, 500, arcade.color.BLACK)


@window.event()
def on_mouse_press(mouse_x, mouse_y, button, modifiers): #during mouse click

    global circle_radius
    global circle_x
    global circle_y
    global points
    global hits
    global misses

    if frames < 1800:
        if (math.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)) < circle_radius: #distance function to check if you click outside or inside the circle
            circle_x = random.randint(0,600) #this randomizes the location of the circle on a hit
            circle_y = random.randint(0,600)
            hits += 1
            points = points + 1 #adds points for each hit inside the circle
        else:
            misses += 1
            points = points - 1 #deducts a point on miss


arcade.run()
