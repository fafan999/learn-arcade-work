import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(
        0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """Draw a snowman"""

    # Draw a point at x, y for reference
    # arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def draw_star(x, y, st_frac):
    """Draw a star"""
    # arcade.draw_line(start_x=x, start_y=y+15-st_frac,
    #                  end_x=x, end_y=y-15+st_frac, color=arcade.csscolor.YELLOW, line_width=2)
    # arcade.draw_line(start_x=x-15+st_frac, start_y=y,
    #                  end_x=x+15-st_frac, end_y=y, color=arcade.csscolor.YELLOW, line_width=2)
    # arcade.draw_line(start_x=x+10-st_frac/2, start_y=y+10-st_frac/2,
    #                  end_x=x-10+st_frac/2, end_y=y-10+st_frac/2, color=arcade.csscolor.YELLOW, line_width=2)
    # arcade.draw_line(start_x=x+10-st_frac/2, start_y=y-10+st_frac/2,
    #                  end_x=x-10+st_frac/2, end_y=y+10-st_frac/2, color=arcade.csscolor.YELLOW, line_width=2)

    # Draw a point at x, y for reference
    arcade.draw_circle_filled(x, y, st_frac, arcade.csscolor.LIGHT_SKY_BLUE)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()

    for i in range(stars_count):
        draw_star(on_draw.stars_x[i], y_random[i], frac_random[i])
    draw_snow_person(on_draw.snow_person2_x, 180)
    draw_snow_person(on_draw.snow_person1_x, 140)

    # st = 7

    # arcade.draw_line(start_x=315, start_y=430-st, end_x=315,
    #                  end_y=400+st, color=arcade.csscolor.YELLOW, line_width=2)
    # arcade.draw_line(start_x=300+st, start_y=415, end_x=330-st,
    #                  end_y=415, color=arcade.csscolor.YELLOW, line_width=2)
    # arcade.draw_line(start_x=325-st/2, start_y=425-st/2, end_x=305+st/2,
    #                  end_y=405+st/2, color=arcade.csscolor.YELLOW, line_width=2)
    # arcade.draw_line(start_x=325-st/2, start_y=405+st/2, end_x=305+st/2,
    #                  end_y=425-st/2, color=arcade.csscolor.YELLOW, line_width=2)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    for i in range(stars_count):
        if (on_draw.stars_x[i] > x_random[i]+40):
            on_draw.stars_d = -0.5
            print("yes")
        elif (on_draw.stars_x[i] < x_random[i]):
            on_draw.stars_d = 0.5

    if (on_draw.snow_person1_x > 310):
        on_draw.snow_person1_d *= -1
    elif (on_draw.snow_person1_x < 150):
        on_draw.snow_person1_d *= -1

    if (on_draw.snow_person2_x > 480):
        on_draw.snow_person2_d *= -1
    elif (on_draw.snow_person2_x < 400):
        on_draw.snow_person2_d *= -1

    for i in range(stars_count):
        on_draw.stars_x[i] += on_draw.stars_d
    on_draw.snow_person1_x += on_draw.snow_person1_d
    on_draw.snow_person2_x += on_draw.snow_person2_d


# Create a value that our on_draw.snow_person1_x will start at.

on_draw.snow_person2_x = 400
on_draw.snow_person2_d = 1
on_draw.snow_person1_x = 150
on_draw.snow_person1_d = 2
on_draw.stars_x = []
on_draw.stars_d = 0.5

stars_count = 150
frac_random = []
x_random = []
y_random = []
# star_pos = []
for i in range(stars_count):
    frac_random.append(random.randrange(0, 3))
    x_random.append(random.randrange(-50, SCREEN_WIDTH))
    f = x_random[i]
    on_draw.stars_x.append(f)
    y_random.append(random.randrange(
        int(SCREEN_HEIGHT/3 + 30), SCREEN_HEIGHT))

# for i in range(100):
#     on_draw.stars_d[i] = 0.5


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    # arcade.start_render()

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# def main():
#     arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
#     arcade.set_background_color(arcade.color.DARK_BLUE)
#     arcade.start_render()

#     draw_grass()

#     # Draw snow people
#     draw_snow_person(300, 140)
#     draw_snow_person(500, 170)

#     #  Finish and run
#     arcade.finish_render()
#     arcade.run()

# Call the main function to get the program started.
main()
