# importing tkinter for gui
import tkinter as tk
from animate_gif import AnimateGIF 
# from draw_tiles import DrawTiles
from tkinter.constants import RAISED
from PIL import Image, ImageTk

# Create window
window = tk.Tk()

# Set Window Attributes
window.attributes('-fullscreen', True)
window.title("Pi of Catan")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set Background Image Attributes
bg_image_src = ImageTk.PhotoImage(Image.open('./waves3.jpeg'))
bg_image_width = 275
bg_image_height = 183

frame = tk.Frame(window, width=screen_width * 0.9, height=screen_height * 0.9) 
frame.place(x = screen_width * 0.05, y = screen_height * 0.05)

canvas = tk.Canvas(frame, bg="black", width=screen_width * 0.9, height=screen_height * 0.9)
canvas.pack()

# Draw Background
x_coor_delimitnator = 0
y_coor_delimitnator = 0
while x_coor_delimitnator<10:
    while y_coor_delimitnator<10:
        # background = AnimateGIF(window, 'waves2.gif')
        canvas.create_image(screen_width-(bg_image_width * y_coor_delimitnator), screen_height-(bg_image_height * x_coor_delimitnator), image=bg_image_src)
        y_coor_delimitnator += 1
    y_coor_delimitnator = 0
    x_coor_delimitnator += 1

# Draw Exit Button
exit_button_temp=Image.open('./img/buttons/exit_button.tiff')
exit_button_temp = exit_button_temp.resize((45, 45), Image.ANTIALIAS)
exit_button_src = ImageTk.PhotoImage(exit_button_temp)
exit_button = tk.Button(window, image=exit_button_src, command=quit)
exit_button.place(x = 5, y = 5)

# Draw Tile Refresh Button
refresh_button = tk.Button(window, text='Refresh', height=3, width=5, relief=RAISED, command=quit)
refresh_button.place(x = 60, y = 5)

# Draw Resource Tiles
tile_1_temp = Image.open('./img/tiles/brick.png')
tile_1_temp = tile_1_temp.resize((174, 200), Image.ANTIALIAS)
tile_1_src = ImageTk.PhotoImage(tile_1_temp)
canvas.create_image(400, 450, image=tile_1_src)

tile_2_temp = Image.open('./img/tiles/ore.png')
tile_2_temp = tile_2_temp.resize((174, 200), Image.ANTIALIAS)
tile_2_src = ImageTk.PhotoImage(tile_2_temp)
canvas.create_image(574, 450, image=tile_2_src)

tile_3_temp = Image.open('./img/tiles/wood.png').convert("RGBA")
tile_3_temp = tile_3_temp.resize((174, 200), Image.ANTIALIAS)
tile_3_src = ImageTk.PhotoImage(tile_3_temp)
canvas.create_image(748, 450, image=tile_3_src)

tile_4_temp = Image.open('./img/tiles/brick.png')
tile_4_temp = tile_4_temp.resize((174, 200), Image.ANTIALIAS)
tile_4_src = ImageTk.PhotoImage(tile_4_temp)
canvas.create_image(922, 450, image=tile_4_src)

tile_5_temp = Image.open('./img/tiles/wheat.png')
tile_5_temp = tile_5_temp.resize((174, 200), Image.ANTIALIAS)
tile_5_src = ImageTk.PhotoImage(tile_5_temp)
canvas.create_image(1096, 450, image=tile_5_src)


tile_6_temp = Image.open('./img/tiles/wheat.png')
tile_6_temp = tile_6_temp.resize((174, 200), Image.ANTIALIAS)
tile_6_src = ImageTk.PhotoImage(tile_6_temp)
canvas.create_image(487, 300, image=tile_6_src)

tile_7_temp = Image.open('./img/tiles/sheep.png')
tile_7_temp = tile_6_temp.resize((174, 200), Image.ANTIALIAS)
tile_7_src = ImageTk.PhotoImage(tile_7_temp)
canvas.create_image(661, 300, image=tile_7_src)


# Draw Number Tiles 

# Save State

window.mainloop()

