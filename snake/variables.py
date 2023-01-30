import math

# CONSTANTS
# colors:
c_white = (255,255,255)
c_richblack = (0, 16, 17)
c_babyblue = (108, 207, 246)
c_lightgreen = (145, 245, 173)
c_lavender = (108, 207, 246)

# screen size:
scr_width = 320
scr_height = 240

# snake/game:
s_size = 10
s_speed = 10
s_foodsize = 10


# DEPENDENT VARIABLES
c_snake = c_lightgreen
c_food = c_babyblue
c_bg = c_richblack
c_contrast = (abs(255-c_bg[0]), abs(255-c_bg[1]), abs(255-c_bg[2]))
c_text = c_white

# message
# UNOPTIMIZED; find a way to do this that does not make use of strings as keys
msg_types = {
    "lose": (c_text, scr_width//4, scr_height//4),
    "score": (c_text, 0, 0),
    "update": (c_text, 100, 0)
}