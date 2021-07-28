# importing tkinter for gui
import tkinter as tk
from animate_gif import AnimateGIF 
from draw_tiles import DrawTiles
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

# Draw Background
x_coor_delimitnator = 0
y_coor_delimitnator = 0
while x_coor_delimitnator<10:
    while y_coor_delimitnator<10:
        background = tk.Label(window, image = bg_image_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
        # background = AnimateGIF(window, 'waves2.gif')
        background.place(x = screen_width-(bg_image_width * y_coor_delimitnator), y = screen_height-(bg_image_height * x_coor_delimitnator))
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

frame = tk.Frame(window)
frame.place(x = screen_width * 0.05, y = screen_height * 0.05)

canvas = tk.Canvas(frame, width=screen_width * 0.9, height=screen_height * 0.9)
canvas.pack()

# Draw Resource Tiles
tile_1_temp = Image.open('./img/tiles/brick.png')
tile_1_temp = tile_1_temp.resize((174, 200), Image.ANTIALIAS)
tile_1_src = ImageTk.PhotoImage(tile_1_temp)
canvas.create_image(350,200,image=tile_1_src)
# tile_1 = tk.Label(window, image = tile_1_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
# tile_1.place(x = 100, y = 300)

tile_2_temp = Image.open('./img/tiles/ore.png')
tile_2_temp = tile_2_temp.resize((174, 200), Image.ANTIALIAS)
tile_2_src = ImageTk.PhotoImage(tile_2_temp)
tile_2 = tk.Label(window, image = tile_2_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_2.place(x = 275, y = 300)

tile_3_temp = Image.open('./img/tiles/wood.png')
tile_3_temp = tile_3_temp.resize((174, 200), Image.ANTIALIAS)
tile_3_src = ImageTk.PhotoImage(tile_3_temp)
tile_3 = tk.Label(window, image = tile_3_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_3.place(x = 500, y = 300)

tile_4_temp = Image.open('./img/tiles/brick.png')
tile_4_temp = tile_4_temp.resize((174, 200), Image.ANTIALIAS)
tile_4_src = ImageTk.PhotoImage(tile_4_temp)
tile_4 = tk.Label(window, image = tile_4_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_4.place(x = 700, y = 300)

tile_5_temp = Image.open('./img/tiles/wheat.png')
tile_5_temp = tile_5_temp.resize((174, 200), Image.ANTIALIAS)
tile_5_src = ImageTk.PhotoImage(tile_5_temp)
tile_5 = tk.Label(window, image = tile_5_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_5.place(x = 900, y = 300)

tile_6_temp = Image.open('./img/tiles/sheep.png')
tile_6_temp = tile_6_temp.resize((174, 200), Image.ANTIALIAS)
tile_6_src = ImageTk.PhotoImage(tile_6_temp)
tile_6 = tk.Label(window, image = tile_6_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_6.place(x = 1100, y = 300)

tile_7_temp = Image.open('./img/tiles/wood.png')
tile_7_temp = tile_7_temp.resize((174, 200), Image.ANTIALIAS)
tile_7_src = ImageTk.PhotoImage(tile_7_temp)
tile_7 = tk.Label(window, image = tile_7_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_7.place(x = 1300, y = 300)

tile_8_temp = Image.open('./img/tiles/brick.png')
tile_8_temp = tile_8_temp.resize((174, 200), Image.ANTIALIAS)
tile_8_src = ImageTk.PhotoImage(tile_8_temp)
tile_8 = tk.Label(window, image = tile_8_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_8.place(x = 1500, y = 300)

tile_9_temp = Image.open('./img/tiles/wheat.png')
tile_9_temp = tile_9_temp.resize((174, 200), Image.ANTIALIAS)
tile_9_src = ImageTk.PhotoImage(tile_9_temp)
tile_9 = tk.Label(window, image = tile_9_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_9.place(x = 300, y = 300)

tile_10_temp = Image.open('./img/tiles/ore.png')
tile_10_temp = tile_10_temp.resize((174, 200), Image.ANTIALIAS)
tile_10_src = ImageTk.PhotoImage(tile_10_temp)
tile_10 = tk.Label(window, image = tile_10_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_10.place(x = 300, y = 300)

tile_11_temp = Image.open('./img/tiles/wood.png')
tile_11_temp = tile_11_temp.resize((174, 200), Image.ANTIALIAS)
tile_11_src = ImageTk.PhotoImage(tile_11_temp)
tile_11 = tk.Label(window, image = tile_11_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_11.place(x = 300, y = 300)

tile_12_temp = Image.open('./img/tiles/brick.png')
tile_12_temp = tile_12_temp.resize((174, 200), Image.ANTIALIAS)
tile_12_src = ImageTk.PhotoImage(tile_12_temp)
tile_12 = tk.Label(window, image = tile_12_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_12.place(x = 300, y = 300)

tile_13_temp = Image.open('./img/tiles/wheat.png')
tile_13_temp = tile_13_temp.resize((174, 200), Image.ANTIALIAS)
tile_13_src = ImageTk.PhotoImage(tile_13_temp)
tile_13 = tk.Label(window, image = tile_13_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_13.place(x = 300, y = 300)

tile_14_temp = Image.open('./img/tiles/sheep.png')
tile_14_temp = tile_14_temp.resize((174, 200), Image.ANTIALIAS)
tile_14_src = ImageTk.PhotoImage(tile_14_temp)
tile_14 = tk.Label(window, image = tile_14_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_14.place(x = 300, y = 300)

tile_15_temp = Image.open('./img/tiles/wood.png')
tile_15_temp = tile_15_temp.resize((174, 200), Image.ANTIALIAS)
tile_15_src = ImageTk.PhotoImage(tile_15_temp)
tile_15 = tk.Label(window, image = tile_15_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_15.place(x = 300, y = 300)

tile_16_temp = Image.open('./img/tiles/ore.png')
tile_16_temp = tile_16_temp.resize((174, 200), Image.ANTIALIAS)
tile_16_src = ImageTk.PhotoImage(tile_16_temp)
tile_16 = tk.Label(window, image = tile_16_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_16.place(x = 300, y = 300)

tile_17_temp = Image.open('./img/tiles/brick.png')
tile_17_temp = tile_17_temp.resize((174, 200), Image.ANTIALIAS)
tile_17_src = ImageTk.PhotoImage(tile_17_temp)
tile_17 = tk.Label(window, image = tile_17_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_17.place(x = 300, y = 300)

tile_18_temp = Image.open('./img/tiles/wheat.png')
tile_18_temp = tile_18_temp.resize((174, 200), Image.ANTIALIAS)
tile_18_src = ImageTk.PhotoImage(tile_18_temp)
tile_18 = tk.Label(window, image = tile_18_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_18.place(x = 300, y = 300)

tile_19_temp = Image.open('./img/tiles/sheep.png')
tile_19_temp = tile_19_temp.resize((174, 200), Image.ANTIALIAS)
tile_19_src = ImageTk.PhotoImage(tile_19_temp)
tile_19 = tk.Label(window, image = tile_19_src, highlightthickness = 0, bd = 0,padx= 0, pady= 0)
tile_19.place(x = 300, y = 300)

# Draw Number Tiles 

# Save State

window.mainloop()

