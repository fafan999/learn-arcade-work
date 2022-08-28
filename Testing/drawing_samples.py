"""
Here I will draw using Arcade Library
Yeah, commenting is good
"""
# single line..
import arcade

# opens a window
arcade.open_window(600, 600, "Drawing Example")

# set the background color
# arcade.set_background_color((0, 255, 0))
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# get ready to draw
arcade.start_render()

# (the draing code comes here)
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.LIGHT_GREEN)

# Tree trunks
arcade.draw_rectangle_filled(center_x=100, center_y=320,
                             width=20, height=60,
                             color=arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(center_x=200,
                             center_y=320,
                             width=20,
                             height=60,
                             color=arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(center_x=300,
                             center_y=320,
                             width=20,
                             height=60,
                             color=arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(center_x=400,
                             center_y=320,
                             width=20,
                             height=60,
                             color=arcade.csscolor.SIENNA)

arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree tops
arcade.draw_circle_filled(center_x=100,
                          center_y=350,
                          radius=30,
                          color=arcade.csscolor.DARK_GREEN)

arcade.draw_ellipse_filled(center_x=200, center_y=370,
                           width=60, height=80,
                           color=arcade.csscolor.DARK_GREEN)

arcade.draw_arc_filled(center_x=300, center_y=340,
                       width=60, height=100,
                       color=arcade.csscolor.DARK_GREEN,
                       start_angle=0, end_angle=180)

arcade.draw_triangle_filled(x1=370, y1=320,
                            x2=430, y2=320,
                            x3=400, y3=420,
                            color=arcade.csscolor.DARK_GREEN)

arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw text
arcade.draw_text("Badacsonyi erdő. Ültess fát!",
                 80, 230, arcade.color.BLACK, 24)

# finish drawing
arcade.finish_render()

# keep the window up until someone closes it
arcade.run()
