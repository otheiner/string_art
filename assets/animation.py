from string_art import StringArt
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")

nol = 2000

string_art = StringArt(number_of_lines = nol,
                       number_of_nails = 236)
string_art.set_image("./test_files/test_image_1.png")
string_art.compute_string(mask_weight=6)
sequence = string_art.get_string()

for i in range (1,nol):
    string_art.clear_plot()
    string_art.draw_frame()
    string_art.set_string_sequence(sequence[0:i])
    image = string_art.draw_string(show=False).figure
    image.savefig("./animation/output_{}.png".format(i), dpi=70)
    plt.close(image)

import imageio
from PIL import Image
from pathlib import Path

folder = Path("./animation/")
with imageio.get_writer('./animation.gif', mode='I', duration=0.005) as writer:
    for i in range(1,len(sequence)-1,5):
        filename = "./animation/output_{}.png".format(i)
        print(filename)
        img = Image.open(filename)
        img = img.resize((700, 700))
        writer.append_data(img)